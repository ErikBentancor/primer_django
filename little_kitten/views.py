from django.http import HttpResponse 
from django.template import Template, Context, loader
from datetime import datetime, timedelta

def saludo(request):
    return HttpResponse("Hola")

1
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


def probar_template_legacy(request):
    with open('C:/Users/Erik/Desktop/Erik/Continuacion/primer_django/little_kitten/plantillas/planilla1.html') as archivo: #copiar el relative path
        #Crear la plantilla en memoria
        plantilla = Template(archivo.read()) #Pasamos como argumento el contennido del HTML
    diccionario = {"nombre": "Erik", "apellido": "Bnt", "lista_de_notas": [10,5,6,5,6]}

    contexto = Context(diccionario) #contexto va a estar vacio
    
    texto_html = plantilla.render(contexto)

    return HttpResponse(texto_html)

def probar_template(request):
  
    diccionario = {"nombre": "Maira", "apellido": "Jaque Rolon", "lista_de_notas": [10,5,6,5,6]}

    plantilla= loader.get_template('planilla1.html')

    texto_html = plantilla.render(diccionario)

    return HttpResponse(texto_html)

def template_amor(request):

    diccionario = {"nombre": "Maira", "apellido": "Jaque Rolon", "lista_de_notas": [10,5,8,8,8]}

    plantilla= loader.get_template('planilla2.html')

    texto_html = plantilla.render(diccionario)

    return HttpResponse(texto_html)