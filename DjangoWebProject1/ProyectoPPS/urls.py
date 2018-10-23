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


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
     path('', TemplateView.as_view(template_name='app/index.html'), name='home'),
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
    #url(r'^grupoLuminaria/(?P<pk>\d+)$', app.views.GrupoLuminariaListView.as_view(), name='grupoLuminaria_edit'),

    #urls Reset de Password


    #Login/Logout
    

    url(r'^tecnico/agregarFalla/$', app.views.agregarFalla, name='agregarFalla'),
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
    
    url(r'^tecnico/$', app.views.vistaTecnico, name='vistaTecnico'),
    url(r'^administracion/$', app.views.vistaAdministracion, name='vistaAdministracion'),
    url(r'^visualizador/$', app.views.vistaVisualizador, name='vistaVisualizador'),
]
