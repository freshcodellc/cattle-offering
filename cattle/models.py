from django.conf import settings
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Photo(models.Model):
    title = models.CharField(max_length=50)
    caption = models.CharField(max_length=100, null=True, blank=True)
    original_image = models.ImageField(upload_to='cattle_images/')
    large_image = ImageSpecField(processors=[ResizeToFit(1000, 600)])
    thumbnail = ImageSpecField(processors=[ResizeToFit(250, 250)],
                               source='original_image')
    cattle = models.ForeignKey('Cattle', related_name='photos')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Cattle(models.Model):
    # Breed Values
    ANGUS = 'angus'
    RED_ANGUS = 'red_angus'
    SIMMENTAL = 'simmental'
    SIMANGUS = 'simangus'
    SHORTHORN = 'shorthorn'
    CHAROLAIS = 'charolais'
    HEREFORD = 'hereford'
    BRAHMAN = 'brahman'
    BRANGUS = 'brangus'
    LIMOUSIN = 'limousin'
    LIMFLEX = 'limflex'

    BREEDS = (
        (ANGUS, 'Angus'),
        (RED_ANGUS, 'Red Angus'),
        (SIMMENTAL, 'Simmental'),
        (SIMANGUS, 'SimAngus'),
        (SHORTHORN, 'Shorthorn'),
        (CHAROLAIS, 'Charolais'),
        (HEREFORD, 'Hereford'),
        (BRAHMAN, 'Brahman'),
        (BRANGUS, 'Brangus'),
        (LIMOUSIN, 'Limousin'),
        (LIMFLEX, 'LimFlex'),
    )

    # Sex Values
    BULL = 'bull'
    FEMALE = 'female'

    SEXES = (
        (BULL, 'Bull'),
        (FEMALE, 'Female'),
    )

    # Female Type Values
    COW = 'cow'
    REPLACEMENT_HEIFER = 'replacement_heifer'
    BRED_HEIFER = 'bred_heifer'
    PAIR = 'pair'

    FEMALE_TYPES = (
        (COW, 'Cow'),
        (REPLACEMENT_HEIFER, 'Replacement Heifer'),
        (BRED_HEIFER, 'Bred Heifer'),
        (PAIR, 'Pair'),
    )

    producer = models.ForeignKey(settings.AUTH_USER_MODEL)
    lot_number = models.IntegerField()
    breed = models.CharField(max_length=25, choices=BREEDS)
    sex = models.CharField(max_length=25, choices=SEXES)
    female_type = models.CharField(max_length=25, choices=FEMALE_TYPES, null=True, blank=True)
    registration_number = models.CharField(max_length=25)
    bull_name = models.CharField(max_length=55)
    sire = models.CharField(max_length=55)
    dame = models.CharField(max_length=55)
    scrotal_circumference = models.DecimalField(max_digits=3, decimal_places=2)
    birth_weight = models.DecimalField(max_digits=3, decimal_places=2)
    weaning_weight = models.IntegerField()
    yearling_weight = models.IntegerField()
    residual_average_daily_gain = models.DecimalField(max_digits=2, decimal_places=2)
    heifer_pregnancy = models.DecimalField(max_digits=3, decimal_places=1)
    calving_ease_maternal = models.IntegerField()
    maternal_milk = models.IntegerField()
    mature_weight = models.IntegerField()
    mature_height = models.DecimalField(max_digits=2, decimal_places=1)
    cow_energy_value = models.DecimalField(max_digits=4, decimal_places=2)
    carcass_weight = models.IntegerField()
    marbling = models.DecimalField(max_digits=3, decimal_places=2)
    ribeye_area = models.DecimalField(max_digits=3, decimal_places=2)
    fat_thickness = models.DecimalField(max_digits=3, decimal_places=3)
    video_url = models.URLField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bull_name

    class Meta:
        unique_together = ('producer', 'bull_name')
        verbose_name_plural = 'cattle'
