from .views import LocationViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LocationViewSet, base_name='location')
urlpatterns = router.urls

