from django.db import models

# Create your models here.
class Cargo(models.Moldel):
    idcargo = models.IntegerField(primary_key=True) # definicion de llave primaria
    Cargo = models.CharField('Cargo', max_length=60)

class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=60)
    telefono = models.CharField('Teléfono', max_length=60)
    correo = models.CharField('Correo', max_length=100)
    sueldo = models.DecimalField('Sueldo', max_digits=9, decimal_places=2)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE) 