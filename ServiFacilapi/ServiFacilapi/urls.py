from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from serviFacilApp.views import inicio, registro, lista_personas, login, UsuarioCreate, EmpresaCreate, ServicioCreate, TurnoCreate, EmpresaList, EmpresaUpdate, EmpresaDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/serviV1/', include('serviFacilApp.api')),
    path('lista_personas', lista_personas , name="list_personas"),
    #path('login', login, name="login"),
    path('inicio', inicio, name="inicio"),
    path('registrar', registro , name="registrarse"),
    path('usuario/registro', UsuarioCreate.as_view(), name='usuario_crear'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('empresa/registro', EmpresaCreate.as_view(), name='empresa_crear'),
    path('servicio/crear', ServicioCreate.as_view(), name='servicio_crear'),
    path('turno/crear', TurnoCreate.as_view(), name='turno_crear'),
    path('empresa/lista', EmpresaList.as_view(), name='empresa_lista'),
    path('empresa/editar/<pk>', EmpresaUpdate.as_view(), name='empresa_editar'),
    path('empresa/elimiar/<pk>', EmpresaDelete.as_view(), name='empresa_eliminar')
]
