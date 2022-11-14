from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """return a hello message"""
        a_viewset= [
            'uses actions (list, create , retrieve, update, partial_update)',
            'autoatcally maps to urls usning rotuters',
            'provides more functionality with less code',
        ]
        return Response({'message':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """create hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self , request, pk=None):
        """Handle Updating an object data """
        return Response({'http_method':'PUT'})


    def partial_update(self , request, pk=None):
        """Handle Updating part of an object"""
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authenication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES 


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating ,reading and updating profile feed itams"""
    authentication_classes = (TokenAuthentication)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfleFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus ,
        IsAuthenticatedOrReadOnly 
    )


    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
         

