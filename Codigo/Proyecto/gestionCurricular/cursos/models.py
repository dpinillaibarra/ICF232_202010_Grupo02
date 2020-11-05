from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import validate_file_extension

class Curso:
    def __init__(self, sigla, nombre):
        self.sigla = sigla
        self.nombre = nombre

class CursoFactory:
    def __init__(self):
        self.cursos = []
        self.cursos.append(Curso("ICF333", "Repositorio: Proyecto Titulo I "))

    def obtenerCursos(self):
        return self.cursos

    def getCurso(self, sigla):
        for curso in self.cursos:
            if curso.sigla == sigla:
                return curso
        return None

class MDocumento(models.Model):
    titulo = models.CharField(max_length=100)
    documento = models.FileField(upload_to='media/', blank=True, null=True, validators=[validate_file_extension])
    comentario = models.TextField(max_length=250, blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class MRubrica(models.Model):
    titulo = models.CharField(max_length=100)
    rubrica = models.FileField(upload_to='rubricas/', blank=True, null=True,validators=[validate_file_extension])
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Descripcion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=400, blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=150, blank=True, null=True)
    exigencia = models.IntegerField(verbose_name="Exigencia")
    nota = models.IntegerField(verbose_name="Nota")
    promedio = models.FloatField(verbose_name="Promedio", default=0)

    def __str__(self):
        return self.nombre

