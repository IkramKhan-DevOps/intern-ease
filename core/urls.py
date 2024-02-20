import notifications
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.views.static import serve

from .settings import MEDIA_ROOT, STATIC_ROOT, ENVIRONMENT

urlpatterns = [
    # REQUIRED --------------------------------------------------------- #
    path('admin/', admin.site.urls),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),

    # PORTALS ---------------------------------------------------------- #
    path('', include('src.website.urls', namespace='website')),
    path('s/', include('src.portals.customer.urls', namespace='customer')),
    path('c/', include('src.portals.company.urls', namespace='company')),
]

""" STATIC AND MEDIA FILES ----------------------------------------------------------------------------------------- """
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

urlpatterns += [
    path('inbox/notifications/', include('notifications.urls', namespace='notifications')),
]

""" DEVELOPMENT ONLY -------------------------------------------------------------------------------------------- """
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
