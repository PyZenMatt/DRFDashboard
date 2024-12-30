from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet, basename='documents')
router.register(r'profiles', ProfileViewSet, basename='profiles')

urlpatterns = router.urls
