"""django-angular URL Configuration
The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from rest_framework_nested import routers
from django.conf.urls import url, include
from django.contrib import admin
from app.views import AccountViewSet
from django.views.generic import TemplateView
from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import views as auth_views

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)

task_pattern = r'(?P<task_id>[\w\d\-\.]+)'

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', app.views.home, name='home'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    
    #urls Usuario (CREATE/DELETE/LIST)
    url(r'^usuario/create$', app.views.usuario_create, name='usuario_create'),
    url(r'^usuario/(?P<pk>\d+)/delete/$', app.views.usuario_delete, name='usuario_delete'),
    url(r'^usuario/(?P<pk>\d+)/update/$', app.views.usuario_update, name='usuario_update'),
    url(r'^usuarios/$', app.views.UsuarioListView.as_view(), name='usuarios'),
    url(r'^usuario/(?P<pk>\d+)$', app.views.UsuarioDetailView.as_view(), name='usuario_edit'),

    #urls Rol
    url(r'^rol/create$', app.views.rol_create, name='rol_create'),
    url(r'^rol/(?P<pk>\d+)/delete/$', app.views.rol_delete, name='rol_delete'),
    url(r'^rol/(?P<pk>\d+)/update/$', app.views.rol_update, name='rol_update'),
    url(r'^roles/$', app.views.RolListView.as_view(), name='roles'),
    
    #urls grupoLuminarias (CREATE/DELETE/LIST)
    url(r'^grupoLuminaria/create$', app.views.grupoLuminaria_create, name='grupoLuminaria_create'),
    url(r'^grupoLuminaria/(?P<pk>\d+)/delete/$', app.views.grupoLuminaria_delete, name='grupoLuminaria_delete'),
    url(r'^grupoLuminaria/(?P<pk>\d+)/update/$', app.views.grupoLuminaria_update, name='grupoLuminaria_update'),
    url(r'^grupoLuminaria$', app.views.GrupoLuminariaListView.as_view(), name='grupoLuminarias'),
    
    #urls Ordenes de reparacion
    url(r'^ordenes/create$', app.views.orden_create, name='orden_create'),
    url(r'^ordenes/(?P<pk>\d+)/delete/$', app.views.orden_delete, name='orden_delete'),
    url(r'^ordenes/(?P<pk>\d+)/update/$', app.views.orden_update, name='orden_update'),
    url(r'^ordenes$', app.views.OrdenListView.as_view(), name='ordenes'),
    
      #urls fabricante (CREATE/DELETE/LIST)
    url(r'^tecnico/fabricante/create$', app.views.fabricante_create, name='fabricante_create'),
    url(r'^tecnico/fabricante/(?P<pk>\d+)/delete/$', app.views.fabricante_delete, name='fabricante_delete'),
    url(r'^tecnico/fabricante/(?P<pk>\d+)/update/$', app.views.fabricante_update, name='fabricante_update'),
    url(r'^tecnico/fabricante$', app.views.fabricanteListView.as_view(), name='fabricante'),
    
      #urls luminarialed (CREATE/DELETE/LIST)
    url(r'^tecnico/luminarialed/create$', app.views.luminarialed_create, name='luminarialed_create'),
    url(r'^tecnico/luminarialed/(?P<pk>\d+)/delete/$', app.views.luminarialed_delete, name='luminarialed_delete'),
    url(r'^tecnico/luminarialed/(?P<pk>\d+)/update/$', app.views.luminarialed_update, name='luminarialed_update'),
    url(r'^tecnico/luminarialed$', app.views.luminarialedListView.as_view(), name='luminarialed'),
      
      #urls luminarianoled (CREATE/DELETE/LIST)
    url(r'^tecnico/luminarianoled/create$', app.views.luminarianoled_create, name='luminarianoled_create'),
    url(r'^tecnico/luminarianoled/(?P<pk>\d+)/delete/$', app.views.luminarianoled_delete, name='luminarianoled_delete'),
    url(r'^tecnico/luminarianoled/(?P<pk>\d+)/update/$', app.views.luminarianoled_update, name='luminarianoled_update'),
    url(r'^tecnico/luminarianoled$', app.views.luminarianoledListView.as_view(), name='luminarianoled'),
      
      #urls marcaled (CREATE/DELETE/LIST)
    url(r'^tecnico/marcaled/create$', app.views.marcaled_create, name='marcaled_create'),
    url(r'^tecnico/marcaled/(?P<pk>\d+)/delete/$', app.views.marcaled_delete, name='marcaled_delete'),
    url(r'^tecnico/marcaled/(?P<pk>\d+)/update/$', app.views.marcaled_update, name='marcaled_update'),
    url(r'^tecnico/marcaled$', app.views.marcaledListView.as_view(), name='marcaled'),
    
      #urls marcanoled (CREATE/DELETE/LIST)
    url(r'^tecnico/marcanoled/create$', app.views.marcanoled_create, name='marcanoled_create'),
    url(r'^tecnico/marcanoled/(?P<pk>\d+)/delete/$', app.views.marcanoled_delete, name='marcanoled_delete'),
    url(r'^tecnico/marcanoled/(?P<pk>\d+)/update/$', app.views.marcanoled_update, name='marcanoled_update'),
    url(r'^tecnico/marcanoled$', app.views.marcanoledListView.as_view(), name='marcanoled'),
      
      #urls modeloled (CREATE/DELETE/LIST)
    url(r'^tecnico/modeloled/create$', app.views.modeloled_create, name='modeloled_create'),
    url(r'^tecnico/modeloled/(?P<pk>\d+)/delete/$', app.views.modeloled_delete, name='modeloled_delete'),
    url(r'^tecnico/modeloled/(?P<pk>\d+)/update/$', app.views.modeloled_update, name='modeloled_update'),
    url(r'^tecnico/modeloled$', app.views.modeloledListView.as_view(), name='modeloled'),
      
      #urls modelonoled (CREATE/DELETE/LIST)
    url(r'^tecnico/modelonoled/create$', app.views.modelonoled_create, name='modelonoled_create'),
    url(r'^tecnico/modelonoled/(?P<pk>\d+)/delete/$', app.views.modelonoled_delete, name='modelonoled_delete'),
    url(r'^tecnico/modelonoled/(?P<pk>\d+)/update/$', app.views.modelonoled_update, name='modelonoled_update'),
    url(r'^tecnico/modelonoled$', app.views.modelonoledListView.as_view(), name='modelonoled'),

        #urls nodoled (CREATE/DELETE/LIST)
    url(r'^tecnico/nodoled/create$', app.views.nodoled_create, name='nodoled_create'),
    url(r'^tecnico/nodoled/(?P<pk>\d+)/delete/$', app.views.nodoled_delete, name='nodoled_delete'),
    url(r'^tecnico/nodoled/(?P<pk>\d+)/update/$', app.views.nodoled_update, name='nodoled_update'),
    url(r'^tecnico/nodoled$', app.views.nodoledListView.as_view(), name='nodoled'),
    
      #urls nodonoled (CREATE/DELETE/LIST)
    url(r'^tecnico/nodonoled/create$', app.views.nodonoled_create, name='nodonoled_create'),
    url(r'^tecnico/nodonoled/(?P<pk>\d+)/delete/$', app.views.nodonoled_delete, name='nodonoled_delete'),
    url(r'^tecnico/nodonoled/(?P<pk>\d+)/update/$', app.views.nodonoled_update, name='nodonoled_update'),
    url(r'^tecnico/nodonoled$', app.views.nodonoledListView.as_view(), name='nodonoled'),
      
      #urls balastro (CREATE/DELETE/LIST)
    url(r'^tecnico/balastro/create$', app.views.balastro_create, name='balastro_create'),
    url(r'^tecnico/balastro/(?P<pk>\d+)/delete/$', app.views.balastro_delete, name='balastro_delete'),
    url(r'^tecnico/balastro/(?P<pk>\d+)/update/$', app.views.balastro_update, name='balastro_update'),
    url(r'^tecnico/balastro$', app.views.balastroListView.as_view(), name='balastro'),

      #urls balastro (CREATE/DELETE/LIST)
    url(r'^tecnico/alerta/create$', app.views.alerta_create, name='alerta_create'),
    url(r'^tecnico/alerta/(?P<pk>\d+)/delete/$', app.views.alerta_delete, name='alerta_delete'),
    url(r'^tecnico/alerta/(?P<pk>\d+)/update/$', app.views.alerta_update, name='alerta_update'),
    url(r'^tecnico/alerta$', app.views.alertaListView.as_view(), name='alerta'),

      #urls Incidentes (CREATE/DELETE/LIST)
    url(r'^tecnico/incidente/create$', app.views.incidente_create, name='incidente_create'),
    url(r'^tecnico/incidente/(?P<pk>\d+)/delete/$', app.views.incidente_delete, name='incidente_delete'),
    url(r'^tecnico/incidente/(?P<pk>\d+)/update/$', app.views.incidente_update, name='incidente_update'),
    url(r'^tecnico/incidente$', app.views.incidenteListView.as_view(), name='incidente'),
	url(r'^tecnico/incidentes_reparador$', app.views.incidentes_reparador, name='incidentes_reparador'),
    url(r'^tecnico/incidente_reparador$', app.views.agregarIncidenteReparador, name='incidente_reparador'),
    path('ajax/load_luminarias/', app.views.load_luminarias, name='ajax_load_luminarias'),  # <-- this one here

    #urls Reset de Password
    #Login/Logout
    url(r'^tecnico/agregarFalla/$', app.views.agregarFalla, name='agregarFalla'),
    url(r'^tecnico/falla/create$', app.views.falla_create, name='falla_create'),
    url(r'^tecnico/agregarOrdenReparacion/$', app.views.agregarOrdenReparacion, name='agregarOrdenReparacion'),
    url(r'^tecnico/agregarObservacion/$', app.views.observacion_Orden_Reparacion, name='observacion_Orden_Reparacion'),
    url(r'^administracion/agregarGrupo/$', app.views.agregarGrupo, name='agregarGrupo'),
    url(r'^administracion/agregar_nodo_luminaria_led/$', app.views.agregar_nodo_luminaria_led, name='agregar_nodo_luminaria_led'),
    url(r'^administracion/agregar_observador_grupo_led/$', app.views.agregar_observador_grupo_led, name='agregar_observador_grupo_led'),
    url(r'^administracion/agregar_tecnico_grupo_led/$', app.views.agregar_tecnico_grupo_led, name='agregar_tecnico_grupo_led'),
    url(r'^administracion/agregarNodo_LED/$', app.views.agregarNodo_LED, name='agregarNodo_LED'),
    url(r'^administracion/agregarLuminaria_LED/$', app.views.agregarLuminaria_LED, name='agregarLuminaria_LED'),
    url(r'^administracion/agregarModeloLED/$', app.views.agregarModeloLED, name='agregarModeloLED'),
    url(r'^administracion/agregarMarcaLED/$', app.views.agregarMarcaLED, name='agregarMarcaLED'),
    
    url(r'^tecnico/configuracion_luminaria/create$', app.views.configuracion_luminaria_create, name='configuracion_luminaria_create'),
    url(r'^tecnico/configuracion_luminaria/(?P<pk>\d+)/delete/$', app.views.configuracion_luminaria_delete, name='configuracion_luminaria_delete'),
    url(r'^tecnico/configuracion_luminaria/(?P<pk>\d+)/update/$', app.views.configuracion_luminaria_update, name='configuracion_luminaria_update'),
    url(r'^tecnico/configuracion_luminaria$', app.views.configuracion_luminariaListView.as_view(), name='configuracion_luminaria'),


    url(r'^tecnico$', app.views.vistaTecnico, name='vistaTecnico'),
    url(r'^base$', app.views.base, name='base'),
    url(r'^administracion$', app.views.vistaAdministracion, name='vistaAdministracion'),
    url(r'^visualizador$', app.views.vistaVisualizador, name='vistaVisualizador'),

    #urls Mapas (CREATE/DELETE/LIST)
    url(r'^visualizador/mapa_luminarias$', app.views.mapaView.as_view(), name='mapa_luminarias'),
    url(r'^visualizador/buscarMarcador$', app.views.mapView.as_view(), name='buscarMarcador'),
   #
	
] 