from .settings import *  # NOQA

DEBUG = False
ALLOWED_HOSTS = ['dev.django-sample.com']

STATIC_ROOT = '/home/root/project/testing/sample/static/'
MEDIA_ROOT = '/home/root/project/testing/sample/media/'

MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_sample',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'var/log/django_sample.log',
            'formatter': 'verbose',
            'backupCount': 10,
            'maxBytes': 5242880, # 5*1024*1024 bytes (5MB)
        },
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django_sample': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}