from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser # this is the default django user model
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    ''' this has to be updated as superuser creation function now requires an email but no superuser name (ex: "admin")'''
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractUser): # all default User attributes

    ''' Force identification by e-mail adress '''
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()  # Link the custom manager

