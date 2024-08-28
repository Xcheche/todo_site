from django.db import models
from django.contrib.auth.models import AbstractUser

from config import settings

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    if  'auth' in settings.INSTALLED_APPS:
        AUTH_USER_MODEL = 'auth.User'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
