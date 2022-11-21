from django.shortcuts import render
from .models import Empleado, Cargo
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy

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