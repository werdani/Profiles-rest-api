from django.urls import path, include
from profiles_api import views
# that is for viewsets .
from rest_framework.routers import DefaultRouter

# that is for viewsets .
router =DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

urlpatterns = [
    path('api-apiview',views.HelloApiView.as_view()), 
    # that is for viewsets .       
    path('api-viewsets',include(router.urls)), 

]