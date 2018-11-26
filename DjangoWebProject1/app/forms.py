"""
Definition of forms.
"""
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import *
from bootstrap_datepicker.widgets import DatePicker
from django.db.models import Count
from django.db.models import F
from django.db.models import Value as V
from django.db.models.functions import Concat

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
            
class RegisterAlertaForm(forms.ModelForm):

        class Meta:
            model = Alerta
            fields = ('nombre', 'descripcion', 'grado_criticidad', 'periodicidad', 'frecuencia')   


class RegisterIncidenteForm(forms.ModelForm):

        class Meta:
            model = Incidente
            fields = ('falla', 'fecha','alerta', 'luminaria', 'estado','relevador', 'descripcion', 'asunto_mail_relevador', 'cuerpo_mail_relevador')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["descripcion"].widget = forms.Textarea()
            #self.fields['relevador'].queryset = Usuario.objects.filter(pk=1)
            #self.fields['relevador'].queryset = Usuario.objects.values('username').distinct().annotate(models.Count('pk'))[:1]
            #queryset = Usuario.objects.annotate(cantidad=Count('incidente_por_usuario')).order_by('cantidad')[:1]


            queryset = Incidente_Por_Usuario.objects.all().order_by(F('cantidad_asignados') - F('cantidad_cerrados'))[:1]            

            for each in queryset:

                self.fields['relevador'].queryset = Usuario.objects.filter(pk=each.usuario.pk)

class RegisterIncidenteFormEdit(forms.ModelForm):

        class Meta:
            model = Incidente
            fields = ('falla', 'fecha','alerta', 'luminaria', 'estado','relevador', 'descripcion', 'asunto_mail_relevador', 'cuerpo_mail_relevador')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["descripcion"].widget = forms.Textarea()

class RegisterIncidenteFormEditReparador(forms.ModelForm):

        class Meta:
            model = Incidente
            fields = ('falla', 'luminaria', 'estado', 'descripcion', 'materiales')
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["descripcion"].widget = forms.Textarea()


class RegisterConfiguracionLuminariaForm(forms.ModelForm):

        class Meta:
            model = Configuracion_Luminaria
            fields = ('nombre', 'descripcion','potencia_desde', 'potencia_hasta','imagen')			

class RegisterMarcadorLEDForm(forms.ModelForm):
        class Meta:
            model = Marcador_Luminaria_Led
            fields = ('nombre', 'luminaria','lat','lng')

class agregarIncidente_Reparador(forms.ModelForm):

        class Meta:
            model = Incidente_Por_Reparador
            fields = ('usuario', 'incidente') 

class RegisterIncidenteReparadorForm(forms.ModelForm):

        class Meta:
            model = Incidente_Por_Reparador
            fields = ('usuario', 'incidente')         

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields["incidente"].widget = forms.SelectMultiple(choices=Incidente.objects.filter(estado='p',incidente_por_reparador__isnull=True)
                .values_list('id',Concat('falla__descripcion', V(' - ') , 'luminaria__identificador',V(' - ') ,'descripcion' ) ))
            self.fields['usuario'].queryset = Usuario.objects.filter(roles__nombre='Reparador')
            


A = Usuario.objects.filter(roles__nombre='Administrador').first()

class RegisterIncidenteReasignacionForm(forms.Form):
        
        usuario= forms.CharField(label='Usuario', widget=forms.Select(choices=Usuario.objects.filter
            (roles__nombre='Administrador').values_list('id',Concat('first_name', V(' ') ,'last_name' ))))
        print(A.pk)
        incidente= forms.CharField(label='Incidente', widget=forms.SelectMultiple(choices=Incidente.objects.filter(estado='p').exclude(relevador_id=A.pk)
            .values_list('id','descripcion' )))

class RegisterMaterialForm(forms.ModelForm):

        class Meta:
            model = Material
            fields = ('descripcion', 'cantidad')         

