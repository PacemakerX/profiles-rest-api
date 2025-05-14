from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

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
