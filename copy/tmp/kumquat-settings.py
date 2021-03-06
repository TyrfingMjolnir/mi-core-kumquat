"""
Django settings for kumquat_web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys, os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'bootstrap3',
	'messagegroups',
	'kumquat',
	'web',
	'mysql',
	'ftp',
	'status',
	'mail',
	'cron',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'kumquat_web.urls'
WSGI_APPLICATION = 'kumquat_web.wsgi.application'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'APP_DIRS': True,
		'DIRS': [
			os.path.join(BASE_DIR, 'templates'),
		],
		'OPTIONS': {
			'debug': True,
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
				'django_settings_export.settings_export',
			],
		},
	},
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/'

# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		# Only use logging if debug is false and it's a production environment
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'formatters': {
		'verbose': {
			'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
			'datefmt': '%Y-%m-%dT%H:%M:%S',
		},
		'simple': {
			'format': '%(levelname)s %(message)s',
			'datefmt': '%Y-%m-%dT%H:%M:%S',
		},
	},
	'handlers': {
		# Log to stdout
		'console': {
			'class':'logging.StreamHandler',
			'stream': sys.stdout,
		},
		# Log to syslog because this is much cleaner than extra file
		'syslog': {
			'class': 'logging.handlers.SysLogHandler',
			'facility': 'local1',
			'address': ('127.0.0.1', 514),
			'formatter': 'simple',
		},
	},
	'loggers': {
		# Might as well log any errors anywhere else in Django
		'django': {
			'handlers': ['console', 'syslog'],
			'level': 'ERROR',
			'propagate': False,
		},
	},
}

# kumquat
KUMQUAT_BACKEND_SOCKET = "ipc:///tmp/kumquat_backend"
KUMQUAT_USE_ZFS        = True
KUMQUAT_WEBMAIL_URL    = ''
KUMQUAT_PHPMYADMIN_URL = ''
KUMQUAT_CRONJOB_CMD    = ['sudo', '-u', 'www', 'crontab']
# Let's Encrypt
LETSENCRYPT_TOS          = 'https://letsencrypt.org/documents/LE-SA-v1.0.1-July-27-2015.pdf'
LETSENCRYPT_ACME_SERVER  = 'https://acme-v01.api.letsencrypt.org/directory'
LETSENCRYPT_ACME_FOLDER  = '/var/letsencrypt/acme/.well-known/acme-challenge/'
LETSENCRYPT_STATE_FOLDER = '/var/letsencrypt/state/'

# Allow the following variables in the template
SETTINGS_EXPORT = [
	'KUMQUAT_WEBMAIL_URL',
	'KUMQUAT_PHPMYADMIN_URL',
	'KUMQUAT_USE_ZFS',
]
