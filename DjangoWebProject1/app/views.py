from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from app.models import Usuario
from app.forms import RegisterUserForm
from app.permissions import IsAccountOwner
from app.serializers import AccountSerializer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import *
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

def vistaTecnico(request):
    return render(request,'app/vistaTecnico.html')

def vistaAdministracion(request):
    return render(request,'app/vistaAdministracion.html')

def vistaVisualizador(request):
    return render(request,'app/vistaVisualizador.html')

def usuario_new(request):
    if request.method == "POST":
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                usuario = form.save(commit=False)
                
                usuario.save()
                return redirect('usuario_update', pk=usuario.pk)
    else:
        form = RegisterUserForm()
    return render(request, 'app/registrar_usuario.html', {'form': form})

def usuario_edit(request, pk):
        usuario = get_object_or_404(Usuario, pk=pk)
        if request.method == "POST":
            form = UsuarioForm(request.POST, instance=post)
            if form.is_valid():
                usuario = form.save(commit=False)
                usuario.save()
                return redirect('usuario_edit', pk=usuario.pk)
        else:
            form = UsuarioForm(instance=post)
        return render(request, 'app/usuario_edit.html', {'form': form})

def usuario_delete(request, pk, template_name='app/usuario_confirm_delete.html'):
    usuario= get_object_or_404(Usuario, pk=pk)    
    if request.method=='POST':
        usuario.is_active=False
        usuario.save()
        return redirect('usuarios')
    return render(request, template_name, {'object':usuario})

def usuario_detail_view(request,pk):
    try:
        book_id=Usuario.objects.get(pk=pk)
    except Usuario.DoesNotExist:
        raise Http404("Usuario no existe")

    #book_id=get_object_or_404(Book, pk=pk)
    
    return render(
        request,
        'app/Usuario_edit.html',
        context={'book':book_id,}
    )


class UsuarioListView(ListView):
    model = Usuario
    #context_object_name = 'usuario_list'
    #queryset = Usuario.objects.filter(is_active=True)
    context_object_name = 'usuarios'
    def get_context_data(self, *args, **kwargs):
        context = super(UsuarioListView, self).get_context_data(*args, **kwargs)

        context['is_active'] = Usuario.objects.filter(is_active=True)
        context['not_is_active'] = Usuario.objects.filter(is_active=False)

        return context
    #template_name = 'app/usuario_detail.html'

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('usuarios')

class UsuarioDelete(DeleteView):
    model = Usuario
    
    success_url = reverse_lazy('usuarios')

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'app/usuario_edit.html'
    

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


class LoginView(views.APIView):
    def post(self, request, format=None):
        username = request.data.get('username', None)

        if Usuario.objects.filter(username=username).exists() == False:
            return Response({
                'status': 'Bad request',
                'message': 'Invalid username.'
            }, status=status.HTTP_400_BAD_REQUEST)

        password = request.data.get('password', None)

        Usuario = authenticate(username=username, password=password)

        if Usuario is not None:
            login(request, Usuario)
            serialized = AccountSerializer(Usuario)

            return Response(serialized.data)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Invalid password.'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)

        return Response({}, status=status.HTTP_204_NO_CONTENT)


