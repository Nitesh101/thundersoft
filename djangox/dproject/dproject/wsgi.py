"""
WSGI config for dproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

path = "/home/nitesh/Desktop/djangox/dproject"

if path not in sys.path:
	sys.path.append(path)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dproject.settings")

application = get_wsgi_application()
