from django.shortcuts import render

from AppRegistro.models import Producto

# Create your views here.

def inicio(request):

    return render(request, 'AppRegistro/inicio.html')

# def personas(request):

#     return render(request, 'Appcoder/personas.html')

def usuario(request):

    return render(request, 'AppRegistro/usuario.html') 

def productoFormulario(request):

    return render(request, 'AppRegistro/productoFormulario.html')

def productoFormularioPost(request):

    nombre_producto = request.POST['nombre_producto']
    cantidad_producto= request.POST['cantidad_producto']
    precio_producto = request.POST['precio_producto']
    descripcion_producto = request.POST['descripcion']

    producto = Producto(nombre_producto= nombre_producto, cantidad_producto=cantidad_producto, precio_producto=precio_producto, descripcion_producto=descripcion_producto)
    
    producto.save()

    return render(request, 'AppRegistro/productoFormulario.html', {'nombre_producto': nombre_producto, 'cantidad_producto':cantidad_producto, 'precio_producto': precio_producto, 'descripcion': descripcion_producto })


