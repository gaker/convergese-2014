
from company.settings import *

INSTALLED_APPS += ('debug_toolbar', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'converge',
        'USER': 'gaker',
        'PASSWORD': ''
    }
}

