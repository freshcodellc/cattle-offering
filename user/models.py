from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models

from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.type = 'admin'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('buyer', 'Buyer'),
        ('producer', 'Producer'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    phone = PhoneNumberField()
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=70)
    state = USStateField()
    zip = USZipCodeField()
    type = models.CharField(max_length=15, choices=USER_TYPES)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
