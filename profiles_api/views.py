from rest_framework.views import APIView
from rest_framework.response import Response

class GenericAPIView(APIView):
    """A generic API view that can be extended for various purposes."""
    
    def get(self, request, format=None):
        """Handle GET requests."""
        
        an_apiview= [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django view",
            "Gives you the most control over your logic",
            "Mapped manually to URLs"
        ]
        return Response({"message": "This is a generic GET response", "an_apiview": an_apiview})

    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        return Response({"message": "This is a generic POST response", "data": request.data})