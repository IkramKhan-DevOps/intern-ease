from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, TemplateView, DetailView
from src.accounts.decorators import company_required
from src.portals.company.bll import get_user_company_bll
from .models import Job, Company, Candidate, Review


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'company/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        jobs = Job.objects.filter(company__user=self.request.user)

        context['jobs'] = jobs[:10]
        context['jobs_all_count'] = jobs.count()
        context['jobs_open_count'] = jobs.filter(status='open').count()
        context['jobs_close_count'] = jobs.filter(status='close').count()
        return context


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class CompanyUpdateView(UpdateView):
    model = Company
    fields = [
        'name', 'business_type', 'tag_line', 'description', 'contact_number',
        'contact_email', 'company_address'
    ]

    def get_success_url(self):
        messages.success(self.request, 'Company Profile Updated Successfully.')
        return reverse_lazy('company:company-update')

    def get_object(self, queryset=None):
        return get_user_company_bll(self.request.user)


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class JobListView(ListView):
    model = Job

    def get_queryset(self):
        return Job.objects.filter(company__user=self.request.user).exclude()


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class JobCreateView(CreateView):
    model = Job
    fields = ['title', 'category', 'vacancy', 'description', 'city', 'country', 'start_time', 'end_time']
    success_url = reverse_lazy('company:job-list')

    def form_valid(self, form):
        form.instance.company = get_user_company_bll(self.request.user)
        return super(JobCreateView, self).form_valid(form)


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class JobUpdateView(UpdateView):
    model = Job
    fields = ['title', 'category', 'vacancy', 'description', 'city', 'country', 'start_time', 'end_time']
    success_url = reverse_lazy('company:job-list')

    def get_object(self, queryset=None):
        return get_object_or_404(
            Job.objects.filter(
                company__user=self.request.user
            ), pk=self.kwargs['pk']
        )


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class JobDeleteView(DeleteView):
    model = Job
    success_url = reverse_lazy('company:job-list')

    def get_object(self, queryset=None):
        return get_object_or_404(
            Job.objects.filter(
                company__user=self.request.user
            ), pk=self.kwargs['pk']
        )


# VERIFIED : TESTED
@method_decorator(company_required, name='dispatch')
class ReviewListView(ListView):

    def get_queryset(self):
        job = get_object_or_404(Job.objects.filter(company__user=self.request.user), pk=self.kwargs['pk'])
        return Review.objects.filter(job=job)

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['job'] = get_object_or_404(Job.objects.filter(company__user=self.request.user), pk=self.kwargs['pk'])
        return context
