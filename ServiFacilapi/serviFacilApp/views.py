from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios
from serviFacilApp.serializers import PersonaSerializer


# Views de los templates.
def inicio(request):
    return render(request, 'Inicio.html',{
        'title': 'Inicio'
    })

def registro(request):
    return render(request, 'registrar.html',{
        'title': 'Registrarse'
    })

# Views en general

class PersonasViewSet(ModelViewSet):
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
 