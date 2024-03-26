import os
import livekit
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core import serializers
import datetime
from authentication.models import *
from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from .models import *
# import googlemaps
from datetime import datetime
import timeit
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from itertools import chain
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json
from rest_framework import generics
from pyfcm import FCMNotification
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import status
import datetime

import firebase_admin
from firebase_admin import credentials, messaging

from rest_framework import filters
cloudinary.config(cloud_name='swadexpress',
                  api_key='357258774133196',
                  api_secret='DcCF1TZG2yXPOLlY0tr3Ok2yzug')
# Submodule path 'protocol': checked out 'f54aaadb8c8e9590d550808071e329311129d8f3'


live_kit_key = 'APIXSp9bDSvuNK2'
live_kit_secret = 'sRgGfseb3rT7WpizoNE9n9czL01LetSfvQ3zmda31JyC'
live_kit_host = "https://pgw.livekit.cloud"
client = livekit.RoomServiceClient(
    live_kit_host, live_kit_key, live_kit_secret)


def access_token():
    grant = livekit.VideoGrant(room_join=True, room="Test Room1")
    access_token = livekit.AccessToken(
        live_kit_key, live_kit_secret,
        grant=grant,
        identity="bob",
        name="Bob",
        metadata='kasarkna'
    )
    token = access_token.to_jwt()

    print(access_token, 'access_token')

# access_token()

#


def test_update_room_metadata():
    metadata = "some super duper metadata"
    client.update_room_metadata("Test Room1", metadata)
    print(client, 'client')


# test_update_room_metadata()


# def test_list_rooms(client, create_room):
#     rooms = client.list_rooms()
#     return rooms
#     # assert isinstance(rooms, list)
# print(test_list_rooms(client,''))
# # def createRoom():

# #     client.mute_published_track(
# #         room="kawsarkhan",
# #         identity="Bob",
# #         track_sid="<track sid>",
# #         muted=True,
# #     )

# grant = livekit.VideoGrant(room_join=True, room="user89872856088867554772")
# access_token = livekit.AccessToken(
#     live_kit_key, live_kit_secret,
#     grant=grant,
#     identity="bob",
#     name="metaData",
#     metadata="metaData"
# )
# token = access_token.to_jwt()

class BuyVIPView(APIView):
    def post(self, request, *args, **kwargs):

        user_profile_id = request.data['user_profile_id']
        name = request.data['name']
        per_day_renewal = request.data['per_day_renewal']
        price = request.data['price']

        VIP.objects.create(
            user_profile_id=user_profile_id,
            name=name,
            price=price,
            per_day_renewal=per_day_renewal,
        )

        responseData = {
            'status': 'success',
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class VIPView(APIView):
    def post(self, request, *args, **kwargs):

        user_profile_id = request.data['user_profile_id']

        vip_data = VIP.objects.filter(user_profile_id=user_profile_id).values(
            "id",
            "user_profile",
            "name",
            "price",
            "per_day_renewal",

        )

        responseData = {
            'status': 'success',
            'vip_data': list(vip_data)
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class VIPListView(APIView):
    def post(self, request, *args, **kwargs):

        user_profile_id = request.data['user_profile_id']

        vip_data = VIP.objects.filter(user_profile_id=user_profile_id).values(
            "id",
            "user_profile",
            "name",
            "price",
            "per_day_renewal",

        )

        responseData = {
            'status': 'success',
            'vip_data': list(vip_data)
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class UsedBuyVIPView(APIView):
    def post(self, request, *args, **kwargs):
        vip_name = request.data['vip_name']
        user_profile_id = request.data['user_profile_id']
        profile_data = Profile.objects.filter(id=user_profile_id)
        profile_data.update(is_vip=vip_name)
        json_data = serializers.serialize(
            "json", profile_data)
        profile_id = [i['pk'] for i in json.loads(json_data)]
        data = [i['fields'] for i in json.loads(json_data)]
        data[0]['id'] = profile_id[0]
        data = list(data)

        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, status=HTTP_200_OK)


class RakingTodayView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.datetime.today()

        fruit_investment_for_history_data = FruitInvestmentWinRanking.objects.filter(
            time__date=today
        ).values(
            'id',

            "user_profile__fast_name",
            "user_profile__last_name",
            "user_profile__image",
            "user_profile__coin",
            "user_profile__diamond",
            "user_profile__custom_id",
            "win_amount",

        )
        fruit_investment_for_history_data = list(
            fruit_investment_for_history_data)

        responseData = {
            'status': 'success',
            'fruit_investment_for_history_data': fruit_investment_for_history_data,

        }
        return JsonResponse(responseData, status=HTTP_200_OK)

class RakingTodayForFruitsLoopView(APIView):
    def get(self, request, *args, **kwargs):
        today = datetime.datetime.today()

        fruit_investment_for_history_data = FruitLoopInvestmentWinRanking.objects.filter(
            time__date=today
        ).values(
            'id',

            "user_profile__fast_name",
            "user_profile__last_name",
            "user_profile__image",
            "user_profile__coin",
            "user_profile__diamond",
            "user_profile__custom_id",
            "win_amount",

        )
        fruit_investment_for_history_data = list(
            fruit_investment_for_history_data)

        responseData = {
            'status': 'success',
            'fruit_investment_for_history_data': fruit_investment_for_history_data,

        }
        return JsonResponse(responseData, status=HTTP_200_OK)





class UserRecordView(APIView):
    def post(self, request, *args, **kwargs):
        today = datetime.datetime.today()
        weekly = datetime.datetime.now()-datetime.timedelta(days=7)
        user_profile_id = request.data['user_profile_id']
        fruit_investment_round_data = FruitInvestmentRound.objects.filter(
            time__date=today,
            user_profile_id=user_profile_id
        ).order_by('-id')
        fruit_investment_win_lose_record_data_list = []
        today_total_win_amount = []
        if fruit_investment_round_data:
            for i in fruit_investment_round_data:
                # print(i.rounds)

                fruit_investment_win_lose_record_data = FruitInvestmentWinLoseRecord.objects.filter(
                    user_profile_id=user_profile_id,
                    rounds=i.rounds,
                    time__date=today,
                ).order_by('-id').values(
                    'id',
                    "user_profile__fast_name",
                    "user_profile__last_name",
                    "user_profile__image",
                    "user_profile__coin",
                    "user_profile__diamond",
                    "user_profile__custom_id",
                    "amount",
                    "win_amount",
                    "fruit_name",
                    "rounds",
                    "win_fruit_name",

                )

                if fruit_investment_win_lose_record_data:
                    fruit_investment_win_lose_record_data_list.append(
                        list(fruit_investment_win_lose_record_data))
                    today_total_win_amount.append(
                        int(fruit_investment_win_lose_record_data[0]['win_amount']))

        # ===============================Weekly==========================

        fruit_investment_round_weekly_data = FruitInvestmentRound.objects.filter(
            time__gte=weekly,
            user_profile_id=user_profile_id
        ).order_by('-id')
        fruit_investment_win_lose_record_weekly_data_list = []
        today_total_win_weekly_amount = []
        if fruit_investment_round_weekly_data:
            for i in fruit_investment_round_weekly_data:
                # print(i.rounds)

                fruit_investment_win_lose_record_weekly_data = FruitInvestmentWinLoseRecord.objects.filter(
                    user_profile_id=user_profile_id,
                    rounds=i.rounds,
                    time__gte=weekly,
                ).order_by('-id').values(
                    'id',
                    "user_profile__fast_name",
                    "user_profile__last_name",
                    "user_profile__image",
                    "user_profile__coin",
                    "user_profile__diamond",
                    "user_profile__custom_id",
                    "amount",
                    "win_amount",
                    "fruit_name",
                    "rounds",
                    "win_fruit_name",

                )

                if fruit_investment_win_lose_record_weekly_data:
                    fruit_investment_win_lose_record_weekly_data_list.append(
                        list(fruit_investment_win_lose_record_weekly_data))
                    today_total_win_weekly_amount.append(
                        int(fruit_investment_win_lose_record_weekly_data[0]['win_amount']))

        responseData = {
            'status': 'success',
            'fruit_investment_win_lose_record_data': fruit_investment_win_lose_record_data_list,
            'fruit_investment_win_lose_record_weekly_data': fruit_investment_win_lose_record_weekly_data_list,
            "today_total_win_amount": sum(today_total_win_amount),
            "today_total_win_amount": sum(today_total_win_weekly_amount),

        }
        return JsonResponse(responseData, status=HTTP_200_OK)

class UserRecordForFruitsLoopView(APIView):
    def post(self, request, *args, **kwargs):
        today = datetime.datetime.today()
        weekly = datetime.datetime.now()-datetime.timedelta(days=7)
        user_profile_id = request.data['user_profile_id']
        fruit_investment_round_data = FruitLoopInvestmentRound.objects.filter(
            time__date=today,
            user_profile_id=user_profile_id
        ).order_by('-id')
        fruit_investment_win_lose_record_data_list = []
        today_total_win_amount = []
        if fruit_investment_round_data:
            for i in fruit_investment_round_data:
                # print(i.rounds)

                fruit_investment_win_lose_record_data = FruitInvestmentWinLoseRecord.objects.filter(
                    user_profile_id=user_profile_id,
                    rounds=i.rounds,
                    time__date=today,
                ).order_by('-id').values(
                    'id',
                    "user_profile__fast_name",
                    "user_profile__last_name",
                    "user_profile__image",
                    "user_profile__coin",
                    "user_profile__diamond",
                    "user_profile__custom_id",
                    "amount",
                    "win_amount",
                    "fruit_name",
                    "rounds",
                    "win_fruit_name",

                )

                if fruit_investment_win_lose_record_data:
                    fruit_investment_win_lose_record_data_list.append(
                        list(fruit_investment_win_lose_record_data))
                    today_total_win_amount.append(
                        int(fruit_investment_win_lose_record_data[0]['win_amount']))

        # ===============================Weekly==========================

        fruit_investment_round_weekly_data = FruitInvestmentRound.objects.filter(
            time__gte=weekly,
            user_profile_id=user_profile_id
        ).order_by('-id')
        fruit_investment_win_lose_record_weekly_data_list = []
        today_total_win_weekly_amount = []
        if fruit_investment_round_weekly_data:
            for i in fruit_investment_round_weekly_data:
                # print(i.rounds)

                fruit_investment_win_lose_record_weekly_data = FruitInvestmentWinLoseRecord.objects.filter(
                    user_profile_id=user_profile_id,
                    rounds=i.rounds,
                    time__gte=weekly,
                ).order_by('-id').values(
                    'id',
                    "user_profile__fast_name",
                    "user_profile__last_name",
                    "user_profile__image",
                    "user_profile__coin",
                    "user_profile__diamond",
                    "user_profile__custom_id",
                    "amount",
                    "win_amount",
                    "fruit_name",
                    "rounds",
                    "win_fruit_name",

                )

                if fruit_investment_win_lose_record_weekly_data:
                    fruit_investment_win_lose_record_weekly_data_list.append(
                        list(fruit_investment_win_lose_record_weekly_data))
                    today_total_win_weekly_amount.append(
                        int(fruit_investment_win_lose_record_weekly_data[0]['win_amount']))

        responseData = {
            'status': 'success',
            'fruit_investment_win_lose_record_data': fruit_investment_win_lose_record_data_list,
            'fruit_investment_win_lose_record_weekly_data': fruit_investment_win_lose_record_weekly_data_list,
            "today_total_win_amount": sum(today_total_win_amount),
            "today_total_win_amount": sum(today_total_win_weekly_amount),

        }
        return JsonResponse(responseData, status=HTTP_200_OK)





class UserSevenDaysRecordView(APIView):
    def post(self, request, *args, **kwargs):
        today = datetime.datetime.today()
        user_profile_id = request.data['user_profile_id']
        fruit_investment_round_data = FruitInvestmentRound.objects.filter(
            time__date=today,
            user_profile_id=user_profile_id
        ).order_by('-id')
        fruit_investment_win_lose_record_data_list = []
        today_total_win_amount = []
        if fruit_investment_round_data:
            for i in fruit_investment_round_data:
                print(i.rounds)

                fruit_investment_win_lose_record_data = FruitInvestmentWinLoseRecord.objects.filter(
                    user_profile_id=user_profile_id,
                    rounds=i.rounds,
                    time__date=today,
                ).order_by('-id').values(
                    'id',
                    "user_profile__fast_name",
                    "user_profile__last_name",
                    "user_profile__image",
                    "user_profile__coin",
                    "user_profile__diamond",
                    "user_profile__custom_id",
                    "amount",
                    "win_amount",
                    "fruit_name",
                    "rounds",
                    "win_fruit_name",

                )

                if fruit_investment_win_lose_record_data:
                    fruit_investment_win_lose_record_data_list.append(
                        list(fruit_investment_win_lose_record_data))
                    today_total_win_amount.append(
                        int(fruit_investment_win_lose_record_data[0]['win_amount']))
        responseData = {
            'status': 'success',
            'fruit_investment_win_lose_record_data': fruit_investment_win_lose_record_data_list,
            "today_total_win_amount": sum(today_total_win_amount),

        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class ExchangeCoinToDaimondView(APIView):
    def post(self, request, *args, **kwargs):
        user_profile_id = request.data['user_profile_id']
        amounts = request.data['amounts']

        profile_data = Profile.objects.filter(
            id=user_profile_id)

        profile_data.update(
            coin=float(profile_data[0].coin) + (float(amounts)/2),
            diamond=float(profile_data[0].diamond) - float(amounts)
        )

        gift_receive_user_profile_data = serializers.serialize(
            "json", profile_data)
        gift_receive_user_profile_id = [
            i['pk'] for i in json.loads(gift_receive_user_profile_data)]
        gift_receive_user_profile_data = [
            i['fields'] for i in json.loads(gift_receive_user_profile_data)]
        gift_receive_user_profile_data[0]['id'] = gift_receive_user_profile_id[0]
        gift_receive_user_profile_data = list(
            gift_receive_user_profile_data)

        responseData = {
            'status': 'success',
            'profile_data': list(gift_receive_user_profile_data),
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class UserReceiveGiftsView(APIView):
    def post(self, request, *args, **kwargs):
        user_profile_id = request.data['user_profile_id']
        all_sented_gifts_data = AllSentedGifts.objects.filter(
            gift_receive_user_profile_id=user_profile_id
        ).values(
            'gift_sent_user',
            'gift_receive_user',
            'gift_sent_user_profile',
            'gift_receive_user_profile',
            'room_coustom_unique_id',
            'gift_name',
            'gift_amount',
        )

        print(all_sented_gifts_data, '............')

        responseData = {
            'status': 'success',
            'all_sented_gifts_data': list(all_sented_gifts_data),
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class RoomGiftSentHistoryView(APIView):
    def post(self, request, *args, **kwargs):
        today = datetime.datetime.today()
        weekly = datetime.datetime.now()-datetime.timedelta(days=7)
        _monthly = datetime.datetime.now()-datetime.timedelta(days=28)
        room_coustom_unique_id = request.data['room_coustom_unique_id']
        all_sented_gifts_user_id_data = AllSentedGifts.objects.filter(
            room_coustom_unique_id=room_coustom_unique_id,
            time__date=today,

        ).values(
            'gift_sent_user',
            'gift_receive_user',
            'gift_sent_user_profile',
            'gift_receive_user_profile',
            'room_coustom_unique_id',
            'gift_name',
            'gift_amount',
        )

        all_sented_gifts_user_profile_id = []
        for i in all_sented_gifts_user_id_data:
            if i['gift_sent_user'] not in all_sented_gifts_user_profile_id:
                all_sented_gifts_user_profile_id.append(i['gift_sent_user'])
        all_sented_gifts_filter_data = []

        for i in all_sented_gifts_user_profile_id:
            all_sented_gifts_data = AllSentedGifts.objects.filter(
                gift_sent_user_id=i,
                time__date=today,
            ).values(
                'id',
                'gift_sent_user',
                'gift_receive_user',
                'gift_sent_user_profile',
                'gift_sent_user_profile__fast_name',
                'gift_sent_user_profile__last_name',
                'gift_sent_user_profile__id',
                'gift_sent_user_profile__user',
                'gift_sent_user_profile__image',
                'gift_receive_user_profile',
                'room_coustom_unique_id',
                'gift_name',
                'gift_amount',
            )

            total_gift_sent_amounts = []
            print(all_sented_gifts_data, 'all_sented_gifts_data')
            for j in all_sented_gifts_data:
                total_gift_sent_amounts.append(int(j['gift_amount']))

            all_sented_gifts_filter_data.append({
                "all_gifts_total_amount": sum(total_gift_sent_amounts),
                'user_details': all_sented_gifts_data[0]
            })

# =======================================================

        all_sented_gifts_user_id_data_weekly = AllSentedGifts.objects.filter(
            room_coustom_unique_id=room_coustom_unique_id,
            time__gte=weekly,

        ).values(
            'gift_sent_user',
            'gift_receive_user',
            'gift_sent_user_profile',
            'gift_receive_user_profile',
            'room_coustom_unique_id',
            'gift_name',
            'gift_amount',
        )

        print(all_sented_gifts_user_id_data_weekly,
              'all_sented_gifts_user_id_data_weekly')

        all_sented_gifts_user_profile_id_weekly = []

        for i in all_sented_gifts_user_id_data_weekly:

            if i['gift_sent_user'] not in all_sented_gifts_user_profile_id_weekly:
                all_sented_gifts_user_profile_id_weekly.append(
                    i['gift_sent_user'])
        all_sented_gifts_filter_data_weekly = []

        for i in all_sented_gifts_user_profile_id_weekly:
            all_sented_gifts_data_weekly = AllSentedGifts.objects.filter(
                gift_sent_user_id=i,
                time__gte=weekly,
            ).values(
                'id',
                'gift_sent_user',
                'gift_receive_user',
                'gift_sent_user_profile',
                'gift_sent_user_profile__fast_name',
                'gift_sent_user_profile__last_name',
                'gift_sent_user_profile__id',
                'gift_sent_user_profile__user',
                'gift_sent_user_profile__image',
                'gift_receive_user_profile',
                'room_coustom_unique_id',
                'gift_name',
                'gift_amount',
            )

            total_gift_sent_amounts_weekly = []

            for j in all_sented_gifts_data_weekly:
                total_gift_sent_amounts_weekly.append(int(j['gift_amount']))

            all_sented_gifts_filter_data_weekly.append({
                "all_gifts_total_amount": sum(total_gift_sent_amounts_weekly),
                'user_details': all_sented_gifts_data_weekly[0]
            })

        # ================================Monthly=========================

        all_sented_gifts_user_id_data_monthly = AllSentedGifts.objects.filter(
            room_coustom_unique_id=room_coustom_unique_id,
            time__gte=_monthly,

        ).values(
            'gift_sent_user',
            'gift_receive_user',
            'gift_sent_user_profile',
            'gift_receive_user_profile',
            'room_coustom_unique_id',
            'gift_name',
            'gift_amount',
        )


        all_sented_gifts_user_profile_id_monthly = []
        for i in all_sented_gifts_user_id_data_monthly:

            if i['gift_sent_user'] not in all_sented_gifts_user_profile_id_monthly:
                all_sented_gifts_user_profile_id_monthly.append(
                    i['gift_sent_user'])
        all_sented_gifts_filter_data_monthly = []

        for i in all_sented_gifts_user_profile_id_monthly:
            all_sented_gifts_data_monthly = AllSentedGifts.objects.filter(
                gift_sent_user_id=i,
                time__gte=_monthly,
            ).values(
                'id',
                'gift_sent_user',
                'gift_receive_user',
                'gift_sent_user_profile',
                'gift_sent_user_profile__fast_name',
                'gift_sent_user_profile__last_name',
                'gift_sent_user_profile__id',
                'gift_sent_user_profile__user',
                'gift_sent_user_profile__image',
                'gift_receive_user_profile',
                'room_coustom_unique_id',
                'gift_name',
                'gift_amount',
            )

            total_gift_sent_amounts_monthly = []

            for j in all_sented_gifts_data_monthly:
                total_gift_sent_amounts_monthly.append(int(j['gift_amount']))

            all_sented_gifts_filter_data_monthly.append({
                "all_gifts_total_amount": sum(total_gift_sent_amounts_monthly),
                'user_details': all_sented_gifts_data_monthly[0]
            })
            sorted_all_sented_gifts_filter_data_monthly =[]
            sorted_all_sented_gifts_filter_data_weekly =[]
            sorted_all_sented_gifts_filter_data =[]

            sorted_all_sented_gifts_filter_data_monthly = sorted(all_sented_gifts_filter_data_monthly, key=lambda x: x["all_gifts_total_amount"])
            sorted_all_sented_gifts_filter_data_weekly = sorted(all_sented_gifts_filter_data_weekly, key=lambda x: x["all_gifts_total_amount"])
            sorted_all_sented_gifts_filter_data = sorted(all_sented_gifts_filter_data, key=lambda x: x["all_gifts_total_amount"])


           



        responseData = {
            'status': 'success',
            'all_sented_gifts_filter_data': sorted_all_sented_gifts_filter_data,
            'all_sented_gifts_filter_data_weekly': sorted_all_sented_gifts_filter_data_weekly,
            'all_sented_gifts_filter_data_monthly': sorted_all_sented_gifts_filter_data_monthly,
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class CreateRoomTokenView(APIView):
    def post(self, request, *args, **kwargs):
        roomName = request.data['roomName']
        roomUniqueId = request.data['roomId']
        metaData = request.data['metaData']
        identity = request.data['identity']
        userProfileId = request.data['userProfileId']
        print(roomUniqueId, 'roomUniqueId')
        grant = livekit.VideoGrant(
            room_join=True,
            can_publish=True,
            room=roomUniqueId,
        )
        access_token = livekit.AccessToken(
            live_kit_key, live_kit_secret,
            grant=grant,
            identity=identity,
            name=metaData,
            metadata=metaData

        )
        token = access_token.to_jwt()
        all_joinded_user_profile_data = AllRooms.objects.filter(
            room_coustom_id=roomUniqueId)
        is_all_joinded_user_profile_data = all_joinded_user_profile_data.filter(
            room_all_joinded_user_profile=userProfileId
        )
        if not is_all_joinded_user_profile_data:
            all_joinded_user_profile_data[0].room_all_joinded_user_profile.add(
                userProfileId
            )

            print(is_all_joinded_user_profile_data, 'not.........not')

        print(is_all_joinded_user_profile_data,
              'is_all_joinded_user_profile_data')

        json_data = serializers.serialize(
            "json", all_joinded_user_profile_data)

        profile_id = [i['pk'] for i in json.loads(json_data)]
        data = [i['fields'] for i in json.loads(json_data)]
        # add profile  id
        data[0]['id'] = profile_id[0]

        is_join_rooms_users_data = IsJoinRoomsUsers.objects.filter(
            room_coustom_unique_id=roomUniqueId).values()
        is_join_rooms_users_data = list(is_join_rooms_users_data)

        room_details = list(data)

        #  =====Create user room token for join Livekit server room=====
        data = {
            "token": token,
            "room_details": room_details,
            "is_join_rooms_users_data": is_join_rooms_users_data,

        }

        responseData = {'status': 'success', 'data': data, }
        return JsonResponse(responseData, status=HTTP_200_OK)


class AllRoomsView(APIView):
    def get(self, request, *args, **kwargs):
        all_rooms_data = AllRooms.objects.all()
        all_rooms_data = serializers.serialize("json", all_rooms_data)
        all_rooms_data = [i['fields'] for i in json.loads(all_rooms_data)]

        print(all_rooms_data, 'all_rooms_data')
        all_livekit_server_rooms = client.list_rooms()
        data = []
        server_filter_data = []
        for i in range(len(all_rooms_data)):

            for j in range(len(all_livekit_server_rooms)):
                if (all_livekit_server_rooms[j].name == all_rooms_data[i]['room_coustom_id']):
                    server_filter_data.append(all_rooms_data[i])

            update_data = (all_rooms_data[i], {"numParticipants": 'test'})
            data.append(update_data)

        all_rooms_data = list(data)
        all_livekit_server_rooms = list(all_livekit_server_rooms)
        server_filter_data = list(server_filter_data)
        all_livekit_server_rooms = json.dumps(
            all_livekit_server_rooms, default=str)
        print(all_livekit_server_rooms, 'all_livekit_server_rooms')
        responseData = {
            'status': 'success',

            'data': all_rooms_data,
            'all_livekit_server_rooms': server_filter_data,
            'server_filter_data': server_filter_data,


        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class AllJoinedRoomsView(APIView):
    def post(self, request, *args, **kwargs):
        user_profile_id = request.data['user_profile_id']
        all_rooms_data = AllRooms.objects.filter(
            room_all_joinded_user_profile=user_profile_id
        )
        all_rooms_data = serializers.serialize("json", all_rooms_data)
        all_rooms_data = [i['fields'] for i in json.loads(all_rooms_data)]

        print(all_rooms_data, 'all_rooms_data')
        all_livekit_server_rooms = client.list_rooms()
        data = []
        server_filter_data = []
        for i in range(len(all_rooms_data)):

            for j in range(len(all_livekit_server_rooms)):
                if (all_livekit_server_rooms[j].name == all_rooms_data[i]['room_coustom_id']):
                    server_filter_data.append(all_rooms_data[i])

            update_data = (all_rooms_data[i], {"numParticipants": 'test'})
            server_filter_data.append(update_data)

        server_filter_data = list(server_filter_data)

        responseData = {
            'status': 'success',
            'data': server_filter_data,
        }
        return JsonResponse(responseData, status=HTTP_200_OK)


class MyRoomsView(APIView):
    def post(self, request, *args, **kwargs):
        user_id = request.data['user_id']
        my_rooms_data = AllRooms.objects.filter(
            room_admin_user_id=user_id).values()

        my_rooms_data = list(my_rooms_data)
        responseData = {
            'status': 'success',
            'my_rooms_data': my_rooms_data,
        }
        return JsonResponse(responseData, status=HTTP_200_OK)
        return JsonResponse(responseData, status=HTTP_200_OK)


class CreateRoomView(APIView):
    def post(self, request, *args, **kwargs):
        roomName = request.data['roomName']
        roomUniqueId = request.data['roomUniqueId']
        roomPercipientTotalJoin = request.data['roomPercipientTotalJoin']
        roomImage = request.data['roomImage']
        customId = request.data['customId']
        adminProfileId = request.data['adminProfileId']
        roomVideoAndAudioStatus = request.data['roomVideoAndAudioStatus']
        #  =====Create Livekit server room=====
        metadata = {
            'roomName': roomName,
            'roomUniqueId': roomUniqueId,
            'roomPercipientTotalJoin': roomPercipientTotalJoin,
            'roomImage': roomImage,
            'adminProfileId': adminProfileId,
            'roomVideoAndAudioStatus': roomVideoAndAudioStatus,

        }
        client.create_room(
            name=roomUniqueId,
            empty_timeout=20 * 60,
            max_participants=100000,


        )
        is_rooms_create = AllRooms.objects.create(
            room_admin_user_id=request.user.id,
            room_admin_profile_id=adminProfileId,
            room_name=roomName,
            room_coustom_id=roomUniqueId,
            room_image=roomImage,
            room_media_status=roomVideoAndAudioStatus,
            room_user_can_join=roomPercipientTotalJoin,
        )
        is_rooms_create = AllRooms.objects.filter(id=is_rooms_create.id)
        for i in is_rooms_create:
            i.room_sup_admin_profile.add(adminProfileId)

        responseData = {'status': 'success', 'data': "data", }
        return JsonResponse(responseData, status=HTTP_200_OK)


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
