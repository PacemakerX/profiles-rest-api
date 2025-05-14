from django.urls import path
from .views import GenericAPIView

urlpatterns = [
    path('generic/', GenericAPIView.as_view(), name='generic-api'),
]