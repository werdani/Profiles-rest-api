from django.urls import path, include
from profiles_api import views
# that is for viewsets .
from rest_framework.routers import DefaultRouter

# that is for viewsets .
router =DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')
router.register('profile-viewset',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('api-apiview',views.HelloApiView.as_view()), 
    path('login/',views.UserLoginApiView.as_view()), 
    # that is for viewsets .       
    path('api-viewsets',include(router.urls)), 

]