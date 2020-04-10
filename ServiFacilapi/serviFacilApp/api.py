from rest_framework import routers
from .views import PersonasViewsSet, TipoViewSet, UsuarioViewsSet

router = routers.DefaultRouter()

router.register(r'personas', PersonasViewsSet)
router.register(r'usuarios', UsuarioViewsSet)
router.register(r'tipo', TipoViewSet)

urlpatterns = router.urls