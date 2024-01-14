from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-#q2qfpy@ij5wh_o!@2n*z#7m^(tzuk6j6*7h5^@oqnp24ia2ld",
)

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]
