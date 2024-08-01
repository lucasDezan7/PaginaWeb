from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from cursos.models import Cursos, Profesor, Estudiantes
from cursos.forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(respuesta):
    return render(respuesta,'cursos/inicio.html')

class CursoListView( LoginRequiredMixin,ListView):
    model = Cursos
    context_object_name = 'cursos'
    template_name = 'cursos/listar.html'

class CursoDetailView(DetailView):
    model = Cursos
    template_name = 'cursos/curso_detalle.html'

class CursoCreateView(CreateView):
    model = Cursos
    template_name = 'cursos/curso_crear.html'
    success_url = reverse_lazy('ListarCursos')
    fields = ['nombre', 'camada']

class CursoUpdateView(UpdateView):
    model = Cursos
    template_name = 'cursos/curso_editar.html'
    success_url = reverse_lazy('ListarCursos')
    fields = ['nombre','camada']

class CursoDeleteView(DeleteView):
    model = Cursos
    template_name = 'cursos/curso_borrar.html'
    success_url = reverse_lazy('ListarCursos')


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