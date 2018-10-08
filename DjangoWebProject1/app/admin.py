from django.contrib import admin

from .models import *


admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Usuarios_has_rol)
admin.site.register(Fabricante)
admin.site.register(Marca_Luminaria_LED)
admin.site.register(Marca_has_Fabricante_LED)
admin.site.register(Modelo_Luminaria_LED)
admin.site.register(Luminaria_LED)
admin.site.register(Nodo_LED)
admin.site.register(Marca_Luminaria_NO_LED)
admin.site.register(Marca_has_Fabricante_NO_LED)
admin.site.register(Modelo_Luminaria_NO_LED)
admin.site.register(Balastro)
admin.site.register(Lampara_No_LED)
admin.site.register(Nodo_NO_LED)
admin.site.register(Grupo_Luminaria)
admin.site.register(Nodo_LED_Grupo_Luminaria)
admin.site.register(Nodo_NO_LED_Grupo_Luminaria)
admin.site.register(Observador_Grupo_Luminaria)
admin.site.register(Tecnico_Grupo_Luminaria)
admin.site.register(Stock_Luminaria_LED)
admin.site.register(Stock_Luminaria_NO_LED)
admin.site.register(Stock_Balastros)
admin.site.register(Insumo_Basico)
admin.site.register(Stock_Insumos_Basicos)
admin.site.register(Falla)
admin.site.register(Orden_Reparacion)
admin.site.register(Observaciones_Orden_Reparacion)
admin.site.register(Gasto_Por_Luminaria_LED)
admin.site.register(Gasto_Por_Lumimnaria_NO_LED)
admin.site.register(Gasto_Por_Balastro)
admin.site.register(Gasto_Por_Insumo_Basico)
admin.site.register(Alerta)
admin.site.register(Notificacion_alerta)
admin.site.register(Personalizacion_Alerta)