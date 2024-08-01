from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from usuarios.forms import UserRegisterForm


# Create your views here.


def login(respuesta):
    msg_login = ''
    if respuesta.method == 'POST':
        form = AuthenticationForm(respuesta, data=respuesta.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(respuesta, user)
                return render(respuesta, 'cursos/inicio.html')
            
        msg_login = 'Usuario o contraseña incorrecta'

    form = AuthenticationForm()
    return render(respuesta, 'usuarios/login.html', {'form': form, 'msg_login': msg_login})

def registro(respuesta):
    msg_register =''
    if respuesta.method == 'POST':

        form = UserRegisterForm(respuesta.POST)
        if form.is_valid():
            form.save()
            return render(respuesta, 'cursos/inicio.html')
        
        msg_register = 'Error en los datos'
    form = UserRegisterForm()
    return render(respuesta, 'usuarios/registro.html', {'form':form, 'msg_register': msg_register})