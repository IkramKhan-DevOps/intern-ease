import django_filters
from django.forms import TextInput

from src.portals.company.models import Job


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Job Title'}), lookup_expr='icontains')
    company = django_filters.CharFilter(widget=TextInput(attrs={'placeholder': 'Company'}), lookup_expr='icontains')

    class Meta:
        model = Job
        fields = {
            'category': ['exact'],
        }
