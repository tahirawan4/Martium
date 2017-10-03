from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

app = Celery('feedly')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_default_queue = 'default'

app.autodiscover_tasks()

# task_routes = {
#     'tasks.feed_importer': 'low-priority',
# }