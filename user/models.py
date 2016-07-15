from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
