from setuptools import setup, find_packages

install_requires = [
    'gevent',
    'gevent-openssl', # https://github.com/mjs/gevent_openssl

    'gunicorn',
    'python-decouple',
    'python-dotenv',
    'requests',
    'ujson',
    'click',
    'Pillow',
    'Django',
    'djangorestframework',
    'dj-database-url',
    'django-cors-headers',
    'django-environ',
    'django-extensions',
    'django-filter',
    'django-cryptography',
    'djoser',
    'drf-yasg[validation]',
    'django-select2',
    'django-q',
    'psutil',
    'jsonpatch',
    'django-redis-cache',
    'hiredis',
    'django-model-utils',
    'django-db-logger@git+https://github.com/srault95/django-db-logger@update_to_django3#egg=django-db-logger',

    'psycopg2-binary',
    'django-db-geventpool', # require: psycopg2>=2.5.1, psycogreen > 1.0
    'psycogreen',

    'mce-django-app',
    'mce-tasks-djq',
]

install_requires_azure = [
    #'azure',
    'azure-mgmt-resource',
    'mce-lib-azure'
]

install_requires_aws = [
    'boto3',
    #'mce-lib-aws',
]

install_requires_gcp = [
    'google-cloud-resource-manager',
    #'mce-lib-gcp',
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
    'bandit',         # python security audit
    'flake8',
    'coverage',
    'responses',
    'freezegun',

    'moto',
    #'localstack',
]

dev_requires = [
    'pylint',
    'ipython',
    'autopep8',
    'black',
]

doc_requires = [
    'Sphinx',
    'sphinx_rtd_theme',
    'sphinx-click',
]

extras_requires = {
    'tests': tests_requires,
    'dev': dev_requires,
    'doc': doc_requires,
    'azure': install_requires_azure,
    'aws': install_requires_aws,
    'gcp': install_requires_gcp,
    'full': install_requires_azure + install_requires_aws + install_requires_gcp
}

setup(
    name='mce-django-server',
    version="0.1.0",
    description='Django Server for Multi Cloud Explorer',
    license='GPLv3+',
    url='https://github.com/multi-cloud-explorer/mce-django-server.git',
    packages=find_packages(),
    include_package_data=True, 
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
