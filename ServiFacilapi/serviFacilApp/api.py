from rest_framework import routers
from .views import PersonasViewsSet

router = routers.DefaultRouter()

router.register(r'personas', PersonasViewsSet)

urlpatterns = router.urls