from typing_extensions import Self
from urllib import request
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    id_usuario = models.CharField('apellido', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
 
class Producto():
   nombre_producto = models.CharField('Nombre del Producto', max_length=30)
   cantidad_producto = models.IntegerField('Cantidad de Producto')
   precio_producto = models.FloatField('Precio del producto')

class Pedido():
   numero_pedido = models.IntegerField('Numero de Pedido')
   fecha_pedido = models.DateField()



      