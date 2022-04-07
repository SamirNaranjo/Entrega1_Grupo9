from django.shortcuts import render
from AppRegistro.forms import usuario_formulario
from AppRegistro.models import Usuario

# Create your views here.

def inicio(request):

    return render(request, 'AppRegistro/inicio.html')

# def personas(request):

#     return render(request, 'Appcoder/personas.html')

def usuario(request):

    if request.method == 'POST':
        usurioFormulario = usuario_formulario(request.POST)
        #print(usurioFormulario)
        if usurioFormulario.is_valid:
            informacion = usurioFormulario.cleaned_data
            persona = Usuario(nombre = informacion['nombre'], id_usuario = informacion['id_usuario'], contraseña= informacion['contraseña'])
            persona.save()
            return render(request, 'inicio.html')
        

    else:
        usurioFormulario = usuario_formulario()
        return render (request, 'AppRegistro/usuario.html', {'miForm':usurioFormulario})

        