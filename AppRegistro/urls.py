from django import views
from django.urls import path

from AppRegistro.forms import usuario_formulario
from .views import  inicio
from .views import usuario

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/' , usuario, name= "usuario_formulario"),
    
    
    
]