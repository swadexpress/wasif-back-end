

# # import os
# # from channels.auth import AuthMiddlewareStack
# # from channels.routing import ProtocolTypeRouter, URLRouter
# # from channels.security.websocket import AllowedHostsOriginValidator
# # from django.core.asgi import get_asgi_application
# # from chat.routing import websocket_urlpatterns
# # django_asgi_app = get_asgi_application()
# # import chat.routing
# # application = ProtocolTypeRouter(
# #     {
# #         "http": django_asgi_app,
# #         "websocket": AllowedHostsOriginValidator(
# #             AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
# #         ),
# #     }
# # )


# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import chat.routing
# from django.core.asgi import get_asgi_application
# django_asgi_app = get_asgi_application()

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     #  "http": django_asgi_app,
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     ),
# })








# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})







