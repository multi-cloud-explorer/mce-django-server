from mce_django_server.settings import *

"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
"""

ALLOWED_HOSTS = ["*"]

DEBUG = True

DATABASES = {
    'default': env.db(default='sqlite:////tmp/mce-django-app-dev-sqlite.db'),
}

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# TODO: env var
INTERNAL_IPS = [
    '127.0.0.1',
    '192.168.56.1',
]

