from django.urls import path
from .views import (
    DashboardView, CandidateListView, CandidateCreateView, CandidateDeleteView, CandidateUpdateView, CandidateLikeView
)

app_name = 'customer'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('job/', CandidateListView.as_view(), name='application-list'),
    path('job/<int:pk>/apply/', CandidateCreateView.as_view(), name='application-apply'),
    path('job/<int:pk>/like/', CandidateLikeView.as_view(), name='job-like'),
    path('job/application/<int:pk>/update/', CandidateUpdateView.as_view(), name='application-update'),
    path('job/application/<int:pk>/delete/', CandidateDeleteView.as_view(), name='application-delete'),
]
