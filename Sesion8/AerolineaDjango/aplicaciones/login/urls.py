from django.urls import path
from . import views
urlpatterns = [
    path('login/index/', views.index), 
] 