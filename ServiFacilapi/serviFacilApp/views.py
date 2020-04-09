from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios
from serviFacilApp.serializers import PersonaSerializer

# Views en general

class PersonasViewsSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

# Views de los templates.
def inicio(request):
    return render(request, 'Inicio.html',{
        'title': 'Inicio'
    })

def registro(request):
    return render(request, 'registrar.html',{
        'title': 'Registrarse'
    })


class TipoViewSet(ModelViewSet):
    serializer_class = TipoUser
    queryset = TipoUser.objects.all()
