#!/usr/bin/env python
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

with open('sample/version.py') as version_file:
    exec(version_file.read())

setup(
    name='sample',
    version=__version__,
    description='Django Sample',
    long_description=README,
    author='leeeandroo',
    author_email='leeeandroo@gmail.com',
    include_package_data=True,
    url='https://bitbucket.org/username/sample.gui',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'server = sample.wsgi:run',         
        ]
    }
)
