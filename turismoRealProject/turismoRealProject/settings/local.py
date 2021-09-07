from .base import *




# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



#Configuracion que viene de secret.json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': get_secret('DB_NAME'),
        'USER':get_secret('DB_USER'),
        'PASSWORD':get_secret('PASSWORD'),
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child('static')]

MEDIA_URL ='/media/'
MEDIA_ROOT=[BASE_DIR.child('media')]

