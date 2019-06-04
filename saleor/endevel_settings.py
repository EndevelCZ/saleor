import os
from decouple import AutoConfig
import raven

config = AutoConfig(os.environ.get('DJANGO_CONFIG_ENV_DIR'))

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('PROJECT_SECRET_KEY', default='')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRESQL_DATABASE', default=''),
        'USER': config('POSTGRESQL_USER', default=''),
        'HOST': config('POSTGRESQL_HOST', default=''),
        'PORT': config('POSTGRESQL_PORT', default=''),
        'PASSWORD': config('POSTGRESQL_PASSWORD', default=''),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 600,
    }
}

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')
DEFAULT_REPLY_EMAIL = config('DEFAULT_REPLY_EMAIL', default='')
EMAIL_SUBJECT_PREFIX = ''
SERVER_EMAIL = 'info@endevel.cz'       # The email address that error messages come from
SEND_BROKEN_LINK_EMAILS = False

UPLOADED_ATTACHMENTS_DIR = u'/tmp/'

PATH_TO_LOGDIR = os.path.join(config('PROJECT_HOME_DIR', ''), 'log/')
os.makedirs(PATH_TO_LOGDIR, exist_ok=True)
DEBUG_LOG_FILE = os.path.join(PATH_TO_LOGDIR, 'debug.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d'
                      '%(thread)d <%(name)s|%(filename)s:%(lineno)s> %(message)s'
        },
        'plain': {
            'format': '%(asctime)s %(levelname)s <%(name)s> %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': DEBUG_LOG_FILE,
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'plain',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },

    },
    'loggers': {
        'main': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG'
        },
        '': {
            'handlers': ['console', 'file'],  #
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

RAVEN_CONFIG = {
    'dsn': config('SENTRY_DSN', default=''),
    'release': raven.fetch_git_sha(PROJECT_DIR),
    'environment': config('ENVIRONMENT', default=''),
}
