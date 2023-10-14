# chat/urls.py
from django.urls import path

from . import views
from chat.views import *

urlpatterns = [

    path('CreateRoomView/', CreateRoomView.as_view(),
         name='CreateRoomView'),
    path('DeleteRoomView/', DeleteRoomView.as_view(),
         name='DeleteRoomView'),
    path('AllRoomsView/', AllRoomsView.as_view(),
         name='AllRoomsView'),
    path('CreateRoomTokenView/', CreateRoomTokenView.as_view(),
         name='CreateRoomTokenView'),
    path('index/', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),

]
