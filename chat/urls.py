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
        path('AllJoinedRoomsView/', AllJoinedRoomsView.as_view(),
         name='AllJoinedRoomsView'),
        path('MyRoomsView/', MyRoomsView.as_view(),
         name='MyRoomsView'),
        path('RakingTodayView/', RakingTodayView.as_view(),
         name='RakingTodayView'),
        path('CreateRoomTokenView/', CreateRoomTokenView.as_view(),
         name='CreateRoomTokenView'),
        path('UserRecordView/', UserRecordView.as_view(),
         name='UserRecordView'),
        path('UserReceiveGiftsView/', UserReceiveGiftsView.as_view(),
         name='UserReceiveGiftsView'),
        path('VIPView/', VIPView.as_view(),
         name='VIPView'),
        path('BuyVIPView/', BuyVIPView.as_view(),
         name='BuyVIPView'),
        path('UsedBuyVIPView/', UsedBuyVIPView.as_view(),
         name='UsedBuyVIPView'),
        path('VIPListView/', VIPListView.as_view(),
         name='VIPListView'),
        path('ExchangeCoinToDaimondView/', ExchangeCoinToDaimondView.as_view(),
         name='ExchangeCoinToDaimondView'),
        path('RoomGiftSentHistoryView/', RoomGiftSentHistoryView.as_view(),
         name='RoomGiftSentHistoryView'),



]


