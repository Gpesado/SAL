from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from app.models import *
from app.forms import *
from app.permissions import IsAccountOwner
from app.serializers import AccountSerializer
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import FormView, TemplateView, RedirectView, DetailView
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# VENTANA INDIVIDUALES , POSIBLEMENTE SE DEBAN ELIMINAR AL ARMAR LAS VENTANAS INTEGRADORAS...
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def agregarFalla(request):
        if request.method == "POST":
            form = agregarFallaForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaTecnico')
        else:
            form = agregarFallaForm()
        return render(request, 'app/agregarFalla.html', {'form': form})

def agregarGrupo(request):
        if request.method == "POST":
            form = agregarGrupoForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregarGrupoForm()
        return render(request, 'app/agregarGrupo.html', {'form': form})

def agregar_nodo_luminaria_led(request):
        if request.method == "POST":
            form = agregar_nodo_luminaria_ledForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregar_nodo_luminaria_ledForm()
        return render(request, 'app/agregar_nodo_luminaria_led.html', {'form': form})

def agregar_observador_grupo_led(request):
        if request.method == "POST":
            form = agregar_observador_grupo_ledForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregar_observador_grupo_ledForm()
        return render(request, 'app/agregar_observador_grupo_led.html', {'form': form})

def agregar_tecnico_grupo_led(request):
        if request.method == "POST":
            form = agregar_tecnico_grupo_ledForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregar_tecnico_grupo_ledForm()
        return render(request, 'app/agregar_tecnico_grupo_led.html', {'form': form})

def agregarOrdenReparacion(request):
        if request.method == "POST":
            form = agregarOrdenReparacionForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaTecnico')
        else:
            form = agregarOrdenReparacionForm()
        return render(request, 'app/agregarOrdenReparacion.html', {'form': form})

def observacion_Orden_Reparacion(request):
        if request.method == "POST":
            form = observacion_Orden_ReparacionForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaTecnico')
        else:
            form = observacion_Orden_ReparacionForm()
        return render(request, 'app/observacion_Orden_Reparacion.html', {'form': form})

def agregarNodo_LED(request):
        if request.method == "POST":
            form = agregarNodo_LEDForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregarNodo_LEDForm()
        return render(request, 'app/agregarNodo_LED.html', {'form': form})

def agregarLuminaria_LED(request):
        if request.method == "POST":
            form = agregarLuminaria_LEDForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregarLuminaria_LEDForm()
        return render(request, 'app/agregarNodo_LED.html', {'form': form})

def agregarModeloLED(request):
        if request.method == "POST":
            form = agregarModeloLEDForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregarModeloLEDForm()
        return render(request, 'app/agregarModeloLED.html', {'form': form})

def agregarMarcaLED(request):
        if request.method == "POST":
            form = agregarMarcaLEDForm(request.POST)
            if form.is_valid():
                falla = form.save(commit=False)
                falla.save()
                return redirect('vistaAdministracion')
        else:
            form = agregarMarcaLEDForm()
        return render(request, 'app/agregarMarcaLED.html', {'form': form})

# VENTANAS DE NAVEGACION DEPENDIENDO DEL ROL
def vistaTecnico(request):
    return render(request,'app/vistaTecnico.html')

def vistaAdministracion(request):
    return render(request,'app/vistaAdministracion.html')

def vistaVisualizador(request):
    return render(request,'app/vistaVisualizador.html')

# VENTANA GESTION DE USUARIOS
def usuario_create(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
    else:
        form = RegisterUserForm()
    return save_usuario_form(request, form, 'app/usuario_create.html')

def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=usuario)
    else:
        form = EditUserForm(instance=usuario)
    return save_usuario_form(request, form, 'app/usuario_update.html')

def usuario_delete(request, pk):
    #usuario = get_object_or_404(Usuario, pk=pk)
    usuario = Usuario.objects.get(pk=pk)
    #usuario = get_object_or_404(queryset, pk=1)
    data = dict()
    if request.method == 'POST':
        usuario.is_active=False
        usuario.save()
        data['form_is_valid'] = True
        usuarios = Usuario.objects.all()
        data['html_usuario_list'] = render_to_string('app/usuario_list.html', {
            'app': usuarios
        })
    else:
        context = {'usuario': usuario}
        data['html_form'] = render_to_string('app/usuario_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_usuario_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data.get("password")
            if password is not None:
                user.set_password(password)
            user.save()
            form.save_m2m()
            data['form_is_valid'] = True
            usuarios = Usuario.objects.all()
            data['html_usuario_list'] = render_to_string('app/usuario_list.html', {
                'app': usuarios
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class UsuarioListView(ListView):
    model = Usuario    
    context_object_name = 'usuarios'
    template_name = 'usuario_list.html'    
    queryset = Usuario.objects.all()  # Default: Model.objects.all()

class UsuarioDelete(DeleteView):
    model = Usuario
    
    success_url = reverse_lazy('usuarios')

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'app/usuario_update.html'
    
# VENTANA ROLES
def rol_create(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
    else:
        form = RolForm()
    return save_rol_form(request, form, 'app/rol_create.html')


def rol_update(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
    else:
        form = RolForm(instance=rol)
    return save_rol_form(request, form, 'app/rol_update.html')

def rol_delete(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        rol.delete()
        data['form_is_valid'] = True
        roles = Rol.objects.all()
        data['html_rol_list'] = render_to_string('app/rol_list.html', {
            'app': roles
        })
    else:
        context = {'rol': rol}
        data['html_form'] = render_to_string('app/rol_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_rol_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            roles = Rol.objects.all()
            data['html_rol_list'] = render_to_string('app/rol_list.html', {
                'app': roles
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class RolListView(ListView):
    model = Rol
    context_object_name = 'roles'
    template_name = 'rol_list.html'    
    paginate_by = 10
    queryset = Rol.objects.all()  # Default: Model.objects.all()

# VALIDACIONES DE USUARIOS
class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Usuario.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        validateData(request.data)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            Usuario.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'Usuario could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

def validateData(data):
    email = data.get('email', None)
    username = data.get('username', None)

    if Usuario.objects.filter(email=email).exists():
        return Response({
            'status': 'Unprocessable entity',
            'message': 'Found existing Usuario for email: ' + str(email)
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    if Usuario.objects.filter(username=username).exists():
        return Response({
            'status': 'Unprocessable entity',
            'message': 'Found existing Usuario with username: ' + str(username)
        }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# VENTANA GRUPO DE LUMINARIA
def grupoLuminaria_create(request):
    if request.method == 'POST':
        form = RegisterGrupoLuminariaForm(request.POST)
    else:
        form = RegisterGrupoLuminariaForm()
    return save_grupoLuminaria_form(request, form, 'app/grupo_luminaria_create.html')

def grupoLuminaria_update(request, pk):
    grupo = get_object_or_404(Grupo_Luminaria, pk=pk)
    if request.method == 'POST':
        form = RegisterGrupoLuminariaForm(request.POST, instance=grupo)
    else:
        form = RegisterGrupoLuminariaForm(instance=grupo)
    return save_grupoLuminaria_form(request, form, 'app/grupo_luminaria_update.html')

def grupoLuminaria_delete(request, pk, template_name='app/grupo_luminaria_confirm_delete.html'):
    grupo = get_object_or_404(Grupo_Luminaria, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        grupo.delete()
        data['form_is_valid'] = True
        grupos = Grupo_Luminaria.objects.all()
        data['html_grupo_list'] = render_to_string('app/grupo_luminaria_list.html', {
            'app': grupos
        })
    else:
        context = {'grupo': grupo}
        data['html_form'] = render_to_string('app/grupo_luminaria_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_grupoLuminaria_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            grupos = Grupo_Luminaria.objects.all()
            data['html_grupo_list'] = render_to_string('app/grupo_luminaria_list.html', {
                'app': grupos
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class GrupoLuminariaListView(ListView):
    model = Grupo_Luminaria    
    context_object_name = 'grupos'
    template_name = 'grupo_luminaria_list.html'    
    paginate_by = 10
    queryset = Grupo_Luminaria.objects.all()  # Default: Model.objects.all()

# VENTANA ORDENES DE REPARACION
def orden_create(request):
    if request.method == 'POST':
        form = RegisterOrdenForm(request.POST)
    else:
        form = RegisterOrdenForm()
    return save_orden_form(request, form, 'app/orden_create.html')

def orden_update(request, pk):
    orden = get_object_or_404(Orden_Reparacion, pk=pk)
    if request.method == 'POST':
        form = RegisterOrdenForm(request.POST, instance=orden)
    else:
        form = RegisterOrdenForm(instance=orden)
    return save_orden_form(request, form, 'app/orden_update.html')

def orden_delete(request, pk, template_name='app/orden_confirm_delete.html'):
    orden = get_object_or_404(Orden_Reparacion, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        orden.delete()
        data['form_is_valid'] = True
        ordenes = Orden_Reparacion.objects.all()
        data['html_orden_list'] = render_to_string('app/orden_list.html', {
            'app': ordenes
        })
    else:
        context = {'orden': orden}
        data['html_form'] = render_to_string('app/orden_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_orden_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            ordenes = Orden_Reparacion.objects.all()
            data['html_orden_list'] = render_to_string('app/orden_list.html', {
                'app': ordenes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

#TODO: PORQUE SI LO TENGO COMO orden_list en el archivo html no me lo toma? ademas esto me afecta a mis redirreciones  
class OrdenListView(ListView):
    model = Orden_Reparacion    
    context_object_name = 'ordenes'
    template_name = 'orden_list.html'    
    paginate_by = 10
    queryset = Orden_Reparacion.objects.all()  # Default: Model.objects.all()

# VENTANA FABRICANTE
def fabricante_create(request):
    if request.method == 'POST':
        form = RegisterFabricanteForm(request.POST)
    else:
        form = RegisterFabricanteForm()
    return save_fabricante_form(request, form, 'app/fabricante_create.html')

def fabricante_update(request, pk):
    fabricante = get_object_or_404(Fabricante, pk=pk)
    if request.method == 'POST':
        form = RegisterFabricanteForm(request.POST, instance=fabricante)
    else:
        form = RegisterFabricanteForm(instance=fabricante)
    return save_fabricante_form(request, form, 'app/fabricante_update.html')

def fabricante_delete(request, pk, template_name='app/fabricante_confirm_delete.html'):
    fabricante = get_object_or_404(Fabricante, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        fabricante.delete()
        data['form_is_valid'] = True
        fabricantes = Fabricante.objects.all()
        data['html_fabricante_list'] = render_to_string('app/fabricante_list.html', {
            'app': fabricantes
        })
    else:
        context = {'fabricante': fabricante}
        data['html_form'] = render_to_string('app/fabricante_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_fabricante_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            fabricantes = Fabricante.objects.all()
            data['html_fabricante_list'] = render_to_string('app/fabricante_list.html', {
                'app': fabricantes
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class fabricanteListView(ListView):
    model = Fabricante    
    context_object_name = 'fabricantes'
    template_name = 'fabricante_list.html'    
    paginate_by = 10
    queryset = Fabricante.objects.all()  # Default: Model.objects.all()

# VENTANA LUMINARIALED
def luminarialed_create(request):
    if request.method == 'POST':
        form = RegisterLuminarialedForm(request.POST)
    else:
        form = RegisterLuminarialedForm()
    return save_luminarialed_form(request, form, 'app/luminarialed_create.html')

def luminarialed_update(request, pk):
    luminarialed = get_object_or_404(Luminaria_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterLuminarialedForm(request.POST, instance=luminarialed)
    else:
        form = RegisterLuminarialedForm(instance=luminarialed)
    return save_luminarialed_form(request, form, 'app/luminarialed_update.html')

def luminarialed_delete(request, pk, template_name='app/luminarialed_confirm_delete.html'):
    luminarialed = get_object_or_404(Luminaria_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        luminarialed.delete()
        data['form_is_valid'] = True
        luminarialeds = Luminaria_LED.objects.all()
        data['html_luminarialed_list'] = render_to_string('app/luminarialed_list.html', {
            'app': luminarialeds
        })
    else:
        context = {'luminarialed': luminarialed}
        data['html_form'] = render_to_string('app/luminarialed_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_luminarialed_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            luminarialeds = Luminaria_LED.objects.all()
            data['html_luminarialed_list'] = render_to_string('app/luminarialed_list.html', {
                'app': luminarialeds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class luminarialedListView(ListView):
    model = Luminaria_LED    
    context_object_name = 'luminarialeds'
    template_name = 'luminarialed_list.html'    
    paginate_by = 10
    queryset = Luminaria_LED.objects.all()  # Default: Model.objects.all()

# VENTANA LUMINARIA NO LED
def luminarianoled_create(request):
    if request.method == 'POST':
        form = RegisterLuminarianoledForm(request.POST)
    else:
        form = RegisterLuminarianoledForm()
    return save_luminarianoled_form(request, form, 'app/luminarianoled_create.html')

def luminarianoled_update(request, pk):
    luminarianoled = get_object_or_404(Lampara_No_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterLuminarianoledForm(request.POST, instance=luminarianoled)
    else:
        form = RegisterLuminarianoledForm(instance=luminarianoled)
    return save_luminarianoled_form(request, form, 'app/luminarianoled_update.html')

def luminarianoled_delete(request, pk, template_name='app/luminarianoled_confirm_delete.html'):
    luminarianoled = get_object_or_404(Lampara_No_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        luminarianoled.delete()
        data['form_is_valid'] = True
        luminarianoleds = Lampara_No_LED.objects.all()
        data['html_luminarianoled_list'] = render_to_string('app/luminarianoled_list.html', {
            'app': luminarianoleds
        })
    else:
        context = {'luminarianoled': luminarianoled}
        data['html_form'] = render_to_string('app/luminarianoled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_luminarianoled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            luminarianoleds = Lampara_No_LED.objects.all()
            data['html_luminarianoled_list'] = render_to_string('app/luminarianoled_list.html', {
                'app': luminarianoleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class luminarianoledListView(ListView):
    model = Lampara_No_LED    
    context_object_name = 'luminarianoleds'
    template_name = 'luminarianoled_list.html'    
    paginate_by = 10
    queryset = Lampara_No_LED.objects.all()  # Default: Model.objects.all()

# MARCALED
def marcaled_create(request):
    if request.method == 'POST':
        form = RegisterMarcaledForm(request.POST)
    else:
        form = RegisterMarcaledForm()
    return save_marcaled_form(request, form, 'app/marcaled_create.html')

def marcaled_update(request, pk):
    marcaled = get_object_or_404(Marca_Luminaria_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterMarcaledForm(request.POST, instance=marcaled)
    else:
        form = RegisterMarcaledForm(instance=marcaled)
    return save_marcaled_form(request, form, 'app/marcaled_update.html')

def marcaled_delete(request, pk, template_name='app/marcaled_confirm_delete.html'):
    marcaled = get_object_or_404(Marca_Luminaria_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        marcaled.delete()
        data['form_is_valid'] = True
        marcaleds = Marca_Luminaria_LED.objects.all()
        data['html_marcaled_list'] = render_to_string('app/marcaled_list.html', {
            'app': marcaleds
        })
    else:
        context = {'marcaled': marcaled}
        data['html_form'] = render_to_string('app/marcaled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_marcaled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            marcaleds = Marca_Luminaria_LED.objects.all()
            data['html_marcaled_list'] = render_to_string('app/marcaled_list.html', {
                'app': marcaleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class marcaledListView(ListView):
    model = Marca_Luminaria_LED    
    context_object_name = 'marcaleds'
    template_name = 'marcaled_list.html'    
    paginate_by = 10
    queryset = Marca_Luminaria_LED.objects.all()  # Default: Model.objects.all()

# MARCA NO LED
def marcanoled_create(request):
    if request.method == 'POST':
        form = RegisterMarcanoledForm(request.POST)
    else:
        form = RegisterMarcanoledForm()
    return save_marcanoled_form(request, form, 'app/marcanoled_create.html')

def marcanoled_update(request, pk):
    marcanoled = get_object_or_404(Marca_Luminaria_NO_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterMarcanoledForm(request.POST, instance=marcanoled)
    else:
        form = RegisterMarcanoledForm(instance=marcanoled)
    return save_marcanoled_form(request, form, 'app/marcanoled_update.html')

def marcanoled_delete(request, pk, template_name='app/marcanoled_confirm_delete.html'):
    marcanoled = get_object_or_404(Marca_Luminaria_NO_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        marcanoled.delete()
        data['form_is_valid'] = True
        marcanoleds = Marca_Luminaria_NO_LED.objects.all()
        data['html_marcanoled_list'] = render_to_string('app/marcanoled_list.html', {
            'app': marcanoleds
        })
    else:
        context = {'marcanoled': marcanoled}
        data['html_form'] = render_to_string('app/marcanoled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_marcanoled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            marcanoleds = Marca_Luminaria_NO_LED.objects.all()
            data['html_marcanoled_list'] = render_to_string('app/marcanoled_list.html', {
                'app': marcanoleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class marcanoledListView(ListView):
    model = Marca_Luminaria_NO_LED    
    context_object_name = 'marcanoleds'
    template_name = 'marcanoled_list.html'    
    paginate_by = 10
    queryset = Marca_Luminaria_NO_LED.objects.all()  # Default: Model.objects.all()

# MODELO LED
def modeloled_create(request):
    if request.method == 'POST':
        form = RegisterModeloledForm(request.POST)
    else:
        form = RegisterModeloledForm()
    return save_modeloled_form(request, form, 'app/modeloleds_create.html')

def modeloled_update(request, pk):
    modeloled = get_object_or_404(Modelo_Luminaria_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterModeloledForm(request.POST, instance=modeloled)
    else:
        form = RegisterModeloledForm(instance=modeloled)
    return save_modeloled_form(request, form, 'app/modeloled_update.html')

def modeloled_delete(request, pk, template_name='app/modeloled_confirm_delete.html'):
    modeloled = get_object_or_404(Modelo_Luminaria_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        modeloled.delete()
        data['form_is_valid'] = True
        modeloleds = Modelo_Luminaria_LED.objects.all()
        data['html_modeloled_list'] = render_to_string('app/modeloled_list.html', {
            'app': modeloleds
        })
    else:
        context = {'modeloled': modeloled}
        data['html_form'] = render_to_string('app/modeloled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_modeloled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            modeloleds = Modelo_Luminaria_LED.objects.all()
            data['html_modeloled_list'] = render_to_string('app/modeloled_list.html', {
                'app': modeloleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class modeloledListView(ListView):
    model = Modelo_Luminaria_LED    
    context_object_name = 'modeloleds'
    template_name = 'modeloled_list.html'    
    paginate_by = 10
    queryset = Modelo_Luminaria_LED.objects.all()  # Default: Model.objects.all()

# MODELO NO LED
def modelonoled_create(request):
    if request.method == 'POST':
        form = RegisterModelonoledForm(request.POST)
    else:
        form = RegisterModelonoledForm()
    return save_modelonoled_form(request, form, 'app/modelonoled_create.html')

def modelonoled_update(request, pk):
    modelonoled = get_object_or_404(Modelo_Luminaria_NO_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterModelonoledForm(request.POST, instance=modelonoled)
    else:
        form = RegisterModelonoledForm(instance=modelonoled)
    return save_modelonoled_form(request, form, 'app/modelonoled_update.html')

def modelonoled_delete(request, pk, template_name='app/modelonoled_confirm_delete.html'):
    modelonoled = get_object_or_404(Modelo_Luminaria_NO_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        modelonoled.delete()
        data['form_is_valid'] = True
        modelonoleds = Modelo_Luminaria_NO_LED.objects.all()
        data['html_modelonoled_list'] = render_to_string('app/modelonoled_list.html', {
            'app': modelonoleds
        })
    else:
        context = {'modelonoled': modelonoled}
        data['html_form'] = render_to_string('app/modelonoled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_modelonoled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            modelonoleds = Modelo_Luminaria_NO_LED.objects.all()
            data['html_modelonoled_list'] = render_to_string('app/modelonoled_list.html', {
                'app': modelonoleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class modelonoledListView(ListView):
    model = Modelo_Luminaria_NO_LED    
    context_object_name = 'modelonoleds'
    template_name = 'modelonoled_list.html'    
    paginate_by = 10
    queryset = Modelo_Luminaria_NO_LED.objects.all()  # Default: Model.objects.all()

# NODO LED
def nodoled_create(request):
    if request.method == 'POST':
        form = RegisterNodoledForm(request.POST)
    else:
        form = RegisterNodoledForm()
    return save_nodoled_form(request, form, 'app/nodoled_create.html')

def nodoled_update(request, pk):
    nodoled = get_object_or_404(Nodo_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterNodoledForm(request.POST, instance=nodoled)
    else:
        form = RegisterNodoledForm(instance=nodoled)
    return save_nodoled_form(request, form, 'app/nodoled_update.html')

def nodoled_delete(request, pk, template_name='app/nodoled_confirm_delete.html'):
    nodoled = get_object_or_404(Nodo_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        nodoled.delete()
        data['form_is_valid'] = True
        nodoleds = Nodo_LED.objects.all()
        data['html_nodoled_list'] = render_to_string('app/nodoled_list.html', {
            'app': nodoleds
        })
    else:
        context = {'nodoled': nodoled}
        data['html_form'] = render_to_string('app/nodoled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_nodoled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            nodoleds = Nodo_LED.objects.all()
            data['html_nodoled_list'] = render_to_string('app/nodoled_list.html', {
                'app': nodoleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class nodoledListView(ListView):
    model = Nodo_LED    
    context_object_name = 'nodoleds'
    template_name = 'nodoled_list.html'    
    paginate_by = 10
    queryset = Nodo_LED.objects.all()  # Default: Model.objects.all()

# NODO NO LED
def nodonoled_create(request):
    if request.method == 'POST':
        form = RegisterNodonoledForm(request.POST)
    else:
        form = RegisterNodonoledForm()
    return save_nodonoled_form(request, form, 'app/nodonoled_create.html')

def nodonoled_update(request, pk):
    nodonoled = get_object_or_404(Nodo_NO_LED, pk=pk)
    if request.method == 'POST':
        form = RegisterNodonoledForm(request.POST, instance=nodonoled)
    else:
        form = RegisterNodonoledForm(instance=nodonoled)
    return save_nodonoled_form(request, form, 'app/nodonoled_update.html')

def nodonoled_delete(request, pk, template_name='app/nodonoled_confirm_delete.html'):
    nodonoled = get_object_or_404(Nodo_NO_LED, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        nodonoled.delete()
        data['form_is_valid'] = True
        nodonoleds = Nodo_NO_LED.objects.all()
        data['html_nodonoled_list'] = render_to_string('app/nodonoled_list.html', {
            'app': nodonoleds
        })
    else:
        context = {'nodonoled': nodonoled}
        data['html_form'] = render_to_string('app/nodonoled_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_nodonoled_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            nodonoleds = Nodo_NO_LED.objects.all()
            data['html_nodonoled_list'] = render_to_string('app/nodonoled_list.html', {
                'app': nodonoleds
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class nodonoledListView(ListView):
    model = Nodo_NO_LED    
    context_object_name = 'nodonoleds'
    template_name = 'nodonoled_list.html'    
    paginate_by = 10
    queryset = Nodo_NO_LED.objects.all()  # Default: Model.objects.all()


# BALASTROS
def balastro_create(request):
    if request.method == 'POST':
        form = RegisterBalastroForm(request.POST)
    else:
        form = RegisterBalastroForm()
    return save_nodonoled_form(request, form, 'app/balastro_create.html')

def balastro_update(request, pk):
    balastro = get_object_or_404(Balastro, pk=pk)
    if request.method == 'POST':
        form = RegisterBalastroForm(request.POST, instance=balastro)
    else:
        form = RegisterBalastroForm(instance=balastro)
    return save_balastro_form(request, form, 'app/balastro_update.html')

def balastro_delete(request, pk, template_name='app/balastro_confirm_delete.html'):
    balastro = get_object_or_404(Balastro, pk=pk)
    data = dict()
    if request.method == 'POST':
        
        balastro.delete()
        data['form_is_valid'] = True
        balastros = Balastro.objects.all()
        data['html_balastro_list'] = render_to_string('app/balastro_list.html', {
            'app': balastros
        })
    else:
        context = {'balastro': balastro}
        data['html_form'] = render_to_string('app/balastro_confirm_delete.html', context, request=request)
    return JsonResponse(data)

def save_balastro_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            balastros = Balastro.objects.all()
            data['html_balastro_list'] = render_to_string('app/balastro_list.html', {
                'app': balastros
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

class balastroListView(ListView):
    model = Balastro    
    context_object_name = 'balastros'
    template_name = 'balastro_list.html'    
    paginate_by = 10
    queryset = Balastro.objects.all()  # Default: Model.objects.all()