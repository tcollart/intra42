"""
Django settings for framework3 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

import local_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_settings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap_breadcrumbs',
    'bootstrap3',
    'apps.admincustom',
    'apps.core',
    'apps.forum',
    'apps.students',
    'apps.tickets',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.students.middleware.ImpersonateMiddleware'
)


TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'framework3.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
)

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    "templates",
    "apps/core/templates",
    "apps/forum/templates",
    "apps/students/templates",
    "apps/tickets/templates",
    "apps/admincustom/templates",
)

LOCALE_PATHS = (
    'templates/locale'
    'apps/core/locale',
    'apps/forum/locale',
    "apps/students/templates",
    'apps/tickets/locale',
    'apps/admincustom/locale',
)

LOGIN_REDIRECT_URL = '/'


# MESSAGE_TAGS = {
#    messages.SUCCESS: 'success',
#    messages.WARNING: 'warning warning',
#    messages.ERROR: 'danger error'
# }


TICKETS_MANAGER_ID = 1


