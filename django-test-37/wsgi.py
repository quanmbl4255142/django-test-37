"""
WSGI config for django-test-37 project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-test-37.settings')

application = get_wsgi_application()
