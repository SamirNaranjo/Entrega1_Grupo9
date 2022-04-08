from urllib import request
from django.db import models
import datetime

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    id_usuario = models.CharField('apellido', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
 
class Producto(models.Model):
   nombre_producto = models.CharField('Nombre del Producto', max_length=30)
   cantidad_producto = models.IntegerField('Cantidad de Producto')
   precio_producto = models.FloatField('Precio del producto')
   descripcion_producto = models.CharField('descripcion', max_length=200)

class Pedido(models.Model):
   numero_pedido = models.IntegerField('Numero de Pedido')
   fecha_pedido = models.DateField(auto_now=True)

   def __str__(self):
      return f'Su Pedido es el: {self.numero_pedido}, adquirido el dia {self.fecha_pedido}'


      