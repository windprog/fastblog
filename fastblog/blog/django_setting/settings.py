#coding:utf-8
# Django settings for selfblog project.
from os import path
from platform import platform
import os

if 'centos' in platform():
    DEBUG = False
else:
    DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.join(os.path.dirname(__file__), '../../')
BLOG_PATH = os.path.join(PROJECT_PATH, 'blog')
LOG_PATH = os.path.join(PROJECT_PATH, "../log")
for _path in (LOG_PATH, ):
    if not os.path.exists(_path):
        os.makedirs(_path)


ADMINS = (
    ('windpro', 'windprog@gmail.com'),
)
ALLOWED_HOSTS = ['localhost', '.codedig.com']

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
    },
    'default2': {
        'ENGINE': 'django.db.backends.dummy',
        'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
    },

}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
#STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm_t&=vit))7cic$zfdl^7wfsc+$e1@_p=4@bmc54pp%25n#*%1'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pingback.middleware.PingbackMiddleware',
    'blog.middleware.OnlineMiddleware',
)
INTERNAL_IPS = ('127.0.0.1',)

ROOT_URLCONF = 'blog.django_setting.urls'
WSGI_APPLICATION = 'blog.django_setting.wsgi.application'

TEMPLATE_DIRS = (
    path.join(PROJECT_PATH, 'blog/templates'),
)

DIRECTORY_URLS = (
    'http://ping.blogs.yandex.ru/RPC2',
    'http://rpc.technorati.com/rpc/ping',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_xmlrpc',

    'xadmin',
    'crispy_forms',
    'pingback',
    'duoshuo',

    'blog',
    'blog.weixin',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
if DEBUG:
    INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar', )
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    LOG_FILE = '/tmp/blog.log'
else:
    LOG_FILE = os.path.join(LOG_PATH, 'blog.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(module)s : %(message)s'
        },
        'verbose': {
            'format': '[%(asctime)s] [%(levelname)s] %(module)s : %(message)s'
        }
    },

    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': LOG_FILE,
            'mode': 'a',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false']
        }
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
        'options': {
            'MAX_ENTRIES': 1024,
        }
    },
}


#配置文章开头使用rst格式无显示的问题
RESTRUCTUREDTEXT_FILTER_SETTINGS = {
    'doctitle_xform': False,
}

DUOSHUO_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
DUOSHUO_SHORT_NAME = 'xxxxxxxx'

# 微信
WEIXIN_APPID = 0
WEIXIN_APPSECRET = ''
