from django.urls import path
from .views import CrossAuthView, UserUpdateView, IdentificationCheckView

app_name = "accounts"
urlpatterns = [
    path('cross-auth/', CrossAuthView.as_view(), name='cross-auth-view'),
    path('user/change/', UserUpdateView.as_view(), name='user-change'),
    path('identification-check/', IdentificationCheckView.as_view(), name='identification-check'),
]
