from django import forms

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=40)
    mail = forms.EmailField()