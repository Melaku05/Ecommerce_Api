from .common import *


DEBUG = True
if DEBUG:
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware')

SECRET_KEY = 'django-insecure-@n$84&@3o#z#%_*%+p$c+9xg2!9cjd!9#yqqpq=$q^12td(^ji'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
