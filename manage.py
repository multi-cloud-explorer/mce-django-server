#!/usr/bin/env python3

from gevent import monkey
monkey.patch_all(thread=True)

import gevent_openssl
gevent_openssl.monkey_patch()

#from psycogreen.gevent import patch_psycopg
#patch_psycopg()

import os, sys

def main():
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mce_django_server.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()