from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.template import loader
from .models import Pregunta
# Create your views here.


from django.http import HttpResponse


def index(request):
    Preguntas =Pregunta.objects.all()
    template =loader.get_template('foro/index.html')
    context={
        'Preguntas': Preguntas,
    }

    return HttpResponse(template.render(context,request))


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def detail(request, Pregunta_id):
    return HttpResponse("You're looking at question %s." % Pregunta_id)

def results(request, Pregunta_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % Pregunta_id)
