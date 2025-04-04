from django.urls import path
from . import views

urlpatterns = [
    path('peliculas/', views.listado_peliculas, name='listado_peliculas'),
    path('salas/',views.listado_salas, name='listado_salas')
]
