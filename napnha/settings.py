"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^i*)$5bjf99xij=l-rvm-_yo7yn@ja#q&&9tl7y1q1d-0fc!8g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://napnha.org',
    'www.napnha.org',
    'napnha.org',
    '162.243.173.228',
    'localhost',
    '127.0.0.1',
    'http://napnha.org',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts.apps.AccountsConfig',
    'contact.apps.ContactConfig',
    'core.apps.CoreConfig',

    'location.apps.LocationConfig',
    'streams.apps.StreamsConfig',
    'flex.apps.FlexConfig',

    # third party app
    'post_office',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'napnha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    # {
    #     'BACKEND': 'post_office.template.backends.post_office.PostOfficeTemplates',
    #     'APP_DIRS': True,
    #     'DIRS': [],
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.contrib.auth.context_processors.auth',
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.i18n',
    #             'django.template.context_processors.media',
    #             'django.template.context_processors.static',
    #             'django.template.context_processors.tz',
    #             'django.template.context_processors.request',
    #         ]
    #     }
    # },
]

WSGI_APPLICATION = 'napnha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'napnha_db',
        'USER': 'napnha_db',
        'PASSWORD': 'pass.p1985',
        'HOST': 'localhost',
        'PORT': '',
        'PORT': ''
    }
}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "otherstatic"),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")


# Global settings of HASH-ID HashidAutoField
HASHID_FIELD_SALT = "icode-programming"
HASHID_FIELD_ALLOW_INT_LOOKUP = True


# Sending Email to registering members
# EMAIL_HOST = 'smtp.webfaction.com'
# EMAIL_HOST_USER = 'napnha_registrations'
# EMAIL_HOST_PASSWORD = 'pass.p1985'
# DEFAULT_FROM_EMAIL = 'registrations@napnha.emeafu.com'
# SERVER_EMAIL = 'registrations@napnha.emeafu.com'
# EMAIL_BACKEND = 'post_office.EmailBackend'


# Sending Email to registering members
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'napnha_registration'
EMAIL_HOST_PASSWORD = 'NAPNHA.password'
DEFAULT_FROM_EMAIL = 'registration@napnha.org'
SERVER_EMAIL = 'registration@napnha.org'
# EMAIL_BACKEND = 'post_office.EmailBackend'

# POST_OFFICE = {
#     'TEMPLATE_ENGINE': 'post_office',
# }
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'freemandigits@gmail.com'
# EMAIL_HOST_PASSWORD = 'freemanbox12'
# EMAIL_PORT = 587
# https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef


try:
    from .local_settings import *
except:
    pass
