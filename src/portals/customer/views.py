from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
    TemplateView, CreateView, ListView,
)

from src.accounts.decorators import customer_required
from src.portals.company.models import Candidate, Job, Review


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'customer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['object_list'] = Candidate.objects.filter(user=self.request.user)
        context['application_all_count'] = Candidate.objects.filter(user=self.request.user).count()
        context['application_pen_count'] = Candidate.objects.filter(user=self.request.user, status='pen').count()
        context['application_acc_count'] = Candidate.objects.filter(user=self.request.user, status='acc').count()
        context['application_app_count'] = Candidate.objects.filter(user=self.request.user, status='app').count()
        return context


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class ReviewsListView(ListView):
    template_name = 'customer/review_list.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


# VERIFIED : TESTED
@method_decorator(customer_required, name='dispatch')
class ReviewCreateView(CreateView):
    template_name = 'customer/review_form.html'
    model = Review
    fields = ['rating', 'description']
    success_url = reverse_lazy('customer:review-list')

    def dispatch(self, request, *args, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])

        if Review.objects.filter(user=request.user, job=job):
            messages.error(request, 'You have already added your review to this job.')
            return redirect('customer:review-list')

        return super(ReviewCreateView, self).dispatch(request)

    def form_valid(self, form):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.job = job

        return super(ReviewCreateView, self).form_valid(form)