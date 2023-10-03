from django.urls import re_path

from . import consumers

websocket_urlpatterns1 = [
    re_path(r"ws/fruitgame/(?P<room_name>\w+)/$", consumers.FruitgameConsumer.as_asgi()),
]