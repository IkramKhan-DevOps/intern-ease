from .models import (
    Job,
)

from django.db.models.signals import post_save
from django.dispatch import receiver

from .notifier import sent_job_create_notification


@receiver(post_save, sender=Job)
def job_create_post_save(sender, instance, created, **kwargs):
    if created:
        sent_job_create_notification(instance)

