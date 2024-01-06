from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.beat_schedule = {
    'repeating_task_in_every_2_sec': {
        'task': 'main.tasks.repeating_task',
        'schedule': 2,
    }
}
