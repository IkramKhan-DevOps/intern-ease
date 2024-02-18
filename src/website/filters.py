import django_filters
from django.forms import DateTimeInput

from src.portals.company.models import Company, Job


class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = Company
        fields = ['name', 'business_type', 'company_registration_no', 'company_address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['name'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['business_type'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search By  title'})
        self.form.fields['company_registration_no'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['company_address'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search By Company'})


class IntershipFilter(django_filters.FilterSet):
    start_time = django_filters.DateTimeFilter(
        label='Start On',
        widget=DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'Select Started On'})
    )

    end_time = django_filters.DateTimeFilter(
        label='End On',
        widget=DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'Select Expiration Date and Time'})
    )

    class Meta:
        model = Job
        fields = ['title', "job_type", "category", 'company__name', 'status', "country", "start_time", "end_time", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields['category'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search By  title'})
        self.form.fields['status'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['company__name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Search By Company'})
        self.form.fields['country'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['start_time'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['end_time'].widget.attrs.update(
            {'class': 'form-control', })
        self.form.fields['job_type'].widget.attrs.update(
            {'class': 'form-control', })