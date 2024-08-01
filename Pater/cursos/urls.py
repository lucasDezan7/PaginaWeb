from django.urls import path
from cursos.views import *
from cursos.forms import forms


urlpatterns = [
    path('', inicio, name='inicio'),
    path('listar',CursoListView.as_view(), name='ListarCursos'),
    path('buscarCurso',busquedaCamada, name='buscarCurso'),    
    path('buscar/',buscar ),    
    path('addProfesores',profesorFormulario, name='Agregarprofesor'),    
    path('addestudiantes',estudiantesFormulario, name='Agregarestudiantes'),    
    path('profesor',ProfesoresListView.as_view(), name='profesores'),      
    path('estudiantes', EstudiantesListView.as_view(), name='estudiantes'),
    path('busquedaProfesor/',busquedaProfesor, name='buscarprofesores'),
    path('buscarr/',buscarProfesor),     
    path('curso/nuevo',CursoCreateView.as_view(), name='NuevoCurso'),     
    path('curso/<pk>',CursoDetailView.as_view(), name='DetalleCurso'),     
    path('curso/<pk>/editar',CursoUpdateView.as_view(), name='EditarCurso'),     
    path('curso/<pk>/borrar',CursoDeleteView.as_view(), name='BorrarCurso'),         
]
