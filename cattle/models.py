from django.db import models

from user.models import User


class Cattle(models.Model):
    """
    Cattle model
    """
    MALE = 'M'
    FEMALE = 'F'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    producer = models.ForeignKey(User)
    zip = models.CharField(max_length=5)
    lot_num = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=GENDERS)
