import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inddb',
        'USER': 'indlib',
        'PASSWORD': 'ind',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


DEBUG = True
