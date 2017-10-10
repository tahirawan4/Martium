from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "feedly.settings.local")

app = Celery('feedly')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_default_queue = 'default'
app.autodiscover_tasks()

import django

django.setup()
from parser.tasks import feed_importer


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(600.0, feed_importer.s(''), name='Run After event 10 minutes')
    # Executes every Monday morning at 7:30 a.m.
    # sender.add_periodic_task(
    #     crontab(hour=7, minute=30, day_of_week=1),
    #     feed_importer.s(''),
    # )
