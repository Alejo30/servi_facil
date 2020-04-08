from django.contrib import admin
from django.urls import path, include
from serviFacilApp.views import inicio, registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/serviV1/', include('serviFacilApp.api')),
    path('inicio', inicio, name="inicio"),
    path('registrar', registro , name="registrarse"),
]
