"""Views de Usuarios"""
#Django
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#Expetions
from django.db.utils import IntegrityError
#Modelo
from django.contrib.auth.models import User
from usuarios.models import Profile

def login_view(request):
    """Login View"""
    """Esto es para iniciar sesion"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Invalid username and password'})
    return render (request, 'usuarios/login.html')

def signup(request):
    """Sign-up view"""
    if request.method == 'POST':
        username =  request.POST['username']
        passwd =  request.POST['passwd']
        passwd_confirmation =  request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
             return render(request, 'usuarios/signup.html', {'error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
             return render(request, 'usuarios/signup.html', {'error': 'Username is already in user'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.tipo_ususario = request.POST['tipo_ususario']

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'usuarios/signup.html')


@login_required
def logout_view(request):
    """Esto es para cerrar sesion"""
    logout(request)
    return redirect('login')