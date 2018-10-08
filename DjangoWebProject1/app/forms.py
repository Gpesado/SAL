"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *

class agregarFallaForm(forms.ModelForm):

        class Meta:
            model = Falla
            fields = ('nombre', 'descripcion','grado_criticidad') 

class agregarGrupoForm(forms.ModelForm):

        class Meta:
            model = Grupo_Luminaria
            fields = ('nombre', 'administrador') 

class agregar_nodo_luminaria_ledForm(forms.ModelForm):

        class Meta:
            model = Nodo_LED_Grupo_Luminaria
            fields = ('nodo', 'grupo') 

class agregar_observador_grupo_ledForm(forms.ModelForm):

        class Meta:
            model = Observador_Grupo_Luminaria
            fields = ('observador', 'grupo')

class agregar_tecnico_grupo_ledForm(forms.ModelForm):

        class Meta:
            model = Tecnico_Grupo_Luminaria
            fields = ('tecnico', 'grupo') 

class agregarOrdenReparacionForm(forms.ModelForm):

        class Meta:
            model = Orden_Reparacion
            fields = ('falla', 'demandante', 'tecnico_asignado','estado') 

class observacion_Orden_ReparacionForm(forms.ModelForm):

        class Meta:
            model = Observaciones_Orden_Reparacion
            fields = ('orden', 'descripcion', 'usuario')

class agregarNodo_LEDForm(forms.ModelForm):

        class Meta:
            model = Nodo_LED
            fields = ('potencia','lampara') 

class agregarLuminaria_LEDForm(forms.ModelForm):

        class Meta:
            model = Luminaria_LED
            fields = ('modeloLampara', 'estado') 

class agregarModeloLEDForm(forms.ModelForm):

        class Meta:
            model = Modelo_Luminaria_LED
            fields = ('nombre', 'marca') 

class agregarMarcaLEDForm(forms.ModelForm):

        class Meta:
            model = Marca_Luminaria_LED
            fields = ('nombre',) 

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               label=_("Usuario"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Nombre de Usuario'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    error_messages = {
        'invalid_login': _(
            "Ingrese un usuario y contrasenia valida"
        ),
        'inactive': _("La cuenta esta inactiva."),
    }

class RegisterUserForm(forms.ModelForm):

        class Meta:
            model = Usuario
            fields = ('first_name', 'last_name', 'username','password', 'email')
            help_texts = {
                'username': None,
            }