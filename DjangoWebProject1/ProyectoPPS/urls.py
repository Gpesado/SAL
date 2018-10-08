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
from app.views import AccountViewSet, LoginView, LogoutView
from django.views.generic import TemplateView
from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
import app.forms
import app.views
from django.contrib.auth import views as auth_views



router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^home$', app.views.home, name='home'),    
    
    #urls Usuario (CREATE/DELETE/LIST)
    url(r'^registrarUsuario$', app.views.usuario_new, name='registrarUsuario'),
    url(r'^usuario/(?P<pk>\d+)/delete/$', app.views.usuario_delete, name='usuario_delete'),
    url(r'^usuario/(?P<pk>\d+)/update/$', app.views.UsuarioUpdate.as_view(), name='usuario_update'),
    url(r'^usuarios/$', app.views.UsuarioListView.as_view(), name='usuarios'),

    url(r'^usuario/(?P<pk>\d+)$', app.views.UsuarioDetailView.as_view(), name='usuario_edit'),

    #urls Reset de Password
    url(r'^password_reset$',
        django.contrib.auth.views.password_reset,
        {
            'template_name': 'app/password_reset_form.html',

        },
        name='password_reset'),
    url(r'^password_reset/done/$', django.contrib.auth.views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    
    #Login/Logout
    url(r'^$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

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
