from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from src.portals.company.filters import JobFilter
from src.portals.company.models import Job, Company
from src.website.forms import ContactForm

from django.shortcuts import render


# Class for handling the home page view, displaying a list of internships with various filters
class HomeView(ListView):
    model = Job
    template_name = 'website/home.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Retrieve jobs with 'open' status
        jobs = Job.objects.filter(status='open')

        # If user is authenticated, filter out jobs related to the user (likes and enrolled jobs)
        if self.request.user.is_authenticated:
            jobs_candidate_user = Job.objects.filter(candidate__user=self.request.user).values('pk')
            jobs_liked_by_user = Job.objects.filter(likes=self.request.user).values('pk')
            likes_list = [x['pk'] for x in jobs_liked_by_user]
            jobs = jobs.exclude(pk__in=jobs_candidate_user)
            kwargs['like_ids'] = likes_list

        # Apply additional filters and set up pagination
        filter_object = JobFilter(self.request.GET, queryset=jobs)
        kwargs['filter_form'] = filter_object.form
        paginator = Paginator(filter_object.qs, 50)
        page_number = self.request.GET.get('page')
        page_object = paginator.get_page(page_number)

        # Add companies and paginated job list to context
        kwargs['companies'] = Company.objects.all()[:5]
        kwargs['object_list'] = page_object

        return super().get_context_data(**kwargs)


# Class for displaying the 'About' page
class AboutView(TemplateView):
    template_name = 'website/about.html'


# Class for handling the 'Contact' page, with GET and POST methods for form submission
class ContactView(View):
    form = ContactForm
    template_name = 'website/contact.html'

    def get(self, request):
        # Render the contact form
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        # Process form submission and display success or error messages
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
        return render(request, self.template_name, {'form': self.form}) if form.is_valid() else render(request,
                                                                                                       self.template_name,
                                                                                                       {'form': form})


# Class for displaying a list of internship jobs
class InternshipView(ListView):
    model = Job
    template_name = 'website/internship.html'

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return Job.objects.filter(Q(title__icontains=query))
        return Job.objects.all()


# Class for displaying details of a specific internship job
class InternshipDetailsView(DetailView):
    model = Job
    template_name = 'website/internship_details.html'

    def get_context_data(self, **kwargs):
        # Add additional context data for displaying related internships
        context = super().get_context_data()
        context['internships'] = Job.objects.all()[:3]
        return context


# Class for displaying a list of companies
class CompanyView(ListView):
    model = Company
    template_name = 'website/company.html'

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query:
            return Company.objects.filter(Q(name__icontains=query))
        return Company.objects.all()


# Class for displaying details of a specific company
class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'website/company_details.html'

    def get_context_data(self, **kwargs):
        # Add additional context data for displaying related companies
        context = super().get_context_data()
        context['companies'] = Company.objects.all()[:3]
        return context


# Class for displaying details of a specific project
class ProjectView(DetailView):
    model = Job
    template_name = 'website/project_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        # Specify the queryset for retrieving project details along with related company information
        return Job.objects.select_related('company').all()
