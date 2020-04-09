from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios
from serviFacilApp.serializers import PersonaSerializer, TipoUserSerializer, UsuariosSerializer

# Views en general

def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'list_personas.html',{
        'title': 'Personas Registradas',
        'personas': personas
    })

#Views Set
class PersonasViewsSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()

class UsuarioViewsSet(ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()

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
    serializer_class = TipoUserSerializer
    queryset = TipoUser.objects.all()
