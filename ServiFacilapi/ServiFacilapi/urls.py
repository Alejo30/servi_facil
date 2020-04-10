from django.contrib import admin
from django.urls import path, include
from serviFacilApp.views import inicio, registro, lista_personas, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/serviV1/', include('serviFacilApp.api')),
    path('lista_personas', lista_personas , name="list_personas"),
    path('login', login, name="login"),
    path('inicio', inicio, name="inicio"),
    path('registrar', registro , name="registrarse"),
]
