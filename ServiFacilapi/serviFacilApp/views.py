from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import PersonaForm, UsuarioForm, EmpresaForm, ServicioForm, TurnoForm
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios, Empresa, Servicio, Turno
from serviFacilApp.serializers import PersonaSerializer, TipoUserSerializer, UsuariosSerializer,\
    EmpresaSerializer, ServicioSerializer, TurnoSerializer
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
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



#Vista Basadas en Clases Create
class UsuarioCreate(CreateView):
    model = Usuarios
    template_name = 'crear_usuario_form.html'
    form_class = UsuarioForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('inicio')

    def get_context_data(self, **kwargs):
        context = super(UsuarioCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            usuario = form.save(commit=False)
            usuario.persona = form2.save()
            usuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'crear_empresa_form.html'
    success_url = reverse_lazy('empresa_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))
class ServicioCreate(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'crear_servicio_form.html'
    success_url = reverse_lazy('servicio_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class TurnoCreate(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'crear_turno_form.html'
    success_url = reverse_lazy('turno_lista')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

#Vista Basadas en Clases List
class EmpresaList(ListView):
    model = Empresa
    template_name = 'empresa_list.html'

class ServicioList(ListView):
    model = Servicio
    template_name = 'servicio_list.html'

class TurnoList(ListView):
    model = Turno
    template_name = 'turno_list.html'

class EmpresaUpdate(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'crear_empresa_form.html'
    success_url = reverse_lazy('empresa_lista')

class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'crear_servicio_form.html'
    success_url = reverse_lazy('servicio_lista')

class TurnoUpdate(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'crear_turno_form.html'
    success_url = reverse_lazy('turno_lista')

class EmpresaDelete(DeleteView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'empresa_delete.html'
    success_url = reverse_lazy('empresa_lista')

class ServicioDelete(DeleteView):
    model = Servicio
    form_class = ServicioForm
    template_name = 'servicio_delete.html'
    success_url = reverse_lazy('servicio_lista')

class TurnoDelete(DeleteView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno_delete.html'
    success_url = reverse_lazy('turno_lista')