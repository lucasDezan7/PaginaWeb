from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from usuarios.forms import UserRegisterForm


# Create your views here.


def login_request(request):
    msg_login = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, 'cursos/inicio.html')
            
        msg_login = 'Usuario o contraseña incorrecta'

    form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form, 'msg_login': msg_login})

def registro(request):
    msg_register =''
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cursos/inicio.html')
        
        msg_register = 'Error en los datos'
    form = UserRegisterForm()
    return render(request, 'usuarios/registro.html', {'form':form, 'msg_register': msg_register})