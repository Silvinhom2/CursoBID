from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre_proyecto = models.CharField('Nombre proyecto', max_length=50)
    fecha_inicio = models.DateField('Fecha de inicio', auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField('Fecha de fin', auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.nombre_proyecto
class Cargo(models.Model):
    idcargo = models.IntegerField(primary_key=True) # definicion de llave primaria
    cargo = models.CharField('Cargo', max_length=60)

    def __str__(self):
        return self.cargo

class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    telefono = models.CharField('Teléfono', max_length=60)
    correo = models.CharField('Correo', max_length=100)
    sueldo = models.DecimalField('Sueldo', max_digits=9, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE) 
    proyecto = models.ManyToManyField(Proyecto, blank=False, related_name='proyecto_empleado')