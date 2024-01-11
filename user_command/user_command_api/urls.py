from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, CommandViewSet


router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'command', CommandViewSet)

urlpatterns = [
   path('', include(router.urls)),
]
