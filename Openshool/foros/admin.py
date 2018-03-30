from django.contrib import admin

# Register your models here.
from .models import Pregunta
from .models import Articulo

admin.site.register(Pregunta)
admin.site.register(Articulo)
