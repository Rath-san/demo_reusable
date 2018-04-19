from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q+!6&z2qczv!kt*b!ylkoxu5dq+6tmm9a)a!4j%s5w&n+r&ecg'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
