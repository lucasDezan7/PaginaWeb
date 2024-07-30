from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from cursos.models import Cursos, Profesor, Estudiantes
from cursos.forms import *

# Create your views here.

def inicio(respuesta):
    return render(respuesta,'cursos/inicio.html')

class CursoListView(ListView):
    model = Cursos
    context_object_name = 'cursos'
    template_name = 'cursos/listar.html'


class ProfesoresListView(ListView):
    model = Profesor
    context_object_name = 'profesores'
    template_name = 'cursos/profesores.html'


class EstudiantesListView(ListView):
    model = Estudiantes
    context_object_name = 'estudiantes'
    template_name = 'cursos/estudiantes.html'


def busquedaCamada(resquest):
    return render(resquest, 'cursos/buscarCurso.html')

def busquedaProfesor(respuesta):
    return render(respuesta, 'cursos/buscarProfesor.html')

def buscar(respuesta):
    if respuesta.GET['nombre']:
        nombre = respuesta.GET['nombre']
        cursos = Cursos.objects.filter(nombre__icontains = nombre)

        return render(respuesta, 'cursos/buscar.html', {'cursos':cursos, 'nombre':nombre})
    else:
        respuesta = 'no enviaste datos'
    return HttpResponse(respuesta)

def buscarProfesor(respuesta):
    if respuesta.GET['nombre']:
        nombre = respuesta.GET['nombre']
        profesor = Profesor.objects.filter(nombre__icontains = nombre)

        return render(respuesta, 'cursos/buscarr.html', {'profesor':profesor, 'nombre':nombre})
    else:
        respuesta = 'no enviaste datos'
    return HttpResponse(respuesta)



def profesorFormulario(resquest):

    if resquest.method == 'POST':

        miFormulario = ProfesorFormulario(resquest.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            profesor.save()
            return render(resquest, 'cursos/profesores.html')
    else:
        miFormulario = ProfesorFormulario()
    
    return render(resquest, 'cursos/agregarprofesor.html',{"miFormulario":miFormulario})

def estudiantesFormulario(resquest):

    if resquest.method == 'POST':

        miFormulario = EstudiantesFormulario(resquest.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            profesor.save()
            return render(resquest, 'cursos/estudiantes.html')
    else:
        miFormulario = EstudiantesFormulario()
    
    return render(resquest, 'cursos/agregarestudiantes.html',{"miFormulario":miFormulario})