"""
WSGI config for FlashcardMastery project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.
"""

import os

from django.core.wsgi import get_wsgi_application

# Point to the project's settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FlashcardMastery.settings')

application = get_wsgi_application()
