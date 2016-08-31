SITE = 'cattle_offering'
SITE_ALT = 'cattle-offering'

command = '/opt/{0}/bin/gunicorn'.format(SITE)
pythonpath = '/opt/{0}/{1}'.format(SITE, SITE_ALT)
bind = '127.0.0.1:8002'

preload_app = True
workers = 6
