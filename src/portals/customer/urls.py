from django.urls import path
from .views import (
    DashboardView, MyReviewListView, ReviewCreateView, JobListView, ReviewListView
)

app_name = 'customer'
urlpatterns = [

    path('', DashboardView.as_view(), name='dashboard'),
    path('my/reviews/', MyReviewListView.as_view(), name='my-review-list'),

    path('job/', JobListView.as_view(), name='job-list'),
    path('job/<int:pk>/review/create/', ReviewCreateView.as_view(), name='review-create'),
    path('job/<int:pk>/review/', ReviewListView.as_view(), name='review-list'),
]
