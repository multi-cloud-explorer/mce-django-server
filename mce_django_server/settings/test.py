from mce_django_server.settings import *

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'db.sqlite3'),
    }
}
"""

# TODO:
pg_config = env.db()
DATABASES = {
    'default': pg_config,
}



