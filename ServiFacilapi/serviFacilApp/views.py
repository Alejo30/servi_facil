from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import ListView
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios, Empresa, Servicio, Turno
from serviFacilApp.serializers import PersonaSerializer, TipoUserSerializer, UsuariosSerializer, EmpresaSerializer, ServicioSerializer, TurnoSerializer

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

class TipoViewSet(ModelViewSet):
    serializer_class = TipoUserSerializer
    queryset = TipoUser.objects.all()

class EmpresaViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()

class ServicioViewSet(ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()

class TurnoViewSet(ModelViewSet):
    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()


# Views de los templates.
def inicio(request):
    return render(request, 'Inicio.html',{
        'title': 'Inicio'
    })

def registro(request):
    return render(request, 'registrar.html',{
        'title': 'Registrarse'
    })

def login(request):
    return render(request, 'login.html',{
        'title': 'Login'
    })


