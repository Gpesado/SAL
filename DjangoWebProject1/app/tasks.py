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

		pepe = Notificacion_alerta.objects.filter(incidente_id = incidente.pk).order_by('-pk').first()

		if pepe.incidente.alerta.periodicidad == 'd':
        
	        d = timedelta(days=pepe.incidente.alerta.frecuencia)
	        fecha = pepe.fecha_envio + d
	    
	    else:
	        h = timedelta(hours=pepe.incidente.alerta.frecuencia)
	        fecha = pepe.fecha_envio + h
	    if timezone.now() > fecha:
	    	na = Notificacion_alerta.objects.create(incidente=incidente)
			na.save()
			send_mail_relevador(incidente.relevador.email, incidente.asunto_mail_relevador, incidente.cuerpo_mail_relevador)    

		
