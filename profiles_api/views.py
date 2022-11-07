from rest_framework.views import APIView
from rest_framework.response import Response




class HelloApiView(APIView):
    """Test api view"""

    def get(self, request, format=None):
        """Returbs a list of APIView features"""
        an_apiview = [
            'user http methods as funtion (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'is mapped manually to urls',
            'welcom ammar yasser'
        ]

        return Response({'message': 'Hello','an_apiview':an_apiview})