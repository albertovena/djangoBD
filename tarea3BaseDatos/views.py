from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Peliculas
from .models import Salas

def listado_peliculas(request):
    peliculas = Peliculas.objects.all()  # Obtiene todos los productos de la base de datos
    return render(request, 'tarea3BaseDatos/listado_peliculas.html', {'peliculas': peliculas})

def listado_salas(request):
    salas = Salas.objects.all()
    return render(request,'tarea3BaseDatos/listado_salas.html',{'salas':salas})
