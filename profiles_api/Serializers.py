from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name = serializers.CharField(max_length=15) 
    # email = serializers.CharField(max_length=15) 


# extra functionality which makes it really easy to work wiht exinting djngo modle .
# modelserializer that define a meta class the way that you work with model.
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password') 
        # to don't retreive the password hash that make the password field write only.
        extra_kwargs ={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}

            }
        }
    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user( # that will override function in model 
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user # that is a new user it is created .

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
 
        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""   

    class Meta:
        modle = models.ProfleFeedItem
        fields = ('id','user_profile','status_text','created_on')
        # this allow us to set the user profile field to read only
        extra_kwargs = {'user_profile':{'read_only':True}}
         
