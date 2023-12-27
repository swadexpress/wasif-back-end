# chat/urls.py
from django.urls import path

from chat.views import *


urlpatterns = [
    # path("", index, name="index"),
    # path("<str:room_name>/", room, name="room"),
        path('CreateRoomView/', CreateRoomView.as_view(),
         name='CreateRoomView'),
        path('AllRoomsView/', AllRoomsView.as_view(),
         name='AllRoomsView'),
        path('MyRoomsView/', MyRoomsView.as_view(),
         name='MyRoomsView'),
        path('CreateRoomTokenView/', CreateRoomTokenView.as_view(),
         name='CreateRoomTokenView'),
]


