# Django URL patterns for mapping views to specific URLs
from django.urls import path
from .views import HomeView, ProjectView, AboutView, ContactView, InternshipView, CompanyView, InternshipDetailsView, \
    CompanyDetailsView

app_name = 'website'
urlpatterns = [

    # URL pattern for the home page
    path('', HomeView.as_view(), name='home'),

    # URL pattern for the 'About' page
    path('about/', AboutView.as_view(), name='about'),

    # URL pattern for the 'Contact' page, handling both GET and POST requests
    path('contact/', ContactView.as_view(), name='contact'),

    # URL pattern for displaying a list of internship jobs
    path('internship/', InternshipView.as_view(), name='internship'),

    # URL pattern for displaying details of a specific internship job, using slug as a parameter
    path('internship/details/<slug:pk>', InternshipDetailsView.as_view(), name='internship-details'),

    # URL pattern for displaying a list of companies
    path('company/', CompanyView.as_view(), name='company'),

    # URL pattern for displaying details of a specific company, using slug as a parameter
    path('company/details/<slug:pk>', CompanyDetailsView.as_view(), name='company-details'),

    # URL pattern for displaying details of a specific project, using int as a parameter
    path('project/<int:pk>/', ProjectView.as_view(), name='project-detail'),

]
