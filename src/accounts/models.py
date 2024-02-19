from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=3, null=True, blank=True, help_text="Short name of country like 'US', 'GB'")
    phone_code = models.CharField(max_length=5, null=True, blank=True, help_text="Phone code of country like '+92', '+1'")
    language = models.CharField(max_length=255, null=True, blank=True, help_text="Language of country like 'English', 'Urdu'")
    currency = models.CharField(max_length=255, null=True, blank=True, help_text="Currency of country like 'USD', 'PKR'")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['name']


class User(AbstractUser):
    GENDER_CHOICE = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    is_customer = models.BooleanField(default=False, help_text="This account belongs to customer")
    is_company = models.BooleanField(default=False, help_text="This account belongs to Company")
    is_completed = models.BooleanField(default=False, help_text="Is user fully fully identified to access application")

    profile_image = models.ImageField(
        null=True, blank=True,
        upload_to='images/profiles/',
        verbose_name="Profile Picture", help_text="Profile image must be 150*150 in size of png, jpg or jpeg"
    )
    gender = models.CharField(max_length=1, null=False, blank=True, choices=GENDER_CHOICE)
    about = models.TextField(null=True, blank=True, help_text="Tell us something interesting about yourself")
    address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=False)
    categories = models.ManyToManyField(Category)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    def delete(self, *args, **kwargs):
        self.profile_image.delete(save=True)
        super(User, self).delete(*args, **kwargs)
