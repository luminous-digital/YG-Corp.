from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')c8=1$h9sj)&ted($vs_x@%kp2-3&=f&objz9^ql_i8v@l=nx+'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# INSTALLED_APPS = INSTALLED_APPS + [
#     'debug_toolbar',
# ]
#
# MIDDLEWARE = MIDDLEWARE + [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

INTERNAL_IPS = ('127.0.0.1', '172.17.0.1')

try:
    from .local import *  # noqa
except ImportError:
    pass

django_heroku.settings(locals())  # noqa
