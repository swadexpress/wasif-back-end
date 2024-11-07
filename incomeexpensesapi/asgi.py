

import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import (ProtocolTypeRouter, URLRouter,
                              get_default_application)
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "incomeexpensesapi.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
# django_asgi_app = get_asgi_application()
django.setup()
application = get_default_application()








