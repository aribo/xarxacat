# -*- coding: utf8 -*- 


"""
Django settings for xarxacat_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'z4t8t*94mo19fe2wut^dww*yo$7zgi46hx6-t#jv1yti@l(8u3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []




# Application definition

INSTALLED_APPS = (
	
	# framework
	
	'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # tools
    'south',
    'smart_selects',
    #'django_extensions',
    #'documents', # for private documents https://github.com/yourlabs/django-documents
    #'autocomplete_light',
    #'genericm2m',
    
    # data
    'cities_light',
    
    # my apps
    'xarxacat_site',
    'core',
    'reference',
    'consell',
    'assemblees',
    'membres',
    'users',
    'tauler',
	'premsa',
    
    # security
    ## sessions
    #session_security',
    
    ## authentication
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    
	### allauth social providers
	#'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.facebook',
    
     #'lockdown', # to lock the whole site https://bitbucket.org/carljm/django-lockdown
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #'lockdown.middleware.LockdownMiddleware', # locks the entire site lockdown app
)

ROOT_URLCONF = 'xarxacat_site.urls'

WSGI_APPLICATION = 'xarxacat_site.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ca'

TIME_ZONE = 'Europe/Andorra'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '../public_html/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'public_html', 'media').replace('\\','/')


# Templates

TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'),
	)
	
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    
     #allauth specific context processors
    #'allauth.account.context_processors.account',
    #'allauth.socialaccount.context_processors.socialaccount',
)


# Authentication

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    #`allauth` specific authentication methods, such as login by e-mail
    #'allauth.account.auth_backends.AuthenticationBackend',
)


# Django suit

SUIT_CONFIG = {
    'ADMIN_NAME': 'ANC Exteriors - Xarxacat: Administració',
}

# Local settings

try:
    from local_settings import *
except ImportError:
    pass
    

# Sites
SITE_ID = 2


# auth and allauth settings

''' LOGIN_REDIRECT_URL = '/admin'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = { 'google':
        { 'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}
          
# Lockdown

LOCKDOWN_FORM = 'lockdown.forms.AuthForm'

'''

# Documents serve https://github.com/yourlabs/django-documents
DOCUMENTS_UPLOAD_TO = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'public_html', 'documents').replace('\\','/')
