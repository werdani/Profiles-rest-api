from email.policy import default
from django.db import models
# AbstractBaseUser >>  that is abstract baseuser from django .
# permission >>  for django defult user to overied it .
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    #objects = UserProfileManager()

    # to customize username field and set email 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # to set name is required field 

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shrot name of user"""
        return self.name

    def __str__(self):
        """Return string represntation of our user"""
        return self.email


       