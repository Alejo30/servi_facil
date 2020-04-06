from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    return render(request, 'Inicio.html',{
        'title': 'Inicio'
    })

def registro(request):
    return render(request, 'registrar.html',{
        'title': 'Registrarse'
    })
