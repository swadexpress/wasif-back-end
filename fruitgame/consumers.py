# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer

# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import *
from django.core import serializers
import datetime
from django.utils.dateparse import parse_datetime
from django.utils import dateparse


class FruitgameConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        status = text_data_json["status"]

        if (status == 'IsJoinRoomsUsers'):
            print(status, 'status')

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_sit_join_data": text_data_json,
                }
            )

    # Receive message from room group

    def chat_message(self, event):
        message = event
        # print(event)

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
