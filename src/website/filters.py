import django_filters
from django.forms import DateTimeInput

from src.portals.company.models import Company, Job


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['name', 'business_type', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Search by Name'
            }
        )
        self.form.fields['business_type'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Company Type'
            }
        )
        self.form.fields['city'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'City'
            }
        )


class InternshipFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Job
        fields = ['title', "job_type", "category", 'company', 'status', "country"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['title'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Search by Title'
            }
        )
        self.form.fields['category'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.form.fields['status'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.form.fields['company'].widget.attrs.update(
            {
                'class': 'form-control',
                'placeholder': 'Search By Company'
            }
        )
        self.form.fields['country'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
        self.form.fields['job_type'].widget.attrs.update(
            {
                'class': 'form-control',
            }
        )
