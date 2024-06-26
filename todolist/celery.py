from celery import Celery

import os

import django
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todolist.settings')

django.setup()

app = Celery('todolist',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0'
             )

app.conf.beat_schedule = {
    'send-daily-emails': {
        'task': 'base.tasks.send_daily_emails',
        'schedule': crontab(),
    },
}

app.conf.timezone = 'UTC'
app.autodiscover_tasks()
