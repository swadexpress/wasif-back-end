# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/test-chat/(?P<room_name>\w+)/$', consumers.TestChatConsumer),
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/fruitgame/(?P<room_name>\w+)/$', consumers.FruitgameConsumer),
    re_path(r'ws/p2p-messages/(?P<room_name>\w+)/$', consumers.P2PMessages),
]




# # chat/routing.py
# from django.urls import re_path

# # from . import consumers
# from chat import consumers

# websocket_urlpatterns = [
#     re_path(r'ws/TestChatConsumer/(?P<room_name>\w+)/$',
#             consumers.TestChatConsumer),
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer),
#     re_path(r"ws/fruitgame/(?P<room_name>\w+)/$",
#             consumers.FruitgameConsumer),
#     re_path(r"ws/p2p-messages/(?P<room_name>\w+)/$",
#             consumers.P2PMessages),

# ]
