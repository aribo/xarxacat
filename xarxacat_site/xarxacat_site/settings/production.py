# settings for production

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z4t8t*94mo19fe2wut^dww*yo$7zgi46hx6-t#jv1yti@l(8u3'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default':{  
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xarxacat',
        'USER': 'xarxacat_user',
        'PASSWORD': 'FreeCat2014',
        'HOST': '10.129.173.154
    }
}

