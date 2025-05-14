from django.db import models
from decimal import Decimal

class Cargo(models.Model):
    descripcion = models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion

class Departamento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20, unique=True)
    direccion = models.TextField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Rol(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    aniomes = models.DateField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    horas_extra = models.DecimalField(max_digits=10, decimal_places=2)
    bono = models.DecimalField(max_digits=10, decimal_places=2)
    iess = models.DecimalField(max_digits=10, decimal_places=2)
    tot_ing = models.DecimalField(max_digits=10, decimal_places=2)
    tot_des = models.DecimalField(max_digits=10, decimal_places=2)
    neto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Rol de {self.empleado.nombre} para {self.aniomes}"
    
    def save(self, *args, **kwargs):
        # Sueldo desde empleado
        self.sueldo = self.empleado.sueldo
        
        # Calcular IESS (9.45% del sueldo)
        self.iess = round(self.sueldo * Decimal('0.0945'), 2)

        # Calcular bonificaciones extras (solo si ya está guardado y tiene ID)
        bonificaciones_suma = Decimal('0')
        if self.pk:  # Solo si ya existe
            bonificaciones_suma = self.bonificaciones.aggregate(
                total=models.Sum('monto')
            )['total'] or Decimal('0')

        # Calcular ingresos y descuentos
        self.tot_ing = round(self.sueldo + self.horas_extra + self.bono + bonificaciones_suma, 2)
        self.tot_des = self.iess
        self.neto = round(self.tot_ing - self.tot_des, 2)

        super().save(*args, **kwargs)


class BonificacionExtra(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='bonificaciones')
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Guarda la bonificación
        self.rol.save()  # Actualiza los totales del rol asociado
