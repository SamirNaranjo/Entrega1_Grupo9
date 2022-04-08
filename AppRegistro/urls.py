from django.urls import path
from .views import  inicio, productoFormulario, productoFormularioPost
from .views import usuario

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/' , usuario ),
    path('productoFormulario/' , productoFormulario, name= 'productoFormulario' ),
    path('productoFormularioPost/' , productoFormularioPost, name= 'productoFormularioPost' ),
        
]