from email.policy import default
from django.db import models
from django.conf import settings


# AbstractBaseUser >>  that is abstract baseuser from django .
# PermissionsMixin >>  for django defult user to overied it .
'''these are the standard base class that you need to use when overriding or 
 customizing the default django user model.'''
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin ,BaseUserManager


# Create your models here.
# to add super user .
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
 
    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email) #normalize_email >> that will convert email after '@' to lower case.
        user = self.model(email=email, name=name)
        #set_password >> the password is encrypted we want to make sure the password is converted to a hash .
        user.set_password(password) 
        user.save(using=self._db) #to specify the database that wants to use .
        return user

    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db) #to specify the database that wants to use
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # that will overide the objects and call the userprofilemanager class like query selector. 
    objects = UserProfileManager() 

    # to customize username field and set email .
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name'] # to set name is required field .

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve shrot name of user"""
        return self.name

    def __str__(self):
        """Return string represntation of our user"""
        return self.email


class ProfleFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text
