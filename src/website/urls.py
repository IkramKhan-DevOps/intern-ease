from django.urls import path
from .views import HomeView, ProjectView, AboutView, ContactView, InternshipView, CompanyView, InternshipDetailsView, \
    CompanyDetailsView

app_name = 'website'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),

    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('internship/', InternshipView.as_view(), name='internship'),
    path('internship/details/<slug:pk>', InternshipDetailsView.as_view(), name='internship-details'),
    path('company/', CompanyView.as_view(), name='company'),
    path('company/details/<slug:pk>', CompanyDetailsView.as_view(), name='company-details'),

    path('project/<int:pk>/', ProjectView.as_view(), name='project-detail'),

]
