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
            print(status, 'status')

            # ==== get data from app====
            my_user_id = text_data_json["my_user_id"]
            room_coustom_unique_id = text_data_json["room_coustom_unique_id"]
            room_name = text_data_json["room_name"]
            room_join_sit_position = text_data_json["room_join_sit_position"]
            room_join_join_uniq_id = text_data_json["room_join_join_uniq_id"]
            # ====IsJoinRoomsUsers model react in database=====
            IsJoinRoomsUsers.objects.filter(
                room_coustom_unique_id=room_coustom_unique_id
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
