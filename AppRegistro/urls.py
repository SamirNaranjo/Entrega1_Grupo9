from django.urls import path
from .views import  inicio
from .views import usuario

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/' , usuario ),
    
    
]