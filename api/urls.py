
from django.urls import path, include
from rest_framework import routers

from .views import BookViewSet, CustomUserViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'user', CustomUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]