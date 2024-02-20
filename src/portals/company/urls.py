from django.urls import path
from .views import (
    JobUpdateView, JobListView, JobCreateView, JobDeleteView,
    DashboardView, CompanyUpdateView, ReviewListView
)

app_name = 'company'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('company/', CompanyUpdateView.as_view(), name='company-update'),

    path('job/', JobListView.as_view(), name='job-list'),
    path('job/add/', JobCreateView.as_view(), name='job-add'),
    path('job/<int:pk>/change/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),

    path('job/<int:pk>/review/', ReviewListView.as_view(), name='review-list'),

]
