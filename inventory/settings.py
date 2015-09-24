# -*- coding: utf-8 -*-
"""
Django settings for inventory project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uy1xe1om78t*ktywn^n*vw438m8!@k&&g1!uv1*$k(qm0s7)_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'showbase',
#    'author',
       
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#    'author.middlewares.AuthorDefaultBackendMiddleware',
)

ROOT_URLCONF = 'inventory.urls'

WSGI_APPLICATION = 'inventory.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '/home/dedo/Django/inventory/db/1.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "/home/dedo/Django/inventory/static/"
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
FIXTURE_DIRS = (
   os.path.join(BASE_DIR, 'fixtures'),
)
GRAPPELLI_ADMIN_TITLE = 'Подотчет'
#GRAPPELLI_AUTOCOMPLETE_LIMIT=10
#GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
 #   "showbase": {
 #       "Podotchet": ("id__iexact", "name__icontains",)
 #   }
#}
