from mce_django_server.settings import *

# FIXME:
ALLOWED_HOSTS = ["*"]

pg_config = env.db()
"""
pg_config.update({
    'ENGINE': 'django_db_geventpool.backends.postgresql_psycopg2', #'django.db.backends.postgresql_psycopg2'
    'ATOMIC_REQUESTS': False,
    'CONN_MAX_AGE': 0,
    'OPTIONS': { 
        'MAX_CONNS': 20 
    }
})
"""

DATABASES = {
    'default': pg_config,
}

CACHES = {
    'default': env.cache()
}

