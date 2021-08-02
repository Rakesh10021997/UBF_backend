"""
WSGI config for upscbasicfunda project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.core.management import call_command
import djcelery
djcelery.setup_loader()
#call_command('crontab add')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upscbasicfunda.settings')

application = get_wsgi_application()
