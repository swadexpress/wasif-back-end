# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import *
import datetime
from django.utils.dateparse import parse_datetime
from django.utils import dateparse
import threading
import random
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

            # ==== get data from app====
            my_user_id = text_data_json["my_user_id"]
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_name = text_data_json["room_name"]
            room_join_sit_position = text_data_json["room_join_sit_position"]
            room_join_join_uniq_id = text_data_json["room_join_join_uniq_id"]
            # ====IsJoinRoomsUsers model react in database=====
            IsJoinRoomsUsers.objects.create(
                user_id=my_user_id,
                room_name=room_name,
                room_coustom_unique_id=room_coustom_unique_id,
                room_join_sit_position=room_join_sit_position,
                room_join_join_uniq_id=room_join_join_uniq_id,
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
        if (status == 'CancelCallRoomJoin'):

            room_join_join_uniq_id = text_data_json["room_join_join_uniq_id"]
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            # ====IsJoinRoomsUsers model react in database=====
            IsJoinRoomsUsers.objects.filter(
                room_join_join_uniq_id=room_join_join_uniq_id
            ).delete()
            
            is_join_rooms_users_data = IsJoinRoomsUsers.objects.filter(
                room_coustom_unique_id=room_coustom_unique_id).values()
            is_join_rooms_users_data = list(is_join_rooms_users_data)
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": "IsJoinRoomsUsers",
                    "is_join_rooms_users_data": is_join_rooms_users_data,

                }
            )

        # ====Group Messages Send Handelilng ====
        elif (status == 'GroupMessageSend'):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "messages_data": text_data_json,

                }
            )

        # ====Group Messages Send Handelilng ====
        elif (status == 'GiftSend'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            gift_receive_user_id = text_data_json["gift_receive_user_id"]
            gift_sent_user_id = text_data_json["gift_sent_user_id"]
            gift_receive_user_profile_id_get = text_data_json["gift_receive_user_profile_id"]
            gift_sent_user_profile_id_get = text_data_json["gift_sent_user_profile_id"]
            gift_name = text_data_json["gift_name"]
            gift_amount_minus = text_data_json["gift_amount_minus"]
            gift_amount = text_data_json["gift_amount"]

            # ============= gift sent user balance update====================
            gift_sent_user_profile_data = Profile.objects.filter(
                user_id=gift_sent_user_id).values()
            gift_sent_user_profile_data_update = Profile.objects.filter(
                user_id=gift_sent_user_id)

            gift_sent_user_profile_data_update.update(
                coin=float(
                    gift_sent_user_profile_data[0]['coin']) - float(gift_amount_minus)
            )
            # ============= gift receive user balance update====================
            gift_receive_user_profile_data = Profile.objects.filter(
                user_id=gift_receive_user_id).values()
            gift_receive_user_profile_data_update = Profile.objects.filter(
                user_id=gift_receive_user_id)

            gift_receive_user_profile_data_update.update(
                coin=float(
                    gift_receive_user_profile_data[0]['coin']) + float(gift_amount)
                    # gift_receive_user_profile_data[0]['diamond']) + float(gift_amount)
            )

            # ==== gift sent and receive user profile data sent to app ====
            # =====================================================
            gift_receive_user_profile_data = serializers.serialize(
                "json", Profile.objects.filter(user_id=gift_receive_user_id))
            gift_receive_user_profile_id = [
                i['pk'] for i in json.loads(gift_receive_user_profile_data)]
            gift_receive_user_profile_data = [
                i['fields'] for i in json.loads(gift_receive_user_profile_data)]
            gift_receive_user_profile_data[0]['id'] = gift_receive_user_profile_id[0]
            gift_receive_user_profile_data = list(
                gift_receive_user_profile_data)

            # ==============================================================
            gift_sent_user_profile_data = serializers.serialize(
                "json", Profile.objects.filter(user_id=gift_sent_user_id))
            gift_sent_user_profile_id = [i['pk']
                                         for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data = [i['fields']
                                           for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data[0]['id'] = gift_sent_user_profile_id[0]
            gift_sent_user_profile_data = list(gift_sent_user_profile_data)

            # ==== create databe AllSentedGifts model ====
            AllSentedGifts.objects.create(
                gift_sent_user_id=gift_sent_user_id,
                gift_receive_user_id=gift_receive_user_id,
                gift_sent_user_profile_id=gift_sent_user_profile_id_get,
                gift_receive_user_profile_id=gift_receive_user_profile_id_get,
                room_coustom_unique_id=room_coustom_unique_id,
                gift_name=gift_name,
                gift_amount=gift_amount,
            )

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "gift_data": text_data_json,
                    "gift_sent_user_id": gift_sent_user_id,
                    "gift_receive_user_id": gift_receive_user_id,
                    "gift_sent_user_profile_data": gift_sent_user_profile_data,
                    "gift_receive_user_profile_data": gift_receive_user_profile_data,

                }
            )

        elif (status == 'MultipleUserGiftSend'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            gift_receive_users_id = text_data_json["gift_receive_users_id"]
            gift_sent_user_id = text_data_json["gift_sent_user_id"]
            gift_name = text_data_json["gift_name"]
            gift_amount_minus = text_data_json["gift_amount_minus"]
            gift_amount = text_data_json["gift_amount"]

            # ============= gift sent user balance update====================
            gift_sent_user_profile_data = Profile.objects.filter(
                user_id=gift_sent_user_id).values()
            gift_sent_user_profile_data_update = Profile.objects.filter(
                user_id=gift_sent_user_id)

            gift_sent_user_profile_data_update.update(
                coin=float(
                    gift_sent_user_profile_data[0]['coin']) - float(gift_amount_minus)
            )
            # ============= gift receive user balance update====================

            for gift_receive_user_id in gift_receive_users_id:
                gift_receive_user_profile_data = Profile.objects.filter(
                    user_id=gift_receive_user_id).values()
                gift_receive_user_profile_data_update = Profile.objects.filter(
                    user_id=gift_receive_user_id)

                # print (gift_receive_user_profile_data,'gift_receive_user_profile_data')

                gift_receive_user_profile_data_update.update(
                    diamond=float(
                        gift_receive_user_profile_data[0]['diamond']) + float(gift_amount)
                )
                # ==== create databe AllSentedGifts model ====
                AllSentedGifts.objects.create(
                    gift_sent_user_id=gift_sent_user_id,
                    gift_receive_user_id=gift_receive_user_id,
                    room_coustom_unique_id=room_coustom_unique_id,
                    gift_name=gift_name,
                    gift_amount=gift_amount,
                )

            # ==== gift sent and receive user profile data sent to app ====
            # =====================================================

            gift_receive_users_profile_update_data = []

            for gift_receive_user_id in gift_receive_users_id:

                gift_receive_user_profile_data = serializers.serialize(
                    "json", Profile.objects.filter(user_id=gift_receive_user_id))

                gift_receive_user_profile_id = [
                    i['pk'] for i in json.loads(gift_receive_user_profile_data)]
                gift_receive_user_profile_data = [
                    i['fields'] for i in json.loads(gift_receive_user_profile_data)]

                gift_receive_user_profile_data[0]['id'] = gift_receive_user_profile_id[0]
                gift_receive_users_profile_update_data.append(
                    list(gift_receive_user_profile_data))

            # ==============================================================
            gift_sent_user_profile_data = serializers.serialize(
                "json", Profile.objects.filter(user_id=gift_sent_user_id))
            # print(gift_sent_user_profile_data,'gift_sent_user_profile_data')
            gift_sent_user_profile_id = [i['pk']
                                         for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data = [i['fields']
                                           for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data[0]['id'] = gift_sent_user_profile_id[0]
            gift_sent_user_profile_data = list(gift_sent_user_profile_data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "gift_data": text_data_json,
                    "gift_sent_user_id": gift_sent_user_id,
                    "gift_receive_users_id": gift_receive_users_id,
                    "gift_sent_user_profile_data": gift_sent_user_profile_data,
                    "gift_receive_users_profile_data": gift_receive_users_profile_update_data,

                }
            )

        elif (status == 'PKGiftSend'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            gift_receive_user_id = text_data_json["gift_receive_user_id"]
            gift_sent_user_id = text_data_json["gift_sent_user_id"]
            gift_receive_user_profile_id_get = text_data_json["gift_receive_user_profile_id"]
            gift_sent_user_profile_id_get = text_data_json["gift_sent_user_profile_id"]
            gift_name = text_data_json["gift_name"]
            gift_amount_minus = text_data_json["gift_amount_minus"]
            gift_amount = text_data_json["gift_amount"]
            pk_unique_id = text_data_json["pk_unique_id"]

            # ============= gift sent user balance update====================
            gift_sent_user_profile_data = Profile.objects.filter(
                user_id=gift_sent_user_id).values()
            gift_sent_user_profile_data_update = Profile.objects.filter(
                user_id=gift_sent_user_id)

            gift_sent_user_profile_data_update.update(
                coin=float(
                    gift_sent_user_profile_data[0]['coin']) - float(gift_amount_minus)
            )
            # ============= gift receive user balance update====================
            gift_receive_user_profile_data = Profile.objects.filter(
                user_id=gift_receive_user_id).values()
            gift_receive_user_profile_data_update = Profile.objects.filter(
                user_id=gift_receive_user_id)

            gift_receive_user_profile_data_update.update(
                diamond=float(
                    gift_receive_user_profile_data[0]['diamond']) + float(gift_amount)
            )

            # ==== gift sent and receive user profile data sent to app ====
            # =====================================================
            gift_receive_user_profile_data = serializers.serialize(
                "json", Profile.objects.filter(user_id=gift_receive_user_id))
            gift_receive_user_profile_id = [
                i['pk'] for i in json.loads(gift_receive_user_profile_data)]
            gift_receive_user_profile_data = [
                i['fields'] for i in json.loads(gift_receive_user_profile_data)]
            gift_receive_user_profile_data[0]['id'] = gift_receive_user_profile_id[0]
            gift_receive_user_profile_data = list(
                gift_receive_user_profile_data)

            # ==============================================================
            gift_sent_user_profile_data = serializers.serialize(
                "json", Profile.objects.filter(user_id=gift_sent_user_id))
            gift_sent_user_profile_id = [i['pk']
                                         for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data = [i['fields']
                                           for i in json.loads(gift_sent_user_profile_data)]
            gift_sent_user_profile_data[0]['id'] = gift_sent_user_profile_id[0]
            gift_sent_user_profile_data = list(gift_sent_user_profile_data)

            # ==== UPdate PkUser Balance====
            pk_request_sent_user_balance_update = AllPK.objects.filter(
                pk_request_sent_user_id=gift_receive_user_id).order_by('-id')[0:1].values()
            pk_request_sent_user_balance_update = AllPK.objects.filter(
                id=pk_request_sent_user_balance_update[0]['id']).values()
            if (pk_request_sent_user_balance_update):
                pk_request_sent_user_balance_update.update(
                    pk_request_sent_user_balance=int(
                        pk_request_sent_user_balance_update[0]['pk_request_sent_user_balance']) + int(gift_amount)
                )
            # =================================
            pk_request_receive_user_balance_update = AllPK.objects.filter(
                pk_request_sent_user_id=gift_receive_user_id).order_by('-id')[0:1].values()
            pk_request_receive_user_balance_update = AllPK.objects.filter(
                id=pk_request_receive_user_balance_update[0]['id']).values()
            if (pk_request_receive_user_balance_update):
                pk_request_receive_user_balance_update.update(
                    pk_request_receive_user_balance=int(
                        pk_request_receive_user_balance_update[0]['pk_request_receive_user_balance']) + int(gift_amount)
                )

            pk_data = AllPK.objects.filter(pk_unique_id=pk_unique_id).order_by('-id')[0:1].values(
                "id",
                "pk_request_sent_user_id",
                "pk_request_receive_user_id",
                "pk_request_sent_user_id",
                "pk_request_sent_user_profile_id",
                "pk_request_receive_user_profile_id",
                "pk_request_sent_user_profile__fast_name",
                "pk_request_sent_user_profile__last_name",
                "pk_request_receive_user_profile__last_name",
                "pk_request_receive_user_profile__fast_name",
                "pk_request_sent_user_profile__image",
                "pk_request_receive_user_profile__image",
                "pk_unique_id",
                "pk_request_sent_user_balance",
                "pk_request_receive_user_balance",
                "pk_time",
                "pk_start_time",
                "pk_end_time",
            )
            server_current_time = datetime.datetime.now()
            pk_data = list(pk_data)
            pk_data.append({"server_current_time": str(server_current_time)})

            print(pk_data, 'pk_data')
            AllSentedGifts.objects.create(
                gift_sent_user_id=gift_sent_user_id,
                gift_receive_user_id=gift_receive_user_id,
                gift_sent_user_profile_id=gift_sent_user_profile_id_get,
                gift_receive_user_profile_id=gift_receive_user_profile_id_get,
                room_coustom_unique_id=room_coustom_unique_id,
                gift_name=gift_name,
                gift_amount=gift_amount,
            )

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "pk_data": pk_data,
                    "gift_data": text_data_json,
                    "gift_sent_user_id": gift_sent_user_id,
                    "gift_receive_user_id": gift_receive_user_id,
                    "gift_sent_user_profile_data": gift_sent_user_profile_data,
                    "gift_receive_user_profile_data": gift_receive_user_profile_data,

                }
            )

        elif (status == 'SentPKRequest'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            pk_unique_id = text_data_json["pk_unique_id"]
            pk_request_receive_user_id = text_data_json["pk_request_receive_user_id"]
            pk_request_sent_user_id = text_data_json["pk_request_sent_user_id"]
            pk_request_sent_user_full_name = text_data_json["pk_request_sent_user_full_name"]
            pk_request_sent_user_image = text_data_json["pk_request_sent_user_image"]
            pk_time = text_data_json["pk_time"]

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {

                    "type": "chat.message",
                    "status": status,
                    "pk_request_data": text_data_json,
                    "pk_request_receive_user_id": pk_request_receive_user_id,




                }
            )
        elif (status == 'PKRequestCancel'):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "pk_request_data": text_data_json,

                }
            )

        elif (status == 'PKRequestAccept'):
            pk_request_data = text_data_json["pk_request_data"]
            print(pk_request_data, 'pk_request_data')
            pk_unique_id = pk_request_data["pk_unique_id"]
            pk_request_receive_user_id = pk_request_data["pk_request_receive_user_id"]
            pk_request_sent_user_id = pk_request_data["pk_request_sent_user_id"]
            pk_request_sent_user_full_name = pk_request_data["pk_request_sent_user_full_name"]
            pk_request_sent_user_image = pk_request_data["pk_request_sent_user_image"]
            pk_request_sent_user_profile_id = pk_request_data["pk_request_sent_user_profile_id"]
            pk_request_receive_user_profile_id = pk_request_data["pk_request_receive_user_profile_id"]
            room_coustom_unique_id = pk_request_data["room_coustom_unique_id"]
            pk_time = pk_request_data["pk_time"]
            pk_start_time = datetime.datetime.now()
            server_current_time = datetime.datetime.now()
            pk_end_time = datetime.datetime.now() + datetime.timedelta(minutes=int(pk_time))
            AllPK.objects.create(
                pk_request_sent_user_id=pk_request_sent_user_id,
                pk_request_receive_user_id=pk_request_receive_user_id,
                pk_request_sent_user_profile_id=pk_request_sent_user_profile_id,
                pk_request_receive_user_profile_id=pk_request_receive_user_profile_id,
                pk_unique_id=pk_unique_id,
                room_coustom_unique_id=room_coustom_unique_id,
                pk_time=pk_time,
                pk_start_time=pk_start_time,
                pk_end_time=pk_end_time,

            )
            pk_data = AllPK.objects.filter(pk_unique_id=pk_unique_id).order_by('-id')[0:1].values(
                "id",
                "pk_request_sent_user_id",
                "pk_request_receive_user_id",
                "pk_request_sent_user_id",
                "pk_request_sent_user_profile_id",
                "pk_request_receive_user_profile_id",
                "pk_request_sent_user_profile__fast_name",
                "pk_request_sent_user_profile__last_name",
                "pk_request_receive_user_profile__last_name",
                "pk_request_receive_user_profile__fast_name",
                "pk_request_sent_user_profile__image",
                "pk_request_receive_user_profile__image",
                "pk_unique_id",
                "pk_request_sent_user_balance",
                "pk_request_receive_user_balance",
                "pk_time",
                "pk_start_time",
                "pk_end_time",
            )

            pk_data = list(pk_data)
            pk_data.append({"server_current_time": str(server_current_time)})
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "pk_request_data": pk_request_data,
                    "pk_data": list(pk_data),
                }
            )

        elif (status == 'WheneJoinRoom'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]

            print(room_coustom_unique_id, 'pk_request_data')

            server_current_time = datetime.datetime.now()

            pk_data = AllPK.objects.filter(room_coustom_unique_id=room_coustom_unique_id).order_by('-id')[0:1].values(
                "id",
                "pk_request_sent_user_id",
                "pk_request_receive_user_id",
                "pk_request_sent_user_id",
                "pk_request_sent_user_profile_id",
                "pk_request_receive_user_profile_id",
                "pk_request_sent_user_profile__fast_name",
                "pk_request_sent_user_profile__last_name",
                "pk_request_receive_user_profile__last_name",
                "pk_request_receive_user_profile__fast_name",
                "pk_request_sent_user_profile__image",
                "pk_request_receive_user_profile__image",
                "pk_unique_id",
                "pk_request_sent_user_balance",
                "pk_request_receive_user_balance",
                "pk_time",
                "pk_start_time",
                "pk_end_time",
            )

            if pk_data:
                if dateparse.parse_datetime(pk_data[0]['pk_end_time']) > server_current_time:
                    pk_data = list(pk_data)
                    pk_data.append(
                        {"server_current_time": str(server_current_time)})
                    pk_data = list(pk_data)
                else:
                    pk_data = None
            else:
                pk_data = None

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "pk_data": pk_data,
                }
            )

        elif (status == 'RoomLockAndUnLock'):
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_lock_password = text_data_json["room_lock_password"]
            room_lock = text_data_json["room_lock"]
            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                room_password=room_lock_password,
                room_lock=room_lock
            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'RoomSitLock'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_sit_lock_position = text_data_json["room_sit_lock_position"]
            room_sit_password = text_data_json["room_sit_password"]
            room_sit_lock_position
            room_sit_lock_position_update = "room_sit_" + \
                str(room_sit_lock_position)+"_lock_position"
            room_sit_password_update = "room_sit_" + \
                str(room_sit_lock_position)+"_password"
            room_update_data = {
                room_sit_lock_position_update: room_sit_lock_position,
                room_sit_password_update: room_sit_password,
            }

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                **room_update_data

            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'ChangeRoomSetNumber'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_set_number = text_data_json["room_set_number"]

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                room_user_can_join=room_set_number
            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )
        elif (status == 'RoomMoveToAudioAndAudioToVideo'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_media_status = text_data_json["room_media_status"]

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                room_media_status=room_media_status
            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'RoomMoveToAudioAndAudioToVideo'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_media_status = text_data_json["room_media_status"]

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                room_media_status=room_media_status
            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'UpdateWelcomeMassageAndTitleAndRoomTag'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_name_update = text_data_json["room_name_update"]
            room_name_values = text_data_json["room_name_values"]
            room_update_data = {
                room_name_update: room_name_values,

            }
            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            all_room_update.update(
                **room_update_data
            )

            json_data = serializers.serialize("json", all_room_update)
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'KickOut'):

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "kick_out_data": text_data_json,
                }
            )

        elif (status == 'JoinVideoCallRequest'):
            print(text_data_json)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "join_video_call_data": text_data_json,
                }
            )

        elif (status == 'JoinVideoCallRequestAccept'):
            

            join_video_call_data = text_data_json["join_video_call_data"]
            print(text_data_json,'........')

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "join_video_call_data": join_video_call_data,
                }
            )
        elif (status == 'AdminCancelCallRoomJoin'):
        
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "cancel_video_call_data": text_data_json,
                }
            )

        elif (status == 'RoomUserMuteMic'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_mute_mic_user_profile_id = text_data_json["room_mute_mic_user_profile_id"]
            muteMicStatus = text_data_json["muteMicStatus"]

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            print(muteMicStatus, 'muteMicStatus')
            print(all_room_update, 'all_room_update')
            if muteMicStatus:
                # print('oka')
                for i in all_room_update:
                    i.room_mute_mic_user_profile_list.remove(
                        room_mute_mic_user_profile_id)
            else:
                # print('no')
                for i in all_room_update:
                    i.room_mute_mic_user_profile_list.add(
                        room_mute_mic_user_profile_id)

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)

            json_data = serializers.serialize("json", AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id))
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_mute_mic_user_profile_id": room_mute_mic_user_profile_id,
                    "room_data": room_details,
                    "muteMicStatus": muteMicStatus,
                }
            )

        elif (status == 'RoomAddAdmin'):

            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_sup_admin_profile_id = text_data_json["room_sup_admin_profile_id"]
            join_status = text_data_json["join_status"]

            print(join_status, 'join_status')

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)
            if join_status:
                print('oka')
                for i in all_room_update:
                    i.room_sup_admin_profile.remove(
                        room_sup_admin_profile_id)
            else:
                print('no')
                for i in all_room_update:
                    i.room_sup_admin_profile.add(
                        room_sup_admin_profile_id)

            all_room_update = AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id)

            json_data = serializers.serialize("json", AllRooms.objects.filter(
                room_coustom_id=room_coustom_unique_id))
            profile_id = [i['pk'] for i in json.loads(json_data)]
            data = [i['fields'] for i in json.loads(json_data)]
            # add profile  id
            data[0]['id'] = profile_id[0]
            room_details = list(data)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_data": room_details,
                }
            )

        elif (status == 'RoomSitLockForJoinRequestSent'):

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_sit_lock_for_join_data": text_data_json,
                }
            )
        elif (status == 'RoomSitLockForJoinRequestReceive'):

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_sit_lock_for_join_data": text_data_json,
                }
            )
        elif (status == 'RoomSitJoinSentRequest'):

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_sit_join_data": text_data_json,
                }
            )
        elif (status == 'RoomSitJoinReceiveRequest'):

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
        status = text_data_json["status"]
        if (status == 'InvestAddAndRemove'):
            investment_data = text_data_json["investment_data"]
            user_profile_data = text_data_json["user_profile_data"]

            if (user_profile_data):
                FruitInvestment.objects.filter(
                    user_profile_id=user_profile_data['id'],
                ).delete()
                FruitInvestment.objects.create(
                    user_profile_id=user_profile_data['id'],
                    investment=json.dumps(investment_data),
                    profile_data=json.dumps(user_profile_data),
                )
            else:
                FruitInvestment.objects.filter(
                    user_profile_id=user_profile_data['id'],
                ).delete()

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "room_sit_join_data": text_data_json,
                }
            )
        elif (status == 'FruitInvestmentTimeline'):
            def mytimer():
                # print("Demo Python Program\n")
                fruit_investment_data = FruitInvestment.objects.all()
                apple_amount = []
                avocado_amount = []
                grape_amount = []
                mango_amount = []
                papaya_amount = []
                pineapple_amount = []
                strawberry_amount = []
                watermelon_amount = []
                fruit_investment_data_update = []
                server_current_time = datetime.datetime.now()

                for i in fruit_investment_data:
                    for j in json.loads(i.investment):
                        if (j['name'] == 'apple'):
                            apple_amount.append(int(j['amount']))
                        elif (j['name'] == 'avocado'):
                            avocado_amount.append(int(j['amount']))
                        elif (j['name'] == 'grape'):
                            grape_amount.append(int(j['amount']))
                        # elif (j['name'] == 'mango'):
                        #     mango_amount.append(int(j['amount']))
                        # elif (j['name'] == 'papaya'):
                        #     papaya_amount.append(int(j['amount']))
                        # elif (j['name'] == 'pineapple'):
                        #     pineapple_amount.append(int(j['amount']))
                        # elif (j['name'] == 'strawberry'):
                        #     strawberry_amount.append(int(j['amount']))
                        # elif (j['name'] == 'watermelon'):
                        #     watermelon_amount.append(int(j['amount']))

                    investment_data = json.loads(i.investment)
                    fruit_investment_data_update.append(
                        [investment_data, [json.loads(i.profile_data)]])

                for i in fruit_investment_data_update:
                    win_fruit_name = 'apple'
                    apple_amount_first_win = []
                    smallest_value = min(sum(apple_amount), sum(
                        avocado_amount), sum(grape_amount))

                if smallest_value > 0:
                    if smallest_value == apple_amount:
                        win_fruit_name = 'apple'
                        apple_amount_first_win = sorted(apple_amount)

                    elif smallest_value == avocado_amount:
                        win_fruit_name = 'avocado'
                        apple_amount_first_win = sorted(avocado_amount)

                    # elif smallest_value == mango_amount:
                    #     win_fruit_name = 'mango'
                    #     apple_amount_first_win = sorted(mango_amount)

                    # elif smallest_value == papaya_amount:
                    #     win_fruit_name = 'papaya'
                    #     apple_amount_first_win = sorted(papaya_amount)

                    # elif smallest_value == pineapple_amount:
                    #     win_fruit_name = 'pineapple'
                    #     apple_amount_first_win = sorted(pineapple_amount)

                    # elif smallest_value == strawberry_amount:
                    #     win_fruit_name = 'strawberry'
                    #     apple_amount_first_win = sorted(strawberry_amount)

                    # elif smallest_value == watermelon_amount:
                    #     win_fruit_name = 'watermelon'
                    #     apple_amount_first_win = sorted(watermelon_amount)

                    win_investment_data_1 = []
                    win_investment_amount_1 = 0
                    win_investment_data_2 = []
                    win_investment_amount_2 = 0
                    win_investment_data_3 = []
                    win_investment_amount_3 = 0

                    all_profile_data = []

                    for item in i[0]:
                        if item["name"] == win_fruit_name:
                            if len(apple_amount_first_win) >= 0:
                                win_investment_data_1.append(i[1][0])
                                win_investment_amount_1 = item['win_amount']
                                print(len(apple_amount_first_win), '1')

                            elif len(apple_amount_first_win) >= 2:
                                win_investment_data_2.append(i[1][0])
                                win_investment_amount_2 = item['win_amount']

                                print(len(apple_amount_first_win), '2')
                            elif len(apple_amount_first_win) >= 3:
                                win_investment_data_3.append(i[1][0])
                                win_investment_amount_3 = item['win_amount']
                                print(len(apple_amount_first_win), '3')

                            filter_profile = Profile.objects.filter(
                                id=i[1][0]['id'])
                            filter_profile_balance = filter_profile.values()
                            filter_profile.update(
                                coin=(
                                    (float(filter_profile_balance[0]['coin'])) + (float(item["win_amount"])))
                            )
                            filter_profile_update = serializers.serialize(
                                "json", filter_profile)
                            filter_profile_update_id = [
                                i['pk'] for i in json.loads(filter_profile_update)]
                            filter_profile_update = [
                                i['fields'] for i in json.loads(filter_profile_update)]
                            filter_profile_update[0]['id'] = filter_profile_update_id[0]
                            all_profile_data.append(filter_profile_update)
                        else:

                            filter_profile = Profile.objects.filter(
                                id=i[1][0]['id'])
                            filter_profile_balance = filter_profile.values()
                            filter_profile.update(
                                coin=(
                                    (float(filter_profile_balance[0]['coin'])) - (float(item["amount"])))
                            )
                            filter_profile_update = serializers.serialize(
                                "json", filter_profile)
                            filter_profile_update_id = [
                                i['pk'] for i in json.loads(filter_profile_update)]
                            filter_profile_update = [
                                i['fields'] for i in json.loads(filter_profile_update)]
                            filter_profile_update[0]['id'] = filter_profile_update_id[0]
                            all_profile_data.append(filter_profile_update)
                        print(win_investment_amount_1,
                              'win_investment_amount_1')
                        print(win_investment_amount_1,
                              'win_investment_amount_1')

                        async_to_sync(self.channel_layer.group_send)(
                            self.room_group_name,
                            {
                                "type": "chat.message",
                                "status": "FruitInvestmentWiner",
                                "server_current_time": str(server_current_time),
                                "win_fruit_name": win_fruit_name,
                                "win_investment_data_1": win_investment_data_1,
                                "win_investment_data_2": win_investment_data_2,
                                "win_investment_data_3": win_investment_data_3,
                                "all_profile_data": all_profile_data,
                                "win_investment_amount_1": win_investment_amount_1,
                                "win_investment_amount_2": win_investment_amount_2,
                                "win_investment_amount_3": win_investment_amount_3,
                            }
                        )

                else:
                    win_investment_data_dumy_1 = Profile.objects.filter(
                        id=1).values()
                    win_investment_data_dumy_2 = Profile.objects.filter(
                        id=2).values()
                    async_to_sync(self.channel_layer.group_send)(
                        self.room_group_name,
                        {
                            "type": "chat.message",
                            "status": "FruitInvestmentWiner",

                            "win_fruit_name": 'apple',
                            "win_investment_data_1": list(win_investment_data_dumy_1),
                            "win_investment_data_2": list(win_investment_data_dumy_2),
                            "win_investment_data_3": list(win_investment_data_dumy_1),
                            "all_profile_data": "",
                            "win_investment_amount_1": random.randint(11111, 99999),
                            "win_investment_amount_2": random.randint(1111, 9999),
                            "win_investment_amount_3": random.randint(111, 999),

                        }
                    )

            def FruitInvestmentTimelineSent():
                start_time = datetime.datetime.now()
                server_current_time = datetime.datetime.now()
                end_time = datetime.datetime.now() + datetime.timedelta(seconds=60)
                is_fruit_investment_timeline_fruit_investment_timeline = FruitInvestmentTimeline.objects.all(
                ).order_by('-id')[0:1].values()
                if (is_fruit_investment_timeline_fruit_investment_timeline):
                    if server_current_time > datetime.datetime.fromisoformat(is_fruit_investment_timeline_fruit_investment_timeline[0]['end_time']):
                        FruitInvestmentTimeline.objects.all().delete()
                        FruitInvestmentTimeline.objects.create(
                            start_time=start_time,
                            end_time=end_time,
                        )

                        # my_timer = threading.Timer(10.0, mytimer)
                        # my_timer.start()
                        my_timer = threading.Timer(60.0, mytimer)
                        my_timer.start()
                else:
                    FruitInvestmentTimeline.objects.create(
                        start_time=start_time,
                        end_time=end_time,
                    )

                    my_timer = threading.Timer(60.0, mytimer)
                    my_timer.start()

                is_fruit_investment_timeline_fruit_investment_timeline = FruitInvestmentTimeline.objects.all(
                ).order_by('-id')[0:1].values()
                fruit_investment_timeline_fruit_investment_timeline_data = list(
                    is_fruit_investment_timeline_fruit_investment_timeline)
                async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name,
                    {
                        "type": "chat.message",
                        "status": status,
                        "server_current_time": str(server_current_time),
                        "fruit_investment_timeline_fruit_investment_timeline_data": fruit_investment_timeline_fruit_investment_timeline_data,
                        "end_time": is_fruit_investment_timeline_fruit_investment_timeline[0]['end_time'],
                    }
                )

            FruitInvestmentTimelineSent()
            FruitInvestmentTimelineSent_timer = threading.Timer(
                70.0, FruitInvestmentTimelineSent)
            FruitInvestmentTimelineSent_timer.start()

    # Receive message from room group

    def chat_message(self, event):
        message = event
        # print(event)

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))


class P2PMessages(WebsocketConsumer):
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
        status = text_data_json["status"]

        if (status == 'AllMessageGet'):
            unique_id = text_data_json["unique_id"]
            print(unique_id, 'unique_id')
            all_p2p_messages = AllP2PMessage.objects.filter(
                unique_id=unique_id).values()

            all_p2p_messages = list(all_p2p_messages)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "all_p2p_messages": all_p2p_messages,
                }
            )
        elif (status == 'SentP2PMessage'):
            unique_id = text_data_json["unique_id"]
            message = text_data_json["message"]
            user_profile_id = text_data_json["user_profile_id"]
            other_user_profile_id = text_data_json["other_user_profile_id"]
            time = text_data_json["time"]

            all_p2p_messages = AllP2PMessage.objects.create(
                other_user_profile_id=other_user_profile_id,
                user_profile_id=user_profile_id,
                unique_id=unique_id,
                messages=message,
                time=time,
            )

            message = {
                "other_user_profile_id": other_user_profile_id,
                "user_profile_id": user_profile_id,
                "unique_id": unique_id,
                "messages": message,
                "time": time,
            }

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "status": status,
                    "message": message,
                }
            )

    # Receive message from room group

    def chat_message(self, event):
        message = event
        # print(event)

        # Send message to WebSocket
        self.send(text_data=json.dumps(event))




class TestChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

class TestChatConsumer1(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
