from celery import shared_task
from smtplib import SMTP
from email.mime.text import MIMEText
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

from todolist.celery import app


@app.task
def send_daily_emails():
    users = User.objects.all()
    for user in users:
        print("Email: " + user.email)
        send_mail(
            subject='Test',
            message='Message text',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )


send_daily_emails.delay()
