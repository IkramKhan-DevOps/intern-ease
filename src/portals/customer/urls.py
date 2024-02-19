from django.urls import path
from .views import (
    DashboardView, ReviewsListView, ReviewCreateView
)

app_name = 'customer'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    path('review/', ReviewsListView.as_view(), name='review-list'),
    path('review/job/<int:pk>/create/', ReviewCreateView.as_view(), name='review-create'),
]
