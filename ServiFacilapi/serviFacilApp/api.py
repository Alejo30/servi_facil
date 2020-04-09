from rest_framework import routers
from .views import PersonasViewsSet, TipoViewSet

router = routers.DefaultRouter()

router.register(r'personas', PersonasViewsSet)
router.register(r'tipo', TipoViewSet)

urlpatterns = router.urls