from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import Serializers


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = Serializers.HelloSerializer

    def get(self, request, format=None):
        """Returbs a list of APIView features"""
        an_apiview = [
            'user http methods as funtion (get, post, patch, put, delete)',
            'is similar to a traditional django view',
            'is mapped manually to urls',
            'welcom ammar yasser'
        ]

        return Response({'message': 'Hello','an_apiview':an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        """Handle updating an object"""
        return Response({'message':'put'})

    def patch(self, request):
        """Handle a partial update of an object"""
        return Response({'message':'patch'})

    def delete(self, request,pk=None):
        """Delete an object"""
        return Response({'method':'delete'})
