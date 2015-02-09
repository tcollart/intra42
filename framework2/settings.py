"""
Django settings for framework2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
from django.conf import global_settings
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
import local_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = local_settings.SECRET_KEY 

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap_breadcrumbs',
    'bootstrap3',
    'apps.core',
    'apps.forum',
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
    'django.middleware.locale.LocaleMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'framework2.sqlite3'),
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
    "apps/tickets/templates",
    "apps/admincustom/templates",
)

LOCALE_PATHS = (
    'templates/locale'
    'apps/core/locale',
    'apps/forum/locale',
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
