from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from serviFacilApp.views import inicio, registro, lista_personas, login, UsuarioCreate,\
    EmpresaCreate, ServicioCreate, TurnoCreate, EmpresaList, EmpresaUpdate, EmpresaDelete,\
    ServicioUpdate, ServicioDelete, ServicioList, TurnoUpdate, TurnoDelete, TurnoList
from django.conf.urls.static import static
from django.conf import settings
"""Importacion de Vistas de Usuarios"""


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name="inicio"),
    path('users/', include(('usuarios.urls', 'users'), namespace='users')),

    path('api/serviV1/', include('serviFacilApp.api')),
    path('lista_personas', lista_personas , name="list_personas"),
    path('registrar', registro , name="registrarse"),
    path('usuario/registro', UsuarioCreate.as_view(), name='usuario_crear'),
    #path('login', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('empresa/crear', EmpresaCreate.as_view(), name='empresa_crear'),
    path('empresa/lista', EmpresaList.as_view(), name='empresa_lista'),
    path('empresa/editar/<pk>', EmpresaUpdate.as_view(), name='empresa_editar'),
    path('empresa/elimiar/<pk>', EmpresaDelete.as_view(), name='empresa_eliminar'),
    path('servicio/crear', ServicioCreate.as_view(), name='servicio_crear'),
    path('servicio/editar/<pk>', ServicioUpdate.as_view(), name='servicio_editar'),
    path('servicio/eliminar/<pk>', ServicioDelete.as_view(), name='servicio_eliminar'),
    path('servicio/lista', ServicioList.as_view(), name='servicio_lista'),
    path('turno/crear', TurnoCreate.as_view(), name='turno_crear'),
    path('turno/editar/<pk>', TurnoUpdate.as_view(), name='turno_editar'),
    path('turno/eliminar/<pk>', TurnoDelete.as_view(), name='turno_eliminar'),
    path('turno/lista', TurnoList.as_view(), name='turno_lista'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)