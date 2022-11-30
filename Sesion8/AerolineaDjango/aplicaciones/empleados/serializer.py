from .models import Empleado, Cargo, Proyecto
from rest_framework import serializers

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id','nombre', 'telefono','correo','sueldo','cargo','proyecto')

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('idcargo','cargo')

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('__all__')

class EmpleadoAllSerializer(serializers.ModelSerializer):
    cargo = CargoSerializer()
    proyecto = ProyectoSerializer(many=True)
    class Meta:
        model = Empleado
        fields = ('__all__')