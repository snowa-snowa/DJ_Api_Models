"""
WSGI config for DJ_Api_Models project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

# import os
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DJ_Api_Models.settings')
#
# application = get_wsgi_application()

import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/snowa/test/main.py/snow'
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'DJ_Api_Models.settings'

application = get_wsgi_application()
