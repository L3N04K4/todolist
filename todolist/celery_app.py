import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

app = Celery('todolist')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
# app.autodiscover_tasks()

@app.task
def test_task():
    time.sleep(10)
    print('test task for celery')

@app.task
def send_test_email():
    smtp_host = 'localhost'
    smtp_port = 1025

    sender_email = 'your-email@example.com'
    receiver_email = 'korablin1605@gmail.com'
    email_header = 'Тестовое письмо'
    email_body = 'Это тестовое письмо, отправленное через Celery.'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = email_header

    body = email_body
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.sendmail(sender_email, receiver_email, message.as_string())

    print('Письмо успешно отправлено!')

# app.conf.beat_schedule = {
#     'send-test-email-every-5-minutes': {
#         'task': 'webshop.celery_email.send_test_email',
#         'schedule': crontab(minute='*/5'),
#     },
# }
