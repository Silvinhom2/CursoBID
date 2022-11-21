from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path('empleados/index/', views.index, name='index-empleado'),
    path(
        'empleados/lista-empleados/',
        views.ListaEmpleados.as_view(),
        name='lista-empleados'),
    path(
        'empleados/crear-empleado',
        views.CrearEmpleado.as_view(),
        name='crear-empleado'),
    path(
        'empleados/modificar-empleado/<pk>/',
        views.CrearEmpleado.as_view(),
        name='modificar-empleado'),
    path(
        'empleados/eliminar-empleado/<pk>/',
        views.CrearEmpleado.as_view(),
        name='eliminar-empleado')
] 