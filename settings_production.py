import platform
from settings import *

DEBUG = TEMPLATE_DEBUG = False

if platform.system() == 'Windows':
    MEDIA_ROOT = 'C:/Program Files/Apache Software Foundation/Apache2.2/htdocs/static'

else:
    MEDIA_ROOT = '/var/www/static'
