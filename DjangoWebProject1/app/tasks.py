from celery import task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from app.models import Usuario

logger = get_task_logger(__name__)


@task()
def add(x, y):
	send_mail(
    'Subject here',
    'Here is the message.',
    'enjeidevelopment@gmail.com',
    ['nicolas.dibiase22@gmail.com'],
    fail_silently=False,
)
