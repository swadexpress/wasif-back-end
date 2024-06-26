from django.urls import re_path

from chat import consumers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
    re_path(r"ws/fruitgame/(?P<room_name>\w+)/$", consumers.FruitgameConsumer.as_asgi()),
    re_path(r"ws/fruit-loop-game/(?P<room_name>\w+)/$", consumers.FruitLoopgameConsumer.as_asgi()),
    re_path(r"ws/rocket-crash-game/(?P<room_name>\w+)/$", consumers.RocketCrashConsumer.as_asgi()),
    re_path(r"ws/p2p-messages/(?P<room_name>\w+)/$", consumers.P2PMessages.as_asgi()),



]