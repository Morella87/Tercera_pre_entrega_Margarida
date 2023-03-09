"""
WSGI config for Tercera_pre_entrega_Margarida project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Tercera_pre_entrega_Margarida.settings')

application = get_wsgi_application()
