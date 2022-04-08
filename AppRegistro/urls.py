from django import views
from django.urls import path
from .views import  inicio, pedido,productoFormulario,productoFormularioPost
from .views import usuario

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/' , usuario, name= "usuario_formulario"),
    path('pedidos/', pedido),
    path('productoFormulario/' , productoFormulario, name= 'productoFormulario' ),
    path('productoFormularioPost/' , productoFormularioPost, name= 'productoFormularioPost' ),

    
]