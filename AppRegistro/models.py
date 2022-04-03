from typing_extensions import Self
from urllib import request
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    id_usuario = models.CharField('apellido', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
 
class Producto():
    #nombre_producto = 
    #cantidad_producto =
    #precio_producto = 

class Pedido():
    #numero_pedido =


class Catalogo_producto():
    #mostrar_producto #metodo
    