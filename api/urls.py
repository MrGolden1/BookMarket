
from django.urls import path, include
from rest_framework import routers

from .views import BookViewSet, CustomUserViewSet, CartViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'user', CustomUserViewSet)
router.register(r'cart', CartViewSet)
router.register(r'item', ItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]