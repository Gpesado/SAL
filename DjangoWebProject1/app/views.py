from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from app.models import Usuario
from app.forms import RegisterUserForm
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
    return render(request, 'app/usuario_create.html', {'form': form})


def usuario_create(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
    else:
        form = RegisterUserForm()
    return save_book_form(request, form, 'app/usuario_create.html')


def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = RegisterUserForm(request.POST, instance=usuario)
    else:
        form = RegisterUserForm(instance=usuario)
    return save_book_form(request, form, 'app/usuario_update.html')


def usuario_delete(request, pk, template_name='app/usuario_confirm_delete.html'):
    usuario= get_object_or_404(Usuario, pk=pk)    
    if request.method=='POST':
        usuario.is_active=False
        usuario.save()
        return redirect('usuarios')
    return render(request, template_name, {'object':usuario})



def save_book_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            books = Usuario.objects.all()
            data['html_book_list'] = render_to_string('app/usuarios.html', {
                'usuarios': books
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
    paginate_by = 10
    queryset = Usuario.objects.all()  # Default: Model.objects.all()



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


#class LoginView(views.APIView):
#    def post(self, request, format=None):
#        username = request.data.get('username', None)

#        if Usuario.objects.filter(username=username).exists() == False:
#            return Response({
#                'status': 'Bad request',
#                'message': 'Invalid username.'
#            }, status=status.HTTP_400_BAD_REQUEST)

#        password = request.data.get('password', None)

#        Usuario = authenticate(username=username, password=password)

#        if Usuario is not None:
#            login(request, Usuario)
#            serialized = AccountSerializer(Usuario)

#            return Response(serialized.data)
#        else:
#            return Response({
#                'status': 'Unauthorized',
#                'message': 'Invalid password.'
#            }, status=status.HTTP_401_UNAUTHORIZED)

#class LogoutView(views.APIView):
#    permission_classes = (permissions.IsAuthenticated,)

#    def post(self, request, format=None):
#        logout(request)

#        return Response({}, status=status.HTTP_204_NO_CONTENT)


def index(request):
    return render(request,'app/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = BootstrapAuthenticationForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = BootstrapAuthenticationForm()
        
    return render(request,'app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'app/login.html', {})