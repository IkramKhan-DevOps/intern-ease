from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView, TemplateView

from src.portals.company.filters import JobFilter
from src.portals.company.models import Job


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

        context['object_list'] = page_object
        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'


class ContactView(TemplateView):
    template_name = 'website/contact.html'


class InternshipView(TemplateView):
    template_name = 'website/internship.html'


class ProjectView(DetailView):
    template_name = 'website/project_detail.html'
    model = Job
    context_object_name = 'object'

    def get_queryset(self):
        return Job.objects.select_related('company').all()
