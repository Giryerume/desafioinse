from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import InseViewSet

router = DefaultRouter()
router.register(r'inses', InseViewSet, basename='inse')
urlpatterns = router.urls
