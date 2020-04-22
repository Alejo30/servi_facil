from django import forms
from django.contrib.auth.models import User
from usuarios.models import Profile


class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(min_length=6,max_length=70, widget=forms.EmailInput())

    def clean_username(self):
        """El usuario tiene que ser unico"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El nombre de Usuario ya esta en uso')
        return username
    
    def clean(self):
        """Verrificar los password - password confirmation"""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las Passwords no son iguales')
        return data
    
    def save(self):
        """Creando Usuario y el Perfil al mismo tiempo"""
        data = self.cleaned_data 
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()