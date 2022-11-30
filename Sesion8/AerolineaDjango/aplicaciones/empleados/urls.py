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
        'empleados/modificar-empleado/<pk>/', # /<pk>/ ayuda a especificar la llave primaria de personaje esecífico que queremos
        views.ModificarEmpleado.as_view(),
        name='modificar-empleado'),
    path(
        'empleados/eliminar-empleado/<pk>/',
        views.EliminarEmpleado.as_view(),
        name='eliminar-empleado'),

    # urls API
    path(
        'api/empleados/lista',
        views.ListaAPIEmpleado.as_view(),
        name='lista-api-empleado'),
    path(
        'api/empleados/crear',
        views.CrearAPIEmpleado.as_view(),
        name='crear-api-empleado')
] 