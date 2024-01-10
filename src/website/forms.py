from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['name'].widget.attrs['class'] = 'form-input border border-slate-100 dark:border-slate-800 mt-2'

        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['email'].widget.attrs['class'] = 'form-input border border-slate-100 dark:border-slate-800 mt-2'

        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'
        self.fields['message'].widget.attrs['class'] = 'form-input border border-slate-100 dark:border-slate-800 mt-2'
