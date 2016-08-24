from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models

from localflavor.us.models import PhoneNumberField, USStateField, USZipCodeField
import mailchimp

from cattle_offering.utils import get_mailchimp_api
from cattle.models import Cattle


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
        user.is_superuser = True
        user.type = 'admin'
        user.newsletter = False
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    BUYER = 'buyer'
    PRODUCER = 'producer'
    ADMIN = 'admin'

    USER_TYPES = (
        (BUYER, 'Buyer'),
        (PRODUCER, 'Producer'),
        (ADMIN, 'Admin'),
    )

    name = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip = USZipCodeField(null=True, blank=True)
    newsletter = models.BooleanField(default=True)
    type = models.CharField(max_length=15, choices=USER_TYPES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    watch_list = models.ManyToManyField(Cattle, related_name='watchers')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def add_email_to_mailing_list(self):
        if self.email and self.name:
            try:
                m = get_mailchimp_api()
                response = m.lists.subscribe(settings.MAILCHIMP_LIST_ID,
                                             {'email': self.email},
                                             {'EMAIL': self.email, 'NAME': self.name},
                                             'html',
                                             False)
                return response
            except mailchimp.Error as e:
                print('An error occurred: %s - %s' % (e.__class__, e))
                return False
        else:
            return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
