from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Model for storing application details
class Application(models.Model):
    name = models.CharField(max_length=100, help_text='Application name', default='Intern Ease')
    short_name = models.CharField(max_length=10, help_text='Your application short name', default='EE')
    tagline = models.CharField(
        max_length=100, help_text='Your application business line', default='Empowering Futures through Collaboration'
    )
    description = models.TextField(
        default="Connect companies offering enriching internships with aspiring students seeking valuable experiences",
        help_text='Application description'
    )

    favicon = models.ImageField(
        upload_to='core/application/images', null=True, blank=True, help_text='Application favicon'
    )
    logo = models.ImageField(
        upload_to='core/application/images', null=True, blank=True,
        help_text='Application real colors logo'
    )
    logo_dark = models.ImageField(
        upload_to='core/application/images', null=True, blank=True, help_text='For dark theme only'
    )
    logo_light = models.ImageField(
        upload_to='core/application/images', null=True, blank=True, help_text='For light theme only'
    )

    contact_email1 = models.EmailField(
        max_length=100, default='support@internease.com', help_text='Application contact email 1'
    )
    contact_email2 = models.EmailField(
        max_length=100, default='support@internease.com', help_text='Application contact email 2'
    )
    contact_phone1 = PhoneNumberField(
        help_text='Application contact phone 1', default='+10000000000'
    )
    contact_phone2 = PhoneNumberField(
        help_text='Application contact phone 2', default='+10000000000'
    )

    address = models.CharField(
        max_length=255, help_text='Office address', default='XYZ, City, Country'
    )
    latitude = models.DecimalField(max_digits=10, decimal_places=6, help_text='Latitude', default=23.7)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, help_text='Longitude', default=90.3)

    terms_url = models.URLField(
        max_length=255, default='https://internease.com/terms-of-use/', help_text='Terms and Conditions page link'
    )

    version = models.CharField(max_length=10, help_text='Current version', default='1.0.0')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Application"
        ordering = ['name']

    def __str__(self):
        return self.name

    # Validate only one record exists
    def clean_fields(self, exclude=None):
        if Application.objects.exists() and not self.pk:
            raise ValidationError("Only one record allowed.")
        super(Application, self).clean_fields(exclude=exclude)


# Model for storing contact details
class Contact(models.Model):
    name = models.CharField(max_length=100, help_text='Contact name')
    email = models.EmailField(max_length=100, help_text='Contact email')
    message = models.TextField(help_text='Contact message')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact"
        ordering = ['name']

    def __str__(self):
        return self.name
