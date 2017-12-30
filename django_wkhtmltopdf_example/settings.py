"""
Django settings for django_wkhtmltopdf_example project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os

import dj_database_url
from email.utils import formataddr

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)

ADMINS = (
    (os.environ.get('ADMIN_NAME', 'admin'), os.environ.get('ADMIN_EMAIL', 'example@example.com')),
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',
                            'nks!55vd$hv31gf-(2w@e+yeo-ocrhja7519c-zfwp22x%6xbk')

# Use env setting if available, otherwise make debug false
DEBUG = bool(int(os.environ.get('DJANGO_DEBUG', '0')))

ALLOWED_HOSTS = ['django-wkhtmltopdf-example.herokuapp.com', 'localhost', '127.0.0.1']
SECURE_SSL_REDIRECT = bool(int(os.environ.get('DJANGO_ENABLE_SSL', '1')))
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'pdf_create',
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

ROOT_URLCONF = 'django_wkhtmltopdf_example.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
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

WSGI_APPLICATION = 'django_wkhtmltopdf_example.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Parse database configuration from $DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(
        default="sqlite:///%s" % os.path.join(BASE_DIR, 'db.sqlite3')
    )
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'django_wkhtmltopdf_example', 'static'),
    os.path.join(BASE_DIR, 'node_modules'),
)

DEFAULT_FROM_EMAIL = formataddr(ADMINS[0])
REPLY_TO = (
    os.environ.get('REPLY_TO_EMAIL', 'example@example.com'),
)
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
EMAIL_USE_TLS = True

if not EMAIL_HOST_PASSWORD:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'emails')


SUMMERNOTE_CONFIG = {
    # Change editor size
    'width': '100%',
    'height': '380',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol', 'height']],
        ['insert', ['link']],
    ],

    # Set common css/js media files
    'base_css': (
        '{}bootstrap/dist/css/bootstrap.css'.format(STATIC_URL),
    ),
    'base_js': (
        '{}jquery/dist/jquery.js'.format(STATIC_URL),
        '{}bootstrap/dist/js/bootstrap.js'.format(STATIC_URL),
    ),

    # You can disable file upload feature.
    'disable_upload': True,

    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
    # and call `initSummernote()` on your page.
    'lazy': True,
}
