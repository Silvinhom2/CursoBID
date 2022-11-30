from .models import Empleado, Cargo, Proyecto
from rest_framework import serializers

class EmpleadoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id','nombre', 'telefono','correo','sueldo','cargo','proyecto']
class CargoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['idcargo','cargo']
class ProyectoSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['__all__']