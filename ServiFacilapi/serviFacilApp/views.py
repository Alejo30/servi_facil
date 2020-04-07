from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios


# Create your views here.


def inicio(request):
    return render(request, 'Inicio.html',{
        'title': 'Inicio'
    })

def registro(request):
    return render(request, 'registrar.html',{
        'title': 'Registrarse'
    })
