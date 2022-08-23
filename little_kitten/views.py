from django.http import HttpResponse 
from django.template import Template, Context
from datetime import datetime, timedelta


def saludo(request):
    return HttpResponse("Hola people")


def segunda_vista(request):
    return HttpResponse("<b>Juju soy un capo</b>")


def dia(request):
    feira = datetime.now()
    texto = f"Hoy es día: <br> {feira} "
    return HttpResponse(texto)


def my_name(request, nombre):
    texto = f"Mi nombre es: <br><br>  {nombre}"
    return HttpResponse(texto)


def age(request, edad):
    hoy = datetime.now()
    anio_nascimiento= hoy- timedelta(days=edad*365)
    texto = f"Naciste aproximadamente en: <br> {anio_nascimiento.year}"
    return HttpResponse(texto)