from django.urls import path
from . import views
urlpatterns = [
    path('empleados/index/', views.index), 
]