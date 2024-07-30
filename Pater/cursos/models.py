from django.db import models

# Create your models here.
class Cursos(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField(max_length=40)

    def __str__(self):
        return self.nombre
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField(max_length=40)

class Entregables(models.Model):
    nombre = models.CharField(max_length=40)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()   

