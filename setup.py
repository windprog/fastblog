#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   cold
E-mail  :   windprog@gmail.com
Date    :   14-11-18
Desc    :   配置
"""
from setuptools import setup

setup(
    name='Blog',
    version='1.1',
    description='evilbinary blog app',
    author='evilbinary',
    author_email='windprog@gmail.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django>=1.7', 'pytz', 'Markdown>=2.5.1', 'Pygments>=1.6', 'django-admin-bootstrapped',
                      'beautifulsoup4>=4.3.2'],
)
