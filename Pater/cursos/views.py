from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView
from cursos.models import Cursos, Profesor, Estudiantes
from cursos.forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):
    return render(request,'cursos/inicio.html')

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


def busquedaCamada(request):
    return render(request, 'cursos/buscarCurso.html')

def busquedaProfesor(request):
    return render(request, 'cursos/buscarProfesor.html')

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        cursos = Cursos.objects.filter(nombre__icontains = nombre)

        return render(request, 'cursos/buscar.html', {'cursos':cursos, 'nombre':nombre})
    else:
        request = 'no enviaste datos'
    return HttpResponse(request)

def buscarProfesor(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        profesor = Profesor.objects.filter(nombre__icontains = nombre)

        return render(request, 'cursos/buscarr.html', {'profesor':profesor, 'nombre':nombre})
    else:
        request = 'no enviaste datos'
    return HttpResponse(request)



def profesorFormulario(request):

    if request.method == 'POST':

        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            profesor.save()
            return render(request, 'cursos/profesores.html')
    else:
        miFormulario = ProfesorFormulario()
    
    return render(request, 'cursos/agregarprofesor.html',{"miFormulario":miFormulario})

def estudiantesFormulario(request):

    if request.method == 'POST':

        miFormulario = EstudiantesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'], mail=informacion['mail'])
            profesor.save()
            return render(request, 'cursos/estudiantes.html')
    else:
        miFormulario = EstudiantesFormulario()
    
    return render(request, 'cursos/agregarestudiantes.html',{"miFormulario":miFormulario})