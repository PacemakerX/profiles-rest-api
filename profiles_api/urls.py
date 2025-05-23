from django.urls import path,include
from .views import GenericAPIView,HelloViewSet,UserProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile',UserProfileViewSet,)
urlpatterns = [
    path('', include(router.urls)),
    path('generic/', GenericAPIView.as_view(), name='generic-api'),
]