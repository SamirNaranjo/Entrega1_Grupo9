from django.urls import path

from  .views import usuario
from .views import  inicio

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/', usuario),
    
]