from django.contrib import messages
from django.db.models import Q
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from src.portals.company.models import Job, Company, Review
from src.website.filters import CompanyFilter, InternshipFilter
from src.website.forms import ContactForm

from django.shortcuts import render


# Class for handling the home page view, displaying a list of internships with various filters
class HomeView(ListView):
    model = Job
    template_name = 'website/home.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['companies'] = Company.objects.all()[:5]
        kwargs['object_list'] = Job.objects.filter(job_type='internship')[:5]
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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = InternshipFilter(self.request.GET, queryset=self.get_queryset())
        context['object_list'] = filter_form.qs
        context['form'] = filter_form.form
        print(filter_form.form)
        return context


# Class for displaying details of a specific internship job
class InternshipDetailsView(DetailView):
    model = Job
    template_name = 'website/internship_details.html'

    def get_context_data(self, **kwargs):
        # Add additional context data for displaying related internships
        context = super().get_context_data()
        context['internships'] = Job.objects.filter(status='o', company=self.object.company)[:3]
        context['reviews'] = Review.objects.filter(job=self.object)
        return context


# Class for displaying a list of companies
class CompanyView(ListView):
    model = Company
    template_name = 'website/company.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter_form = CompanyFilter(self.request.GET, queryset=self.get_queryset())
        context['object_list'] = filter_form.qs
        context['form'] = filter_form.form
        print(filter_form.form)
        return context


# Class for displaying details of a specific company
class CompanyDetailsView(DetailView):
    model = Company
    template_name = 'website/company_details.html'

    def get_context_data(self, **kwargs):
        # Add additional context data for displaying related companies
        context = super().get_context_data()
        context['internships'] = Job.objects.filter(company=self.object)[:3]

        return context


# Class for displaying details of a specific project
class ProjectView(DetailView):
    model = Job
    template_name = 'website/project_detail.html'
    context_object_name = 'object'

    def get_queryset(self):
        # Specify the queryset for retrieving project details along with related company information
        return Job.objects.select_related('company').all()
