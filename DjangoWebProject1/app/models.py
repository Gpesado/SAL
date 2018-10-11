from django.db import models

from django.contrib.auth.models import AbstractUser
from django.urls import reverse
class Rol (models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return "{0}".format(self.nombre)

#LOGGING
class Usuario(AbstractUser):    

    email = models.EmailField(verbose_name='Mail', unique=True)
    first_name = models.CharField(verbose_name='Nombre', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Apellido', max_length=30, blank=True)

    def get_absolute_url(self):
        return reverse('usuario_update', args=[str(self.id)])
    
    def get_delete_url(self):
        return reverse('usuario_delete', args=[str(self.id)])

    def get_success_url(self):
        return reverse('usuarios')

    def __str__(self):
        return "{0} {1} ({2})".format(self.first_name,self.last_name,self.username)
    
    roles = models.ManyToManyField(Rol)


    
class Usuarios_has_rol(models.Model):
    usuario = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, null = False,blank = False, on_delete=models.CASCADE)


#Luminarias
    #FABRICANTES
class Fabricante(models.Model):
    nombre = models.CharField(max_length=35)
    
    #Luminarias LED
class Marca_Luminaria_LED(models.Model):
    nombre = models.CharField(max_length=35)
    
    def __str__(self):
        return "{0}".format(self.nombre)
    
class Marca_has_Fabricante_LED(models.Model):
    marca = models.ForeignKey(Marca_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, null = False,blank = False, on_delete=models.CASCADE)
  
class Modelo_Luminaria_LED(models.Model):
    nombre = models.CharField(max_length=35)
    marca = models.ForeignKey(Marca_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0} {1}".format(self.nombre,self.marca)
    
class Luminaria_LED(models.Model):
    modeloLampara = models.ForeignKey(Modelo_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    ESTADO = (('f','En funcionamiento'), ('d','Con desperfectos'), ('r','En Reparacion'), ('d','Desconectada'))
    estado = models.CharField(max_length= 1, choices=ESTADO, default='d')
    def __str__(self):
      return "{0} {1}".format(self.estado,self.modeloLampara)
      
class Nodo_LED(models.Model):
    id = models.UUIDField
    es_concentrador = models.BooleanField
    potencia = models.FloatField(null = False,blank = False)
    lampara = models.ForeignKey(Luminaria_LED, null = True,blank = False, on_delete=models.CASCADE)

    
#LUMINARIAS NO LED
class Marca_Luminaria_NO_LED(models.Model):
    nombre = models.CharField(max_length= 35)

class Marca_has_Fabricante_NO_LED(models.Model):
    marca = models.ForeignKey(Marca_Luminaria_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
    fabricante = models.ForeignKey(Fabricante, null = False,blank = False, on_delete=models.CASCADE)

class Modelo_Luminaria_NO_LED(models.Model):
    nombre = models.CharField(max_length= 35)
    marca = models.ForeignKey(Marca_Luminaria_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
   
class Balastro(models.Model):
    modelo = models.CharField(max_length= 35)
    modeloLampara = models.ForeignKey(Fabricante, null = False,blank = False, on_delete=models.CASCADE)

class Lampara_No_LED(models.Model):
    modeloLampara = models.ForeignKey(Modelo_Luminaria_NO_LED, null = True,blank = False, on_delete=models.CASCADE)
    es_incandecente = models.BooleanField
    balastro = models.ForeignKey(Balastro, null = True,blank = False, on_delete=models.CASCADE)
    ESTADO = (('f','En funcionamiento'), ('d','Con desperfectos'), ('r','En Reparacion'), ('d','Desconectada'))
    estado = models.CharField(max_length= 1, choices=ESTADO, default='d')

class Nodo_NO_LED(models.Model):
    id = models.UUIDField
    es_concentrador = models.BooleanField
    potencia = models.FloatField(null = False,blank = False)
    lampara = models.ForeignKey(Lampara_No_LED, null = True,blank = False, on_delete=models.CASCADE)    

#GRUPOS LUMINARIAS
class Grupo_Luminaria(models.Model):
    nombre = models.CharField(max_length= 35)
    administrador = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0} (admin = {1})".format(self.nombre, self.administrador.__str__())

class Nodo_LED_Grupo_Luminaria(models.Model):
    nodo = models.ForeignKey(Nodo_LED, null = False,blank = False, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo_Luminaria, null = False,blank = False, on_delete=models.CASCADE)
    
class Nodo_NO_LED_Grupo_Luminaria(models.Model):
    nodo = models.ForeignKey(Nodo_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo_Luminaria, null = False,blank = False, on_delete=models.CASCADE)
    
class Observador_Grupo_Luminaria(models.Model):
    observador = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo_Luminaria, null = False,blank = False, on_delete=models.CASCADE)
    
class Tecnico_Grupo_Luminaria(models.Model):
    tecnico = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo_Luminaria, null = False,blank = False, on_delete=models.CASCADE)

#STOCK DE INSUMOS PARA REPARACIONES
class Stock_Luminaria_LED(models.Model):
    item = models.ForeignKey(Modelo_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField
    
class Stock_Luminaria_NO_LED(models.Model):
    item = models.ForeignKey(Modelo_Luminaria_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField
    
class Stock_Balastros(models.Model):    
    item = models.ForeignKey(Balastro, null = False,blank = False, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField
    
class Insumo_Basico(models.Model):
    nombre = models.CharField(max_length= 15)
    
class Stock_Insumos_Basicos(models.Model):
    item = models.ForeignKey(Insumo_Basico, null = False,blank = False, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField
    
#INDICENCIAS EN LUMINARIAS
    #FALLAS
class Falla(models.Model):
    nombre = models.CharField(max_length= 35)
    descripcion = models.CharField(max_length= 35)
    criticidad = (('a','Alta'), ('m','Media'), ('b','Baja'))
    grado_criticidad = models.CharField(max_length=1, choices=criticidad, default='m')
    def __str__(self):
        return "{0} ({1})".format(self.nombre,self.grado_criticidad)

    #ORDEN_REPARACION
class Orden_Reparacion(models.Model):
    falla = models.ForeignKey(Falla, null = False,blank = False, on_delete=models.CASCADE)
    demandante = models.ForeignKey(Usuario,related_name='%(class)s_requests_created', null = True,blank = False, on_delete=models.CASCADE)
    fecha = models.DateField
    tecnico_asignado = models.ForeignKey(Usuario, null = True,blank = False, on_delete=models.CASCADE)
    estados_fallas = (('prt','Pendiente de revision tecnica'), 
                      ('pcf','Pendiente de confirmacion tecnica'), 
                      ('cna','Confirmacion no aprobada, pendiente de arreglo'),
                      ('tca','Ticket cerrado por aprobacion'),
                      ('tcs','Ticket cerrado sin aprobacion'))
    estado = models.CharField(max_length= 3, choices=estados_fallas, default='prt')
    def __str__(self):
        return "{0} (tec:{1}) (estado:{2})".format(self.falla,self.tecnico_asignado,self.estado)
    
class Observaciones_Orden_Reparacion(models.Model):
    orden = models.ForeignKey(Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, null = True,blank = False, on_delete=models.CASCADE)
    
    
#GASTOS EN REPARACIONES
class Gasto_Por_Luminaria_LED(models.Model):
    observacion_orden = models.ForeignKey(Observaciones_Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    item_gastado = models.ForeignKey(Stock_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    
class Gasto_Por_Lumimnaria_NO_LED(models.Model):
    orden = models.ForeignKey(Observaciones_Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    item_gastado = models.ForeignKey(Stock_Luminaria_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
    
class Gasto_Por_Balastro(models.Model):
    orden = models.ForeignKey(Observaciones_Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    item_gastado = models.ForeignKey(Stock_Balastros, null = False,blank = False, on_delete=models.CASCADE)
    
class Gasto_Por_Insumo_Basico(models.Model):
    orden = models.ForeignKey(Observaciones_Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    item_gastado = models.ForeignKey(Stock_Insumos_Basicos, null = False,blank = False, on_delete=models.CASCADE)
    
    
#SISTEMA DE ALERTAS
class Alerta(models.Model):
    nombre = models.CharField(max_length= 35)
    descripcion = models.CharField(max_length= 100)
    tiempo = models.TimeField
    criticidad = (('a','Alta'), ('m','Media'), ('b','Baja'))
    grado_criticidad = models.CharField(max_length= 1, choices=criticidad, default='m')
    
class Notificacion_alerta(models.Model):
    alerta = models.ForeignKey(Alerta, null = False,blank = False, on_delete=models.CASCADE)
    destinatario = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    asunto = models.CharField(max_length= 100)
   
class Personalizacion_Alerta(models.Model):
    alerta = models.ForeignKey(Alerta, null = False,blank = False, on_delete=models.CASCADE)
    personalizador = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE) 