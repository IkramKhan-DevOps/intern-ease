from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'tagline', 'description', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'short_name', 'tagline', 'description']
    list_per_page = 10
    fieldsets = [
        ('Application', {'fields': ['name', 'short_name', 'tagline', 'description']}),
        ('Favicon', {'fields': ['favicon']}),
        ('Logo', {'fields': ['logo', 'logo_dark', 'logo_light']}),
        ('Contact', {'fields': ['contact_email1', 'contact_email2', 'contact_phone1', 'contact_phone2']}),
        ('Address', {'fields': ['address', 'latitude', 'longitude']}),
        ('Terms and Conditions', {'fields': ['terms_url']}),
        ('Version', {'fields': ['version']}),
        ('Status', {'fields': ['is_active']}),
    ]
    readonly_fields = ['created_on']


admin.site.register(Application, ApplicationAdmin)
