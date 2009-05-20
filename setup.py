#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
 
setup(
    name='django-cumulus',
    version='1.0.0b',
    description='Mosso Cloudfiles integration for Django.',
    author='Richard Leland',
    author_email='rich@richleland.com',
    url='http://github.com/richleland/django-cumulus/',
    packages=[
        'cumulus'
    ],
    zip_safe=False,
    classifiers=['Development Status :: 4 - Beta',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)