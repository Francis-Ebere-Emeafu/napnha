from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "www.napnha.coding4africa.com", "napnha.coding4africa.com", "www.napnha.org", "napnha.com"]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my-db-name',
        'USER': 'my-db-user-name',
        'PASSWORD': 'my-db-password',
        'HOST': 'localhost',
        'PORT': ''
    }
}
