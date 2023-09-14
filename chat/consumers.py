# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer

# chat/consumers.py
import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import *


class ChatConsumer(WebsocketConsumer):
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

            print(status, 'status')
            # ==== get data from app====
            my_user_id = text_data_json["my_user_id"]
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_name = text_data_json["room_name"]
            room_join_sit_position = text_data_json["room_join_sit_position"]

            # ====IsJoinRoomsUsers model react in database=====
            IsJoinRoomsUsers.objects.create(
                user_id=my_user_id,
                room_name=room_name,
                room_coustom_unique_id=room_coustom_unique_id,
                room_join_sit_position=room_join_sit_position,
            )
            is_join_rooms_users_data = IsJoinRoomsUsers.objects.filter(
                room_coustom_unique_id=room_coustom_unique_id).values()
            is_join_rooms_users_data = list(is_join_rooms_users_data)

            # ====Send data to room group=====
            data = {
                "type": "chat.message",
                "status": status,
                "is_join_rooms_users_data": is_join_rooms_users_data,

            }
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "is_join_rooms_users_data": is_join_rooms_users_data,

                }
            )

    # Receive message from room group
    def chat_message(self, event):
        message = event
        print(event)

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
