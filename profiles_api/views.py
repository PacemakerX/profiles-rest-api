from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api import serializers
from rest_framework import filters

from profiles_api import models
from profiles_api import permissions

class GenericAPIView(APIView):
    """A generic API view that can be extended for various purposes."""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Handle GET requests."""
        
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "Mapped manually to URLs"
        ]
        return Response({"message": "This is a generic GET response", "an_apiview": an_apiview})

    def post(self, request):
        """Create POST request with our name."""
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object."""
        return Response({"message": "PUT method called"})

    def patch(self, request, pk=None):
        """Handle partial update of an object."""
        return Response({"message": "PATCH method called"})

    def delete(self, request, pk=None):
        """Handle deletion of an object."""
        return Response({"message": "DELETE method called"}, status=status.HTTP_204_NO_CONTENT)

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """Return a hello message."""
        
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using routers",
            "Provides more functionality with less code"
        ]
        return Response({"message": "This is a ViewSet", "a_viewset": a_viewset})
    
    def create(self,request):
       """ Crea a new hello message """
       serializer = self.serializer_class(data=request.data)

       if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})
       else:
           return Response(
               serializer.errors,
               status=status.HTTP_400_BAD_REQUEST
           )
           
    def retrieve(self,reques,pk=None):
        """Handle getting and object by its ID"""
        return Response({'http_method':'GET'})
    
    def update(self,reques,pk=None):
        """Handle updating and Objecty"""
        return Response({'http_reques':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Handle updating part of an objec"""
        return Response({'http_reques':'PATCH'})
    
    def destroy(self,request,pk=None):
        """Handle destory of an object"""
        return Response({'http_method':'Delete'})
            
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email')
    