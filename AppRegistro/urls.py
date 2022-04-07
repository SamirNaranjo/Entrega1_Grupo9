from django import views
from django.urls import path
from .views import  inicio, pedido
from .views import usuario

urlpatterns = [
    path('', inicio),
    # path('personas/', personas),
    path('usuario/' , usuario ),
    path('pedidos/', pedido)

    
]