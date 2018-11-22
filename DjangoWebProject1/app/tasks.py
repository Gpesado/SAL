from celery import task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from app.models import *

logger = get_task_logger(__name__)


@task()
def add(x, y):
	
	queryset = Incidente.objects.all().order_by(F('cantidad_asignados') - F('cantidad_cerrados'))[:1]   	
	
	for each in queryset:
                self.fields['relevador'].queryset = Usuario.objects.filter(pk=each.usuario.pk)
	
	send_mail(
    'Subject here',
    'Here is the message.',
    'enjeidevelopment@gmail.com',
    ['nicolas.dibiase22@gmail.com'],
    fail_silently=False,
)
