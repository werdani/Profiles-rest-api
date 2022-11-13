from django.urls import path
from profiles_api import views

urlpatterns = [
    path('api-apiview',views.HelloApiView.as_view()), 

]