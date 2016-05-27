from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email,password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        if not kwargs.get('username'):
            raise ValueError('Users must have a valid username.')

        if not kwargs.get('first_name'):
            raise ValueError('Users must have a valid forename.')

        if not kwargs.get('last_name'):
            raise ValueError('Users must have a valid surname.')

        user = self.model(
            email=self.normalize_email(email), username=kwargs.get('username'),
            first_name=kwargs.get('first_name'), last_name=kwargs.get('last_name')
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, **kwargs)

        user.is_admin = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255) #Needs to be unique for login
    username = models.CharField(max_length=35, unique=True) #Needs to be unique for URL

    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)

    is_admin = models.BooleanField(default=False) # Are they an admin?
    created_at = models.DateTimeField(auto_now_add=True, editable=False) #When object was created
    updated_at = models.DateTimeField(auto_now=True) #When object was last updated

    objects = UserManager()

    USERNAME_FIELD = 'email' #Djangos built in user requires a username. This is used to log in the user.
    REQUIRED_FIELDS = ['username'] #uses username in URL so we must have it.

    def __str__(self):
        return self.username

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

def get_anonymous_user_instance(User):
    return User(username='Anonymous',
                first_name='Anonymous',
                last_name='User')
