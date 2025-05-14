from django.contrib import admin
from .models import Empleado, Cargo, Departamento, TipoContrato, Rol, BonificacionExtra

# Register your models here.
admin.site.register(Empleado)
admin.site.register(Cargo)
admin.site.register(Departamento)
admin.site.register(TipoContrato)
admin.site.register(Rol)
admin.site.register(BonificacionExtra)