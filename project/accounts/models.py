from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models

import string, random

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class UserManager(BaseUserManager):
    def create_user(self, email,password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')

        user = self.model(
            email=self.normalize_email(email),
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
    key = models.CharField(max_length=6, unique=True, db_index=True)
    email = models.EmailField(unique=True, max_length=255) #Needs to be unique for login
    is_admin = models.BooleanField(default=False) # Are they an admin?

    created_at = models.DateTimeField(auto_now_add=True, editable=False) #When object was created
    updated_at = models.DateTimeField(auto_now=True) #When object was last updated

    objects = UserManager()

    USERNAME_FIELD = 'email' #Djangos built in user requires a username. This is used to log in the user.

    def __str__(self):
        return self.email

    def save(self, **kwargs):
        if not self.key:
            # Generate ID once, then check the db. If exists, keep trying.
            self.key = id_generator()
            while User.objects.filter(key=self.key).exists():
                self.key = id_generator()
        super(User, self).save()
