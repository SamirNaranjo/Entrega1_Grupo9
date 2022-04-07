from operator import length_hint
from django import forms

class usuario_formulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=20)
    id_usuario= forms.CharField(label="Usuario", required=True)
    contraseña= forms.CharField(label="Password", max_length=10)
