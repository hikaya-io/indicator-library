"""
Local deployment configurations
Set the environment variables to improve the security of your credentials
Do not push hardcoded values to the remote repo
"""
from .base import *

import os

SECRET_KEY = '=tg2x0!e#9@)0jgl1wgi8g*b=aw^ogd6d3k%9mplnna%v3+wn='

ALLOWED_HOSTS = []


DEBUG = False
# Application definition


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # django.db.backends.sqlite3
        'NAME': os.environ.get('INDICATOR_LIB_DB_NAME', ''),
        'USER': os.environ.get('INDICATOR_LIB_DB_USER', ''),
        'PASSWORD': os.environ.get('INDICATOR_LIB_DB_PASSWORD', ''),
        'HOST': os.environ.get('INDICATOR_LIB_DB_HOST', ''),
        'PORT': os.environ.get('INDICATOR_LIB_DB_PORT', 0),
    }
}



