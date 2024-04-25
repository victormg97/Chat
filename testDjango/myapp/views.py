from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("¡Hola, mundo! Esta es mi primera vista en Django.")
