from django.shortcuts import render
from .models import Empleado, Cargo
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from rest_framework.generics import (ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView)
from .serializer import EmpleadoSerializer, EmpleadoAllSerializer

# API Viesws
class ListaAPIEmpleado(ListAPIView):
    serializer_class = EmpleadoAllSerializer
    queryset = Empleado.objects.all()
class CrearAPIEmpleado(CreateAPIView):
    serializer_class = EmpleadoSerializer
class EliminarAPIEmpleado(DestroyAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
class ObtenerAPIEmpleado(RetrieveAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
class ModificarAPIEmpleado(RetrieveUpdateAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
class Modificar2APIEmpleado(UpdateAPIView):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()

# Create your views here.
def index(request):
    return render(request, 'empleados/index.html') 

# views empleados
class ListaEmpleados(ListView):
    template_name = 'empleados/lista-empleados.html'
    model = Empleado
    context_object_name = 'lista_empleados'
class CrearEmpleado(CreateView):
    template_name = 'empleados/crear-empleado.html'
    model = Empleado
    fields = ['nombre', 'telefono','correo','sueldo','cargo']
    success_url = reverse_lazy('empleados_app:lista-empleados')
class ModificarEmpleado(UpdateView):
    template_name = 'empleados/modificar-empleado.html'
    model = Empleado
    fields = ['nombre', 'telefono','correo','sueldo','cargo']
    success_url = reverse_lazy('empleados_app:lista-empleados')
class EliminarEmpleado(DeleteView):
    template_name = 'empleados/eliminar-empleado.html'
    model = Empleado 
    success_url = reverse_lazy('empleados_app:lista-empleados') 