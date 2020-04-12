from setuptools import setup, find_packages

setup(
    name='mce-django-server',
    version="0.1.0",
    description='Django Server for Multi Cloud Explorer',
    license='GPLv3+',
    url='https://github.com/multi-cloud-explorer/mce-django-server.git',
    packages=find_packages(),
    include_package_data=True, 
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
