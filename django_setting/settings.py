#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 windpro

Author  :   windpro
E-mail  :   windprog@gmail.com
Date    :   14-11-18
Desc    :   配置
"""
"""
Django settings for fastblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os,sys
# 项目根目录
BASE_DIR = os.path.join(os.path.dirname(__file__), '../')
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0wijm$qzn5!p4k=j$1h_yz=z_pck)m7qw9lmkjg@%lon_3f*l9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.codedig.org', 'localhost']


# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fastblog',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

)

ROOT_URLCONF = 'django_setting.urls'

WSGI_APPLICATION = 'django_setting.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

#TIME_FORMAT = 'a'
DATETIME_FORMAT = 'Y/m/d H:i:s'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.eggs.Loader',

    'django.template.loaders.filesystem.Loader',  #to load bootstrap must make it after or disable
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'fastblog/templates').replace('\\', '/'),

)

STATIC_ROOT = os.path.join(BASE_DIR, 'fastblog/static'.replace('\\', '/'))

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

FASTBLOG_PATH = os.path.join(BASE_DIR, 'fastblog/').replace('\\', '/')

STATICFILES_DIRS = (
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('js', os.path.join(STATIC_ROOT, 'js')),
    ('img', os.path.join(STATIC_ROOT, 'img')),
    ('admin/css', os.path.join(STATIC_ROOT, 'admin/css')),
    ('admin/js', os.path.join(STATIC_ROOT, 'admin/js')),
    ('admin/js/admin', os.path.join(STATIC_ROOT, 'admin/js/admin')),

    ('admin/img', os.path.join(STATIC_ROOT, 'admin/img')),


    ('admin/css', os.path.join(FASTBLOG_PATH, 'static/admin/css')),
    ('admin/js', os.path.join(FASTBLOG_PATH, 'static/admin/js')),
    ('admin/js/admin', os.path.join(FASTBLOG_PATH, 'static/admin/js/admin')),

    ('admin/img', os.path.join(FASTBLOG_PATH, 'static/admin/img')),
)

# print ('admin/css', os.path.join(MYBLOG_PATH, 'static/admin/css'))
# print ('css', os.path.join(STATIC_ROOT, 'css'))

#头像地址
GRAVATAR_URL_PREFIX = 'https://0.gravatar.com/avatar/'
#GRAVATAR_DEFAULT_IMAGE=''
