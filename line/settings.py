import os
import dj_database_url
env = os.environ
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '$7@53e2!*+9*fn%nbn32+ks%i#7%elb4w8+*4#s&mi!2l0s%dv'
DEBUG = os.environ.get('DEBUG', None) == 'True'
WSGI_APPLICATION = 'line.wsgi.application'
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'line.urls'
LIVEAGENT_API_VERSION = '40'
LIVEAGENT_HOST = env.get('LIVEAGENT_HOST')
LIVEAGENT_ORGANIZATION_ID = env.get('LIVEAGENT_ORGANIZATION_ID')
LIVEAGENT_DEPLOYMENT_ID = env.get('LIVEAGENT_DEPLOYMENT_ID')
LIVEAGENT_BUTTON_ID = env.get('LIVEAGENT_BUTTON_ID')
LIVEAGENT_USER_AGENT = env.get('LIVEAGENT_USER_AGENT', 'Mozilla/5.0')
LINE_ACCESS_TOKEN = env.get('LINE_ACCESS_TOKEN')
LINE_ACCESS_SECRET = env.get('LINE_ACCESS_SECRET')
CELERY_BROKER_URL = env.get('REDIS_URL', 'redis://127.0.0.1:6379/0')

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.contenttypes',
    'liveagent',
]

MIDDLEWARE = []

TEMPLATES = []

DATABASES = {
    'default': dj_database_url.parse(env.get('DATABASE_URL'))
}

LOGGING = {
    'version': 1,
    'formatters': {
        'all': {
            'format': '\t'.join([
                '[%(levelname)s]',
                'code:%(lineno)s',
                'asctime:%(asctime)s',
                'module:%(module)s',
                'message:%(message)s',
            ])
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'all'
        },
    },
    'loggers': {
        'command': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
