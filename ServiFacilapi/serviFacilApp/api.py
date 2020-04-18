from rest_framework import routers
from .views import PersonasViewsSet, TipoViewSet, UsuarioViewsSet, EmpresaViewSet, ServicioViewSet, TurnoViewSet

router = routers.DefaultRouter()

router.register(r'personas', PersonasViewsSet)
router.register(r'usuarios', UsuarioViewsSet)
router.register(r'tipo', TipoViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'servicio', ServicioViewSet)
router.register(r'turno', TurnoViewSet)


urlpatterns = router.urls