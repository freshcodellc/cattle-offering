"""
Local Configuration Settings.
"""
from .common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'HOST': '',
        'PORT': 5432,
    }
}

DEBUG = False

# Mailchimp - API_KEY is production and LIST_ID is a test list ID
MAILCHIMP_API_KEY = '6c1e85312a1322f32d7c5752e34a8f0f-us12'
MAILCHIMP_LIST_ID = 'cf0a31c843'
