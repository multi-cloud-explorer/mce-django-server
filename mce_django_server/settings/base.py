import os
import tempfile

import environ
from django.utils.translation import gettext_lazy as _

env = environ.Env(DEBUG=(bool, False))

try:
    environ.Env.read_env(env.str('ENV_PATH', '.env'))
except:
    pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))

SECRET_KEY = env('MCE_SECRET_KEY', default='fa(=utzixi05twa3j*v$eaccuyq)!-_c-8=sr#hih^7i&xcw)^')

DEBUG = env('MCE_DEBUG', default=False, cast=bool)

ROLLBAR_ENABLE = env('MCE_ROLLBAR_ENABLE', default=False, cast=bool)

ROLLBAR_TOKEN = env('MCE_ROLLBAR_TOKEN', default=None)

#ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'material.admin',
    'material.admin.default',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
    'django.contrib.humanize',

    'django_select2',
    'django_filters',
    'crispy_forms',

    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'drf_yasg',
    'corsheaders',

    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',

    'django_rq',
    'mce_tasks_rq',
    'mce_django_app',
]

if DEBUG:
    INSTALLED_APPS.append('django.contrib.admindocs')

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mce_django_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ])
            ],
        },
    },
]

WSGI_APPLICATION = 'mce_django_server.wsgi.application'

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#        'LOCATION': 'unique-snowflake',
#    }
#}
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        #"OPTIONS": {
        #    "CLIENT_CLASS": "django_redis.client.DefaultClient",
        #}
    },
}

AUTH_USER_MODEL = 'mce_django_app.User'

LOGIN_URL = 'admin:login'
#LOGIN_URL = '/accounts/login/'
#LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    #'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'), )

LANGUAGES = [
  ('fr', _('Français')),
  ('en', _('Anglais')),
]

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

USE_TZ = True

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    ('mce-server', os.path.join(BASE_DIR, 'project_static'))
]

MEDIA_ROOT = tempfile.gettempdir()

SITE_ID = env('MCE_SITE_ID', default=1, cast=int)

#SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# TODO: env settings pour enable/disable db logger et autres

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '%(asctime)s - [%(name)s] - [%(process)d] - [%(module)s] - [line:%(lineno)d] - [%(levelname)s] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '[%(process)d] - %(asctime)s - %(name)s: [%(levelname)s] - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'debug' if DEBUG else 'simple'
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': env('MCE_LOG_LEVEL', default='DEBUG'),
            'propagate': False,
        },
        'urllib3': {'level': 'ERROR'},
        'chardet': {'level': 'WARN'},
        'cchardet': {'level': 'WARN'},
    },
}


CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        #'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.AllowAny'
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'ORDERING_PARAM': 'sort',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = 10
DJANGO_DB_LOGGER_ENABLE_FORMATTER = False

if ROLLBAR_ENABLE and ROLLBAR_TOKEN:
    MIDDLEWARE.append('rollbar.contrib.django.middleware.RollbarNotifierMiddleware')
    ROLLBAR = {
        'access_token': ROLLBAR_TOKEN,
        'environment': 'development' if DEBUG else 'production',
        'root': BASE_DIR,
    }
    import rollbar
    rollbar.init(**ROLLBAR)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#CRISPY_TEMPLATE_PACK = 'bootstrap4'

SWAGGER_SETTINGS = {
    #'LOGIN_URL': reverse_lazy('admin:login'),
    #'LOGOUT_URL': '/admin/logout',
    'PERSIST_AUTH': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'REFETCH_SCHEMA_ON_LOGOUT': True,

    #'DEFAULT_INFO': 'testproj.urls.swagger_info',

    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'in': 'header',
            'name': 'Authorization',
            'type': 'apiKey',
        },
        #'OAuth2 password': {
        #    'flow': 'password',
        #    'scopes': {
        #        'read': 'Read everything.',
        #        'write': 'Write everything,',
        #    },
        #    'tokenUrl': OAUTH2_TOKEN_URL,
        #    'type': 'oauth2',
        #},
        'Query': {
            'in': 'query',
            'name': 'auth',
            'type': 'apiKey',
        },
    },
    #'OAUTH2_REDIRECT_URL': OAUTH2_REDIRECT_URL,
    #'OAUTH2_CONFIG': {
    #    'clientId': OAUTH2_CLIENT_ID,
    #    'clientSecret': OAUTH2_CLIENT_SECRET,
    #    'appName': OAUTH2_APP_NAME,
    #},
    #"DEFAULT_PAGINATOR_INSPECTORS": [
    #    'testproj.inspectors.UnknownPaginatorInspector',
    #    'drf_yasg.inspectors.DjangoRestResponsePagination',
    #    'drf_yasg.inspectors.CoreAPICompatInspector',
    #]
}

MATERIAL_ADMIN_SITE = {
    'HEADER':  _("Multi-Cloud-Explorer Administration"),
    'TITLE':  _('Multi-Cloud-Explorer'),
    'SHOW_THEMES':  False,
    'TRAY_REVERSE': False, 
    'NAVBAR_REVERSE': False,  
    'SHOW_COUNTS': True, 
    'APP_ICONS': {  
        'sites': 'send',
        'mce_django_app': 'web',
    },
    'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
        'site': 'contact_mail',
    }
}

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    }
}

RQ = {
    'DEFAULT_RESULT_TTL': 86400, # 24H
    #'BURST': True,
    'SHOW_ADMIN_LINK': True
}

