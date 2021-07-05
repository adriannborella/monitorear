"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os

from .config.database import *
from .config.apps import *
from .config.templates import *
from .config.dir import *
from .config.middleware import *
from .config.pass_validators import *
from .config.jet import *

IMPORT_EXPORT_USE_TRANSACTIONS = True
ROOT_URLCONF = 'src.urls'
WSGI_APPLICATION = 'src.wsgi.application'
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

USE_THOUSAND_SEPARATOR = True

