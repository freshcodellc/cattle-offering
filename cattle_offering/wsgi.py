"""
WSGI config for cattle_offering project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get('APP_ENV', 'local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cattle_offering.settings.{}'.format(env))

application = get_wsgi_application()
