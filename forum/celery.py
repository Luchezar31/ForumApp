import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ForumApp.settings')


app = Celery('ForumApp')
app.config_from_object('django.conf:settings',namespace="CELERY")
app.autodiscover_tasks()

