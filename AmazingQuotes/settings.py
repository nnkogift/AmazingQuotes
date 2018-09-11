"""
Django settings for AmazingQuotes project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from dj_database_url import config
import decouple
from google.oauth2 import service_account

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# for online debugging switch this to true
ONLINE = True
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '#nqluyl$n-=x0p(6yw$yxz(23t-wijs^ai@$k^&dqnuhtyqc9^'


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'flat_responsive',
    'flat',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django_comments',
    'amazingQuote',
    'widget_tweaks',
    'threadedcomments',
    'blog',
    'dj_database_url',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AmazingQuotes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AmazingQuotes.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if not ONLINE:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
else:
    DATABASES = {
        'default': {
            # If you are using Cloud SQL for MySQL rather than PostgreSQL, set
            # 'ENGINE': 'django.db.backends.mysql' instead of the following.
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'amazingquotes_db',
            'USER': 'gian',
            'PASSWORD': 'gianttally',
            # For MySQL, set 'PORT': '3306' instead of the following. Any Cloud
            # SQL Proxy instances running locally must also be set to tcp:3306.
            'PORT': '5433',
        }
    }
    # In the flexible environment, you connect to CloudSQL using a unix socket.
    # Locally, you can use the CloudSQL proxy to proxy a localhost connection
    # to the instance
    DATABASES['default']['HOST'] = '/cloudsql/amazingquotes-215218:us-central1:amazingquotesdbase'
    if os.getenv('GAE_INSTANCE'):
        pass
    else:
        DATABASES['default']['HOST'] = '127.0.0.1'



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

if ONLINE:
    STATIC_URL = '//storage.googleapis.com/amazingquotes-static-bucket/static/'
    STATIC_ROOT = 'static/'
else:
    STATIC_URL = 'static/'
    STATIC_ROOT = 'static/'
    # STATICFILES_DIRS = [
    #     os.path.join(BASE_DIR, "static"),
    # ]
    # STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


if ONLINE:
    MEDIA_URL = '//storage.googleapis.com/amazingquotes-media-bucket/media/'
    MEDIA_ROOT = 'media/'

else:
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if ONLINE:
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    GS_BUCKET_NAME = 'amazingquotes-media-bucket'

SITE_ID = 1


if not DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = 'DENY'

    # email settings

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.google.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'nnkogift@gmail.com'
    EMAIL_HOST_PASSWORD = 'gianttallY'

# GCS settings
GS_PROJECT_ID = 'amazingquotes-215218'

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.path.join(BASE_DIR, "amazingquotes-a926f9b0b815.json")
)

