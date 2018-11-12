"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *
from bootstrap_datepicker.widgets import DatePicker

class agregarFallaForm(forms.ModelForm):

        class Meta:
            model = Falla
            fields = ('nombre', 'descripcion','grado_criticidad') 

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
            fields = ('identificador','es_concentrador','potencia_esperada','potencia_real','fecha_ult_medicion','lampara')

class agregarLuminaria_LEDForm(forms.ModelForm):

        class Meta:
            model = Luminaria_LED
            fields = ('identificador','modeloLampara', 'estado') 

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
        password = forms.CharField(widget=forms.PasswordInput)    

        class Meta:
            model = Usuario
            fields = ('username', 'first_name', 'last_name', 'password', 'email', 'roles')
            help_texts = {
                'username': None,
            }

class EditUserForm(forms.ModelForm):         

        class Meta:
            model = Usuario
            fields = ('username', 'first_name', 'last_name', 'email', 'roles')
            help_texts = {
                'username': None,
            }

class RolForm(forms.ModelForm):

        class Meta:
            model = Rol
            fields = ('nombre', 'menues')
            
class MenuForm(forms.ModelForm):

        class Meta:
            model = Menu
            fields = ('nombre',)

class RegisterGrupoLuminariaForm(forms.ModelForm):

        class Meta:
            model = Grupo_Luminaria
            fields = ('nombre', 'administrador','nodo_luminarias_led','nodo_luminarias_no_led','observadores','tecnicos')
            
class RegisterOrdenForm(forms.ModelForm):

        class Meta:
            model = Orden_Reparacion
            fecha = forms.DateField(
                widget=DatePicker(
                    options={
                        "format": "mm/dd/yyyy",
                        "autoclose": True
                    }
                )
            )
            fields = ('falla','demandante','fecha','tecnico_asignado','estado')

#NUEVOS NUEVOS NUEVOSNUEVOS NUEVOS NUEVOSNUEVOS NUEVOS NUEVOSNUEVOS NUEVOS NUEVOSNUEVOS NUEVOS NUEVOSNUEVOS NUEVOS NUEVOS
class RegisterFabricanteForm(forms.ModelForm):

        class Meta:
            model = Fabricante
            fields = ('nombre','origen')
            
class RegisterLuminarialedForm(forms.ModelForm):

        class Meta:
            model = Luminaria_LED
            fields = ('identificador', 'modeloLampara','estado')
            
class RegisterLuminarianoledForm(forms.ModelForm):

        class Meta:
            model = Lampara_No_LED
            fields = ('identificador','modeloLampara', 'es_incandecente','balastro','estado')
            
class RegisterMarcaledForm(forms.ModelForm):

        class Meta:
            model = Marca_Luminaria_LED
            fields = ('nombre', 'fabricante')
            
class RegisterMarcanoledForm(forms.ModelForm):

        class Meta:
            model = Marca_Luminaria_NO_LED
            fields = ('nombre', 'fabricante')
            
class RegisterModeloledForm(forms.ModelForm):

        class Meta:
            model = Modelo_Luminaria_LED
            fields = ('nombre', 'marca')
            
class RegisterModelonoledForm(forms.ModelForm):

        class Meta:
            model = Modelo_Luminaria_NO_LED
            fields = ('nombre', 'marca')
            
class RegisterNodoledForm(forms.ModelForm):

        class Meta:
            model = Nodo_LED
            fields = ('identificador', 'es_concentrador','potencia_esperada','potencia_real','fecha_ult_medicion','lampara')
            
class RegisterNodonoledForm(forms.ModelForm):

        class Meta:
            model = Nodo_NO_LED
            fields = ('identificador', 'es_concentrador','potencia_esperada','potencia_real','fecha_ult_medicion','lampara')    

class RegisterBalastroForm(forms.ModelForm):

        class Meta:
            model = Balastro
            fields = ('modelo', 'fabricante')   
            
class RegisterIncidenteForm(forms.ModelForm):

        class Meta:
            model = Incidente
            fields = ('falla', 'fecha','luminaria', 'estado','relevador')

class RegisterMarcadorLEDForm(forms.ModelForm):
        class Meta:
            model = Marcador_Luminaria_Led
            fields = ('nombre', 'luminaria','lat','lng')