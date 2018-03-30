#para conectarse a los temnplates mas facil y el codigo sea mas limpio
from django.shortcuts import render

from django.conf import settings
#
from django.core.files.storage import FileSystemStorage
#impoorta la tabla pregunta
from .models import Pregunta

# Create your views here.
#libreria que manda errores si pasan cosas que no esperamos
#es para ser try cath
from django.http import Http404
from django.http import HttpResponse


def index(request):
    Preguntas =Pregunta.objects.all()
    return render(request,'foro/index.html',{'Preguntas': Preguntas})





def detail(request, Pregunta_id):
    try:
        P = Pregunta.objects.get(pk=Pregunta_id)
    except Pregunta.DoesNotExist:
        raise Http404("No existe tu Pregunta")
    return render(request,'foro/detail.html',{'P': P})




def results(request, Pregunta_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % Pregunta_id)
