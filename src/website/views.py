from django.contrib import messages
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from src.portals.company.filters import JobFilter
from src.portals.company.models import Job, Company
from src.website.forms import ContactForm

from django.shortcuts import render


class HomeView(ListView):
    template_name = 'website/home.html'
    paginate_by = 20
    model = Job

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        jobs = Job.objects.filter(status='o')

        # IF AUTHENTICATED USER
        if self.request.user.is_authenticated:
            # GETTING LIKES AND ENROLLED JOBS
            jobs_candidate_user = Job.objects.filter(candidate__user=self.request.user).values('pk')
            jobs_liked_by_user = Job.objects.filter(likes=self.request.user).values('pk')
            likes_list = [x['pk'] for x in jobs_liked_by_user]

            # OPEN AND CLOSE FILTERS
            jobs = jobs.exclude(pk__in=jobs_candidate_user)
            context['like_ids'] = likes_list

        # IF NOT AND FOR ALL
        filter_object = JobFilter(self.request.GET, queryset=jobs)
        context['filter_form'] = filter_object.form

        paginator = Paginator(filter_object.qs, 50)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        context['companies'] = Company.objects.all()[:5]
        context['object_list'] = page_object

        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'


class ContactView(View):
    form = ContactForm
    template_name = 'website/contact.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return render(request, self.template_name, {'form': self.form})
        else:
            return render(request, self.template_name, {'form': form})


class InternshipView(ListView):
    model = Job
    template_name = 'website/internship.html'


class InternshipDetailsView(DetailView):
    model = Job
    template_name = 'website/internship_details.html'


class CompanyView(ListView):
    model = Company
    template_name = 'website/company.html'


class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'website/company_details.html'


class ProjectView(DetailView):
    template_name = 'website/project_detail.html'
    model = Job
    context_object_name = 'object'

    def get_queryset(self):
        return Job.objects.select_related('company').all()
