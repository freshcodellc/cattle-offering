#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    env = os.environ.get('APP_ENV', 'local')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'cattle_offering.settings.{}'.format(env))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
