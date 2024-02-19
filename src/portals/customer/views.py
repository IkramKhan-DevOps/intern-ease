from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (
    TemplateView, CreateView, DetailView, ListView,
    UpdateView, DeleteView
)

from src.accounts.decorators import customer_required
from src.portals.company.models import Candidate, Job


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


@method_decorator(customer_required, name='dispatch')
class CandidateListView(ListView):
    template_name = 'customer/candidate_list.html'

    def get_queryset(self):
        return Candidate.objects.filter(user=self.request.user)


@method_decorator(customer_required, name='dispatch')
class CandidateCreateView(CreateView):
    template_name = 'customer/candidate_form.html'
    model = Candidate
    fields = ['degree', 'experience', 'about', 'previous_company', 'cv']
    success_url = reverse_lazy('customer:application-list')

    def dispatch(self, request, *args, **kwargs):
        job = get_object_or_404(Job.objects.all(), pk=kwargs['pk'])
        if Candidate.objects.filter(user=request.user, job=job):
            messages.error(request, 'You have already applied to this job.')
            return redirect('customer:application-list')
        return super(CandidateCreateView, self).dispatch(request)

    def form_valid(self, form):
        job = get_object_or_404(Job.objects.all(), pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.job = job
        return super(CandidateCreateView, self).form_valid(form)


@method_decorator(customer_required, name='dispatch')
class CandidateUpdateView(UpdateView):
    template_name = 'customer/candidate_form.html'
    model = Candidate
    fields = ['degree', 'experience', 'about', 'previous_company', 'cv']
    success_url = reverse_lazy('customer:application-list')

    def form_valid(self, form):
        return super(CandidateUpdateView, self).form_valid(form)


@method_decorator(customer_required, name='dispatch')
class CandidateDeleteView(DeleteView):
    template_name = 'customer/candidate_confirm_delete.html'
    model = Candidate
    success_url = reverse_lazy('customer:application-list')


@method_decorator(customer_required, name='dispatch')
class CandidateLikeView(View):

    def get(self, request, pk):
        job = get_object_or_404(Job.objects.all(), pk=pk)
        if not Job.objects.filter(pk=job.pk, likes=request.user):
            print("Liked this post successfully")
            job.likes.add(request.user)
        else:
            print("disliked this post successfully")
            job.likes.remove(request.user)

        j = job.save()
        print(j)
        return redirect('website:home')
