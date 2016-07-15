"""
Local Configuration Settings.
"""
from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cattle_offering',
        'USER': 'cattle_offering',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEBUG = True

# Celery Broker
BROKER_URL = 'django://'
