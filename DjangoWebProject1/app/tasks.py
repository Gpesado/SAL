from celery import task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from app.models import *

logger = get_task_logger(__name__)


def send_mail_relevador(x, y, z):
    send_mail(
    y,
    z,
    'enjeidevelopment@gmail.com',
    [x],
    fail_silently=False,
)

@task()
def add(x, y):
	

	incidentes = Incidente.objects.exclude(estado='a')

	for incidente in incidentes:
		#incidente = Incidente.objects.get(pk=each.pk)
		na = Notificacion_alerta.objects.create(alerta=incidente.alerta, destinatario=incidente.relevador)
		na.save()
		send_mail_relevador(incidente.relevador.email, incidente.asunto_mail_relevador, incidente.cuerpo_mail_relevador)
