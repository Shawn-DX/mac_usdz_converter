from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GLBFileViewSet

router = DefaultRouter()
router.register('', GLBFileViewSet, basename='glbfile')

urlpatterns = router.urls