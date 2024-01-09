from django.urls import path
from .views import (
    JobUpdateView, JobListView, JobCreateView, JobDeleteView, CandidateListView, JobLikeListView, JobStatusUpdate,
    DashboardView, CompanyUpdateView, CandidateDetailView, CandidateStatusUpdate, CandidateStatusDelete
)

app_name = 'company'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('company/profile/', CompanyUpdateView.as_view(), name='company-update'),
    path('job/', JobListView.as_view(), name='job-list'),
    path('job/add/', JobCreateView.as_view(), name='job-add'),
    path('job/<int:pk>/change/', JobUpdateView.as_view(), name='job-update'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('job/<int:pk>/status/', JobStatusUpdate.as_view(), name='job-status'),
    path('job/<int:pk>/likes/', JobLikeListView.as_view(), name='job-likes-list'),
    path('job/<int:pk>/candidates/', CandidateListView.as_view(), name='candidate-list'),
    path('job/<int:job>/candidate/<int:pk>/', CandidateDetailView.as_view(), name='candidate-detail'),
    path('job/<int:job>/candidate/<int:pk>/action/<str:action>/', CandidateStatusUpdate.as_view(), name='candidate'
                                                                                                        '-status-update'),
    path('job/<int:job>/candidate/<int:pk>/delete', CandidateStatusDelete.as_view(), name='candidate-status-delete'),

]
