from django.http import HttpResponse
from django.template import Template, Context, loader
from appFamilia.models import *

def inicio(request):
    archivo = open(r"C:\Users\Mostro\Documents\Proyecto\Familia\Familia\templates\inicio.html")

    plantilla = Template(archivo.read())

    archivo.close()

    contexto = Context({"objs": Familiar.objects.all()})

    documento = plantilla.render(contexto)

    return HttpResponse(documento)


