"""Views de Usuarios"""
#Django
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
#Forms
from usuarios.forms import SignupForm
#Modelo
from django.contrib.auth.models import User
from usuarios.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """Detalle de Usuario"""
    template_name = 'usuarios/perfil.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Vista basada en clase para actualizar el perfil"""
    template_name = 'usuarios/update_profile.html'
    model = Profile
    fields = ['phone_number', 'picture']

    def get_object(self):
        """Regresa el perfil del usurio"""
        return self.request.user.profile
    
    def get_success_url(self):
        username= self.object.user.username
        return reverse('users:detail', kwargs={'username': username})



class SignupView(FormView):
    """Formulario de Registro"""
    template_name = 'usuarios/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Guardar"""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login"""
    template_name = 'usuarios/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'usuarios/logged_out.html'
