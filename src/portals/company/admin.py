from django.contrib import admin
from .models import (
    Company, Candidate, Feedback, Job
)


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'company', 'end_time', 'status', 'is_active', 'created_on']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['user', 'job', 'status', 'created_on']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'created_on']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'tag_line', 'business_type', ]


admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Feedback, FeedbackAdmin)
