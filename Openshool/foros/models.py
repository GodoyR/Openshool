from django.db import models

# Create your models here.
from django.db import models


class Pregunta(models.Model):
    Texto_Pregunta = models.CharField(max_length=200)
    Fecha_Publicacion = models.DateTimeField('date published')
    Estado = models.BooleanField()


class Articulo(models.Model):
    Pdf_articulo = models.FileField(max_length=200)
    Titulo = models.CharField(max_length=200)


class Respuesta_Pregunta(models.Model):
    Pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    Texto_Respuesta = models.CharField(max_length=200)

class Comentario_Articulo(models.Model):
    Articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    Texto_Respuesta = models.CharField(max_length=200)
