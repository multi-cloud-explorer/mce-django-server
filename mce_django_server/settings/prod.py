from mce_django_server.settings import *

# FIXME:
ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': env.db(default='DATABASE_URL=postgres://mce:password@127.0.0.1:5432/mce')
}

# TODO:
#CACHES = {
#    'default': env.cache()
#}

