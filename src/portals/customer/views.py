from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView, CreateView, ListView,
)
from notifications.signals import notify

from src.accounts.decorators import customer_required
from src.accounts.models import City
from src.portals.company.bll import recommended_jobs_for_candidate
from src.portals.company.models import Candidate, Job, Review


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['review_count'] = Review.objects.filter(user=self.request.user).count()
        context['jobs'] = recommended_jobs_for_candidate(self.request.user)

        # for job in Job.objects.all():
        #     job.city = City.objects.order_by('?').first()
        #     job.save()

        return context


@method_decorator(customer_required, name='dispatch')
class JobListView(ListView):
    model = Job
    template_name = 'customer/job_list.html'

    def get_queryset(self):
        return Job.objects.filter().exclude()


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class MyReviewListView(ListView):
    template_name = 'customer/my_review_list.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class ReviewCreateView(CreateView):
    template_name = 'customer/review_form.html'
    model = Review
    fields = ['rating', 'description']
    success_url = reverse_lazy('customer:job-list')

    def dispatch(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])

        if Review.objects.filter(user=request.user, job=job):
            messages.error(request, 'You have already added your review to this job.')
            return redirect('customer:job-list')

        return super(ReviewCreateView, self).dispatch(request)

    def form_valid(self, form):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.job = job

        return super(ReviewCreateView, self).form_valid(form)


@method_decorator(customer_required, name='dispatch')
class ReviewListView(ListView):
    template_name = 'customer/review_list.html'

    def get_queryset(self):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])
        return Review.objects.filter(job=job)

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['job'] = get_object_or_404(Job, pk=self.kwargs['pk'])
        return context
