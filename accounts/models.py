from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    REQUIRED_FIELDS = ['first_name', 'last_name']
    def __str__(self):
        return self.username