import os
import local_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = local_settings.SECRET_KEY

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

DATABASES = local_settings.DATABASES

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'app',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    'app/templates/',
)

STATIC_ROOT = 'app/static/'
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'


CONTACT_EMAIL = [local_settings.EMAIL_HOST_USER]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = local_settings.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = local_settings.EMAIL_HOST_PASSWORD
EMAIL_PORT = 587
