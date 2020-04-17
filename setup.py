from setuptools import setup, find_packages

install_requires = [
    'uvicorn',
    'uvloop',
    'gevent',
    'python-dotenv',
    'Pillow',
    'python-decouple',

    'Django>=3.0',
    'django-environ',
    'django-extensions',
    'django-filter',
    'django-cryptography',
    'django-select2',
    'django-model-utils',
    'django-material-admin',
    'django-crispy-forms',

    'whitenoise',
    'rollbar',

    'djangorestframework',
    'django-cors-headers',
    'djoser',
    'drf-yasg',

    'hiredis',
    'django-redis',

    'mce-django-app@git+https://github.com/multi-cloud-explorer/mce-django-app.git@master#egg=mce_django_app',
    'mce-tasks-rq@git+https://github.com/multi-cloud-explorer/mce-tasks-rq.git@master#egg=mce_tasks_rq',
]

tests_requires = [
    'pytest',
    'pytest-cov',
    'pytest-pep8',
    'pytest-django',
    'pytest-timeout',
    'django-dynamic-fixture',
    'pytest-instafail',
    'curlify',
    'factory-boy',
    'bandit',
    'flake8',
    'coverage',
    'responses',
    'freezegun',
]

dev_requires = [
    'pylint',
    'ipython',
    'autopep8',
    'black',
    'wheel',
    'django-debug-toolbar',
]

extras_requires = {
    'tests': tests_requires,
    'dev': dev_requires,
    'psql': [
        'psycopg2-binary',
        #'psycogreen',
        #'django-db-geventpool',
    ],
   'mysql': [
        'mysqlclient',
   ]
}

setup(
    name='mce-django-server',
    version="0.1.0",
    description='Django Server for Multi Cloud Explorer',
    license='GPLv3+',
    url='https://github.com/multi-cloud-explorer/mce-django-server.git',
    packages=find_packages(exclude=("tests",)),
    include_package_data=False, 
    tests_require=tests_requires,
    install_requires=install_requires,
    extras_require=extras_requires,
    test_suite='tests',
    zip_safe=False,
    author='Stephane RAULT',
    author_email="stephane.rault@radicalspam.org",
    python_requires='>=3.7',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
