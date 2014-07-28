# settings for development

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z4t8t*94mo19fe2wut^dww*yo$7zgi46hx6-t#jv1yti@l(8u3'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

'''
DATABASE_USER = os.environ.get("XARXACAT_DB_USER",'')
DATABASE_PASSWORD = os.environ.get("XARXACAT_DB_PASSWORD",'')

DATABASES = {
    'default':{  
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xarxacat',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': '127.0.0.1'
    }
}
'''
DATABASES = {
    'default':{  
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_xarxacat',
        'USER': 'xarxacat_user',
        'PASSWORD': 'FreeCat2014',
        'HOST': '127.0.0.1'
    }
}
