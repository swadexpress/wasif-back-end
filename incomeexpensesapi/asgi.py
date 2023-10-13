

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import os
import django
from chat.routing import websocket_urlpatterns
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "incomeexpensesapi.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django.setup()
application = get_default_application()





