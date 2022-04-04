
from urllib import request
from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    id_usuario = models.CharField('apellido', max_length=50)
    password= models.CharField('password', max_length=50)

#class Producto(models.Model):
    #nombre_producto = 
    #cantidad_producto =
    #precio_producto = 

#class Pedido(models.Model):
    #numero_pedido =


#class Catalogo_producto(models.Model):
    #mostrar_producto
