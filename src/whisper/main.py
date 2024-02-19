from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from notifications.signals import notify

from core.settings import EMAIL_HOST_USER


class NotificationService:

    def __init__(self, heading, description, obj=None, recipient_list=None):
        """
        :param heading > small line of message
        :param description > detailed down message
        :param obj > object to be notified
        :param recipient_list > list of users to be notified
        :return:
        """
        if recipient_list is None:
            recipient_list = []

        self.recipient_list = recipient_list
        self.heading = heading
        self.obj = obj
        self.description = description

    def send_email_notification_smtp(self, template, context, email=None):
        email_list = []
        if email:
            for recipient in email:
                email_list.append(recipient)
        else:
            for user in self.recipient_list:
                email_list.append(user.email)

        if email_list:
            try:
                context = context
                html_message = render_to_string(template, context)
                plain_message = strip_tags(html_message)
                from_email = EMAIL_HOST_USER
                send_mail(self.heading, plain_message, from_email, email_list, html_message=html_message)
            except Exception as e:
                print(e)

    def send_email_notification(self, template, context, email=None):
        pass

    def send_app_notification(self):
        for user in self.recipient_list:
            notify.send(self.obj, recipient=user, verb=self.heading, description=self.description, object=self.obj)

    def send_sms_notification(self):
        pass

    def send_push_notification(self):
        pass
