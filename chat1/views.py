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


class CreateRoomTokenView(APIView):
    def post(self, request, *args, **kwargs):
        roomName = request.data['roomName']
        roomUniqueId = request.data['roomId']
        metaData = request.data['metaData']
        identity = request.data['identity']
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

        json_data = serializers.serialize("json", AllRooms.objects.filter(
            room_coustom_id=roomUniqueId))

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
        all_rooms_data = AllRooms.objects.all().values()
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
        is_rooms_create= AllRooms.objects.filter(id =is_rooms_create.id)
        for i in is_rooms_create:
            i.room_sup_admin_profile.add(adminProfileId)

        responseData = {'status': 'success', 'data': "data", }
        return JsonResponse(responseData, status=HTTP_200_OK)


def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})