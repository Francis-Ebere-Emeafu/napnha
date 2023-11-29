from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'http://napnha.emeafu.com',
    'http://napnha.org',
    'www.napnha.org',
    'napnha.org',
]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'napnha_db',
#         'USER': 'napnha_db',
#         'PASSWORD': 'NAPNHA.password',
#         'HOST': 'localhost',
#         'PORT': '',
#         'PORT': ''
#     }
# }
