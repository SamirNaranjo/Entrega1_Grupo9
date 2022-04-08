from django.http import HttpResponse
from django.shortcuts import render
from AppRegistro.forms import usuario_formulario
from AppRegistro.models import Usuario
from .models import Producto
# Create your views here.

def inicio(request):

    return render(request, 'AppRegistro/inicio.html')

# def personas(request):

#     return render(request, 'Appcoder/personas.html')

def usuario(request):
    if request.method == 'POST':
        usurioFormulario = usuario_formulario(request.POST)
        #print(usurioFormulario)
        if usurioFormulario.is_valid():
            informacion = usurioFormulario.cleaned_data
            persona = Usuario(nombre = informacion['nombre'], id_usuario = informacion['id_usuario'], contraseña= informacion['contraseña'])
            persona.save()
            return render(request, 'AppRegistro/inicio.html')
        

    else:
        usurioFormulario = usuario_formulario()
        return render (request, 'AppRegistro/usuario.html', {'miForm':usurioFormulario})

def pedido (request):

    return render(request, 'AppRegistro/pedido.html')

def productoFormulario(request):

    return render(request, 'AppRegistro/productoFormulario.html')

def productoFormularioPost(request):

    nombre_producto = request.POST['nombre_producto']
    cantidad_producto= request.POST['cantidad_producto']
    precio_producto = request.POST['precio_producto']
   

    producto = Producto(nombre_producto= nombre_producto, cantidad_producto=cantidad_producto, precio_producto=precio_producto,)
    
    producto.save()

    return render(request, 'AppRegistro/productoFormulario.html', {'nombre_producto': nombre_producto, 'cantidad_producto':cantidad_producto, 'precio_producto': precio_producto,})

