from ckeditor.fields import RichTextField
from django.db import models
from src.accounts.models import User


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


class Company(models.Model):
    BUSINESS_TYPE = (
        ('non profit', 'Non Profit'),
        ('government', 'Government'),
        ('small business', 'Small Business'),
        ('medium business', 'Medium Business'),
        ('enterprise', 'Enterprise'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="Name")
    tag_line = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    business_type = models.CharField(
        max_length=255, choices=BUSINESS_TYPE, default='small business', verbose_name='Company Type'
    )

    logo = models.ImageField(upload_to='company_logo', null=True, blank=True)
    company_registration_no = models.CharField(max_length=255, null=True, blank=True)
    company_start_date = models.DateTimeField(verbose_name='Date started', null=True, blank=True)

    contact_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Phone')
    contact_email = models.CharField(max_length=255, null=True, blank=True, verbose_name='Email')
    company_address = models.TextField(null=True, blank=True, verbose_name='Address')

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# MODEL JOBS
class Job(models.Model):
    STATUS_CHOICE = (
        ('open', 'Open'),
        ('close', 'Close')
    )
    JOB_TYPE = (
        ('full time', 'Full Time'),
        ('part time', 'Part Time'),
        ('remote', 'Remote'),
        ('freelance', 'Freelance'),
        ('internship', 'Internship'),
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vacancy = models.IntegerField(default=0)
    description = models.TextField()
    detailed_description = RichTextField(null=True, blank=True)
    company = models.ForeignKey('Company', related_name='job_provider', on_delete=models.CASCADE, blank=True)
    logo = models.ImageField(upload_to='company_logo', null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')
    candidates = models.ManyToManyField(User, related_name='candidates', through='Candidate')
    status = models.CharField(max_length=5, choices=STATUS_CHOICE, default='open')

    job_type = models.CharField(max_length=50, null=True, blank=True, default='internship', choices=JOB_TYPE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-pk']
        verbose_name = "InternShip"
        verbose_name_plural = "InternShips"

    def __str__(self):
        return self.title


# CANDIDATE
class Candidate(models.Model):
    STATUS_CHOICE = (
        ('acc', 'Accepted'),
        ('pen', 'Pending'),
        ('app', 'Applied'),
        ('rej', 'Rejected'),
    )
    DEGREE_CHOICES=(
        ('ssc', 'Matric'),
        ('hssc', 'F.sc'),
        ('bs', 'Bachelors'),
        ('ms', 'Master'),
        ('phd', 'Doctorate'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    degree = models.CharField(
        max_length=15,
        choices=DEGREE_CHOICES,
        default='ssc',
        help_text="Name of Field in which you have passed bachelors - Leave blank if you don't have bachelors degree"
    )
    experience = models.PositiveIntegerField(default=0, help_text="Years of working experience")
    about = models.TextField(
        null=True, blank=True,
        help_text='Say something about yourself, your love to hear you, briefly describe yourself, interests etc'
    )
    previous_company = models.CharField(max_length=255, null=True, blank=True, help_text="Leave blank if not")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICE, default='app')
    cv = models.FileField(upload_to='company/candidate/cvs/',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title


# FEEDBACK
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name
