# SAL
Programa para la materia PPS de la Universidad nacional de general sarmiento.

# REQUERIMENTS
## DJANGO >2.0
## python (version > 3.5)
## django  (version > 2.0)
## widget_tweaks
## django_celery_beat
## celerybeat_status
## LIBRERÍAS:
### queryset_sequence
### datetime
### eventlet

# Instalación

Para instalar cada requerimiento se podrá utilizar la herramienta pip de python
py pip install "INGRESAR EL REQUERIMIENTO SIN LAS COMILLAS"

# Para instanciar la BD se podra utilizar el mismo manage.py de django del modo de:
## Pararse sobre la carpeta raíz del proyecto, donde se pueda ubicar el archivo manage.py

## Para crear el esquema de la migración, así el sistema puede saber que deberá crear en el migrations.
py manage.py makemigrations

## Para crear aplicar la migración y así crear la BD 
py manage.py migrate

## Crear un superusuario para crear el primer administrador del sistema con el. 
py manage.py createsuperuser
Seguir las instrucciones que detalla el programa para su creación.
PD: Evitar este paso si ya se posee el superusuario del sistema.

## Para correr el programa (correrá en localhost:8080 por defecto). 
py manage.py runserver

## Ingresar a localhost:8080/admin/ con las credenciales del superusuario para modificar directamente la BD. Desde aqui se podria crear los primeros usuarios del sistema para luego registrarlos mediante el uso de la página web.

## Se podrá navegar a las siguientes URLS:
localhost:8080/técnico -> gestión de luminarias
localhost:8080/administracion -> gestión de usuarios y luminarias
localhost:8080/visualizador -> ver los mapas de luminarias
localhost:8080/ -> acá se verán las notificaciones

Ante cada cambio efectuado en el models.py, se deberá volver a realizar todos los pasos para que el cambio impacte en la BD.

Listo! ya tiene el sistema en funcionamiento, para ver como realizar 
cambios en el proyecto por favor abra el documento estructura.txt

PD: Para mas informacion por favor visitar https://tutorial.djangogirls.org/es/django_installation/
Esta página fue nuestra guia en nuestros primeros pasos en la creación del sistema!

# Correr proceso background:

## Ejecutar el siguiente comando para empezar a recibir los eventos:

celery -A ProyectoPPS beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

## Ejecutar el siguiente comando en una nueva consola para empezar a ejecutar las tareas:

celery -A ProyectoPPS worker -l info -P eventlet


# Estructura

La estructura del sistema es así:
DjangoWebProject1
	└───app
    		└───static
    	  		└───app
    	  			└───scripts
    	  	    			└───books.js -> JS PARA VENTANAS MODALES
  			└───templates
    	  			└───app -> HTMLS DE LAS VISTAS
    		└───forms.py -> TODOS LOS FORMULARIOS DEL SISTEMA VAN ACA
    		└───views.py -> ACA SE REGISTRAN LAS VISTAS (HTML con URL)
    		└───models.py -> ACA SE ESPECIFICA COMO ES LA BD
	└───ProyectoPPS
    		└───urls.py -> ACA SE RELACIONAN LAS FUNCIONES DE VIEWS CON   LA
                           URL DEL NAVEGADOR
    		└───settings.py -> ACA SE DEBEN REGISTRAR NUEVAS LIBRERIAS QUE AGREGEN
└───manage.py -> NO SE DEBERIA TOCAR ESTE ARCHIVO, PERO ES EL PUNTO DE ENTRADA DE LA APLICACIÓN.

## EL ESQUEMA BÁSICO PARA AGREGAR UNA VISTA SERÍA:
### SI LA NUEVA VISTA NECESITA AGREGAR ELEMENTOS AL MODELS SE DEBERÁ PRIMERO MODIFICAR EL MISMO.
#### EN CASO DE HABER MODIFICADO EL MODELS: CORRER makemigrations Y migrate para que los cambios se agreguen en la BD.
### AGREGAR EL ARCHIVO HTML EN templates/app/
###PARA PODER UTILIZARLO SE DEBERÁ AGREGAR LA LÓGICA DE LA VENTANA EN views.py.
###AHORA PARA REGISTRAR DICHA LÓGICA AL SISTEMA SE DEBERA AGREGAR ESE METODO DE views.py EN urls.py, INDICANDO QUE DIRECCION DEL NAVEGADOR CORRESPONDERÁ A DICHO MÉTODO IMPLEMENTADO (Y CONSECUENTEMENTE DICHO HTML).
PD: ANTE DUDAS EN ESTOS PUNTOS, POR FAVOR RECURRIR AL TUTORIAL CON EL CUAL NOS GUIAMOS EN https://tutorial.djangogirls.org/es/

## REGISTRO DE CLAVES:
Para el registro de claves/token de acceso para la aplicación deberán:
### REGISTRO DE GOOGLE MAPS API JS:
### Crear clave para utilizar el mapa como se describe en la documentación oficial de Google Maps. Link: https://developers.google.com/maps/documentation/javascript/get-api-key#get-an-api-key
### Registrar la clave en los archivos HTML en app/templates/app/.
#### add_marcador_led.html
#### add_marcador_no_led.html
#### marcador_grupo_luminaria_list.html

Exactamente en la parte que dice:
<script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=INGRESATUCLAVEAQUI&libraries=places"></script>

## REGISTRO DE EMAIL:
### Crear una cuenta de mail.
### Agregar servidor de mail, mail y contraseña en el archivo settings.py:
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ejemplo@gmail.com'
EMAIL_HOST_PASSWORD = 'ejemplo'

# DESARROLLADORES:
## Di Biase, Nicolas
### Contacto: nicolas.dibiase22@gmail.com
## Pesado, Gonzalo
### Contacto: gonzapesa@gmail.com
