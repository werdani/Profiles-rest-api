from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

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

    def put(self,request, pk=None):
        """Handle updating an object"""
        return Response({'message':'put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'message':'patch'})

    def delete(self, request,pk=None):
        """Delete an object"""
        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    def list(self, request):
        """return a hello message"""
        a_viewset= [
            'uses actions (list, create , retrieve, update, partial_update)',
            'autoatcally maps to urls usning rotuters',
            'provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})
