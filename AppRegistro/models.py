from urllib import request
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    id_usuario = models.CharField('apellido', max_length=50)
    contraseña = models.CharField('contraseña', max_length=50)
 
class Producto(models.Model):
   nombre_producto = models.CharField('nombre_producto', max_length=30)
   cantidad_producto = models.IntegerField('cantidad_producto')
   precio_producto = models.FloatField('precio_producto')
   descripcion_producto = models.CharField('descripcion', max_length=200)

class Pedido():
   numero_pedido = models.IntegerField('Numero de Pedido')
   fecha_pedido = models.DateField()



      