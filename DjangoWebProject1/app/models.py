from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime

class Menu(models.Model):
    nombre = models.CharField(max_length=35)
    url = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return "{0}".format(self.nombre)

class Rol (models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return "{0}".format(self.nombre)

    menues = models.ManyToManyField(Menu)

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

    def algo(self, pagina):
        for rol in self.roles.all():
            for menu in rol.menues.all():
                if menu.nombre == pagina:
                    return True
        return False

#Luminarias
    #FABRICANTES
class Fabricante(models.Model):
    nombre = models.CharField(max_length=35)
    origen = models.CharField(max_length=35, default='Argentina')
    def __str__(self):
        return "{0}".format(self.nombre)

    
    #Luminarias LED
class Marca_Luminaria_LED(models.Model):
    nombre = models.CharField(max_length=35)
    fabricante = models.ManyToManyField(Fabricante)
    
    def __str__(self):
        return "{0}".format(self.nombre)
  
class Modelo_Luminaria_LED(models.Model):
    nombre = models.CharField(max_length=35)
    marca = models.ForeignKey(Marca_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.nombre,self.marca)
    
class Luminaria_LED(models.Model):
    identificador = models.CharField(max_length=35,default='LAMP_LED_')
    modeloLampara = models.ForeignKey(Modelo_Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    ESTADO = (('f','En funcionamiento'), ('d','Con desperfectos'), ('r','En Reparacion'), ('d','Desconectada'))
    estado = models.CharField(max_length= 1, choices=ESTADO, default='d')
    def __str__(self):
      return "{2} ({0} MOD: {1})".format(self.estado,self.modeloLampara,self.identificador)
      
      
class Nodo_LED(models.Model):
    identificador = models.CharField(max_length=35,default='N_LED_')
    es_concentrador = models.BooleanField(default='False')
    potencia_esperada = models.FloatField(null = False,blank = False,default = 0)
    potencia_real = models.FloatField(null = False,blank = False,default = 0)
    fecha_ult_medicion = models.DateField(default = datetime.date.today, blank=False)
    lampara = models.ForeignKey(Luminaria_LED, null = True,blank = False, on_delete=models.CASCADE)

    def __str__(self):
        return "{3} (LAMP = {0}POT = {1} / {4} ) (CON = {2})".format(self.lampara.__str__(), self.potencia_real.__str__(), self.es_concentrador.__str__(),self.identificador, self.potencia_esperada)

    
#LUMINARIAS NO LED
class Marca_Luminaria_NO_LED(models.Model):
    nombre = models.CharField(max_length= 35)
    fabricante = models.ManyToManyField(Fabricante)
    def __str__(self):
        return "{0}".format(self.nombre)

class Modelo_Luminaria_NO_LED(models.Model):
    nombre = models.CharField(max_length= 35)
    marca = models.ForeignKey(Marca_Luminaria_NO_LED, null = False,blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0} {1}".format(self.nombre,self.marca)

class Balastro(models.Model):
    modelo = models.CharField(max_length= 35)
    fabricante = models.ForeignKey(Fabricante, null = False,blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}".format(self.modelo)

class Lampara_No_LED(models.Model):
    identificador = models.CharField(max_length=35,default='LAMP_NLED_')
    modeloLampara = models.ForeignKey(Modelo_Luminaria_NO_LED, null = True,blank = False, on_delete=models.CASCADE)
    es_incandecente = models.BooleanField(default='False')
    balastro = models.ForeignKey(Balastro, null = True,blank = False, on_delete=models.CASCADE)
    ESTADO = (('f','En funcionamiento'), ('d','Con desperfectos'), ('r','En Reparacion'), ('d','Desconectada'))
    estado = models.CharField(max_length= 1, choices=ESTADO, default='d')
    def __str__(self):
      return "{2} ({0} MOD: {1})".format(self.estado,self.modeloLampara,self.identificador)
class Nodo_NO_LED(models.Model):
    identificador = models.CharField(max_length=35,default='N_NLED_')
    es_concentrador = models.BooleanField(default='False')
    potencia_esperada = models.FloatField(null = False,blank = False,default = 0)
    potencia_real = models.FloatField(null = False,blank = False,default = 0)
    fecha_ult_medicion = models.DateField(default = datetime.date.today, blank=False)
    lampara = models.ForeignKey(Lampara_No_LED, null = True,blank = False, on_delete=models.CASCADE)

    def __str__(self):
        return "{3} (LAMP = {0}POT = {1}) (CON = {2})".format(self.lampara.__str__(), self.potencia.__str__(), self.es_concentrador.__str__(),self.identificador)

#GRUPOS LUMINARIAS
class Grupo_Luminaria(models.Model):
    nombre = models.CharField(max_length= 35 , null = False)
    administrador = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    nodo_luminarias_led = models.ManyToManyField(Nodo_LED, blank=True)
    nodo_luminarias_no_led = models.ManyToManyField(Nodo_NO_LED, blank=True)
    observadores = models.ManyToManyField(Usuario, related_name='observadores', blank=True)
    tecnicos = models.ManyToManyField(Usuario, related_name='tecnicos', blank=True)

    def __str__(self):
        return "{0} (admin = {1})".format(self.nombre, self.administrador.__str__())
    
    
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

    #INCIDENTES
class Incidente(models.Model):
    falla = models.ForeignKey(Falla, null = False,blank = False, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today, blank=False)
    luminaria = models.ForeignKey(Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    estado_incidente = (('a','Arreglado'), ('e','En reparacion'), ('p','Pendiente de Reparacion'))
    estado = models.CharField(max_length=1, choices=estado_incidente, default='p')
    relevador = models.ForeignKey(Usuario, null = False,blank = False, on_delete=models.CASCADE)
    def __str__(self):
        return "{2} (F: {0}/{1}{3})".format(self.falla,self.fecha,self.luminaria,self.estado)

    #ORDEN_REPARACION
class Orden_Reparacion(models.Model):
    falla = models.ForeignKey(Falla, null = False,blank = False, on_delete=models.CASCADE)
    demandante = models.ForeignKey(Usuario,related_name='%(class)s_requests_created', null = True,blank = False, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today, blank=False)
    tecnico_asignado = models.ForeignKey(Usuario, null = True,blank = False, on_delete=models.CASCADE)
    estados_fallas = (('prt','Pendiente de revision tecnica'), 
                      ('pcf','Pendiente de confirmacion tecnica'), 
                      ('cna','Confirmacion no aprobada, pendiente de arreglo'),
                      ('tca','Ticket cerrado por aprobacion'),
                      ('tcs','Ticket cerrado sin aprobacion'))
    estado = models.CharField(max_length= 3, choices=estados_fallas, default='prt')
    def __str__(self):
        return "{0} {1}(tec:{2}) (estado:{3})".format(self.falla,self.demandante,self.tecnico_asignado,self.estado)
    
class Observaciones_Orden_Reparacion(models.Model):
    orden = models.ForeignKey(Orden_Reparacion, null = False,blank = False, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.date.today, blank=False)
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

#MARCADOR LUMINARIAS
class Marcador_Luminaria_Led(models.Model):
    nombre = models.CharField(max_length= 35)
    luminaria = models.ForeignKey(Luminaria_LED, null = False,blank = False, on_delete=models.CASCADE)
    lat = models.CharField(max_length= 35)
    lng = models.CharField(max_length= 35)

    def __str__(self):
        return "{0} L:{1}(cord:{2},{3})".format(self.nombre,self.luminaria,self.lat,self.lng)

class Marcador_Luminaria_No_Led(models.Model):
    nombre = models.CharField(max_length= 35)
    luminaria = models.ForeignKey(Lampara_No_LED, null = False,blank = False, on_delete=models.CASCADE)
    lat = models.CharField(max_length= 35)
    lng = models.CharField(max_length= 35)

    def __str__(self):
        return "{0} L:{1}(cord:{2},{3})".format(self.nombre,self.luminaria,self.lat,self.lng)
class Marcador_Grupo_Luminaria(models.Model):
    nombre = models.CharField(max_length= 35)
    grupo = models.ForeignKey(Grupo_Luminaria, null = False,blank = False, on_delete=models.CASCADE)
    marcadoresLed = models.ManyToManyField(Marcador_Luminaria_Led, blank=True)
    marcadoresNoLed = models.ManyToManyField(Marcador_Luminaria_No_Led, blank=True)
    lat = models.CharField(max_length= 35)
    lng = models.CharField(max_length= 35)
    
    def __str__(self):
        return "{0} L:{1}(cord:{2},{3})".format(self.nombre,self.grupo,self.lat,self.lng)