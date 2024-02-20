from src.portals.company.bll import recommended_candidates_for_job
from src.whisper.main import NotificationService


def sent_job_create_notification(obj):
    recipient_list = recommended_candidates_for_job(obj)

    notification_service = NotificationService(
        heading="Job Recommendation",
        description="A new job has been created that matches your profile. Check it out now!",
        obj=obj,
        recipient_list=recipient_list
    )
    notification_service.send_app_notification()


