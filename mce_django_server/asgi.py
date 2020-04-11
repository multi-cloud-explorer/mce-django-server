import os

from django.core.asgi import get_wsgi_application

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', ' mce_django_server.settings.dev')

application = get_asgi_application()
