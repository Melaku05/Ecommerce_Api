import os
from .common import *


DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [] # only need production, we do not need for development