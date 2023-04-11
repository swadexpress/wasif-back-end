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

# push_service = FCMNotification(api_key="AAAAE7z-Af4:APA91bHW9tBpU4835tbUqRiC9-tZh0LCq29UPwSFf3CxIJsXHY8r2airzRBU4y26gLOkgXBnEHf-6Lmgt9ao674yx7rs6LzHQkOOg3epYshxyud3GuQLv_bFn32foLIt0iNTyCcFKV1A")


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class CompetitionQualifiersDataView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        # this_month = datetime.datetime.now().month
        this_year = datetime.datetime.now().year

        this_month = '04'
        day_1 = "01"
        day_2 = "02"
        day_3 = "03"
        day_4 = "04"
        day_5 = "05"
        day_6 = "06"
        day_7 = "07"
        day_8 = "08"
        date_time_1 = str(day_1)+"-" + str(this_month)+"-" + str(this_year)
        date_time_2 = str(day_2)+"-" + str(this_month)+"-" + str(this_year)
        date_time_3 = str(day_3)+"-" + str(this_month)+"-" + str(this_year)
        date_time_4 = str(day_4)+"-" + str(this_month)+"-" + str(this_year)
        date_time_5 = str(day_5)+"-" + str(this_month)+"-" + str(this_year)
        date_time_6 = str(day_6)+"-" + str(this_month)+"-" + str(this_year)
        date_time_7 = str(day_7)+"-" + str(this_month)+"-" + str(this_year)
        date_time_8 = str(day_8)+"-" + str(this_month)+"-" + str(this_year)

        print(date_time_1, 'oay')

        # print(this_month, 'this_month')
        # print(day_1, 'this_day')


# =========================== day_1_data==========================
        day_1_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_1, time__month=this_month)
            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_1_data.append(new_data)
        day_1_data = sorted(day_1_data, key=lambda k: k['total_daimon_amount'])
        day_1_qualified_data = day_1_data[::-1][0:8]  # top 1-8 user data
        day_1_not_qualified_data = day_1_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_2_data==========================
        day_2_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_2, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_2_data.append(new_data)
        day_2_data = sorted(day_2_data, key=lambda k: k['total_daimon_amount'])
        day_2_qualified_data = day_2_data[::-1][0:8]  # top 1-8 user data
        day_2_not_qualified_data = day_2_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_3_data==========================
        day_3_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_3, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_3_data.append(new_data)
        day_3_data = sorted(day_3_data, key=lambda k: k['total_daimon_amount'])
        day_3_qualified_data = day_3_data[::-1][0:8]  # top 1-8 user data
        day_3_not_qualified_data = day_3_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_4_data==========================
        day_4_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_4, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_4_data.append(new_data)
        day_4_data = sorted(day_4_data, key=lambda k: k['total_daimon_amount'])
        day_4_qualified_data = day_4_data[::-1][0:8]  # top 1-8 user data
        day_4_not_qualified_data = day_4_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_5_data==========================
        day_5_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_5, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_5_data.append(new_data)
        day_5_data = sorted(day_5_data, key=lambda k: k['total_daimon_amount'])
        day_5_qualified_data = day_5_data[::-1][0:8]  # top 1-8 user data
        day_5_not_qualified_data = day_5_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_6_data==========================
        day_6_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_6, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_6_data.append(new_data)
        day_6_data = sorted(day_6_data, key=lambda k: k['total_daimon_amount'])
        day_6_qualified_data = day_6_data[::-1][0:8]  # top 1-8 user data
        day_6_not_qualified_data = day_6_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_7_data==========================
        day_7_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_7, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_7_data.append(new_data)
        day_7_data = sorted(day_7_data, key=lambda k: k['total_daimon_amount'])
        day_7_qualified_data = day_7_data[::-1][0:14]  # top 1-8 user data
        day_7_not_qualified_data = day_7_data[::-1][8:14]  # top 9-15 user data
        # print(day_1_data)

# =========================== day_8_data==========================
        day_8_data = []
        is_pre_month_host_agents = Profile.objects.all()
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.id, time__day=day_8, time__month=this_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i.id,
                    "user_id": i.user_id,
                    "fast_name": i.fast_name,
                    "last_name": i.last_name,
                    "image": i.image,
                    "custom_id": i.custom_id,
                }

                day_8_data.append(new_data)
        day_8_data = sorted(day_8_data, key=lambda k: k['total_daimon_amount'])
        day_8_qualified_data = day_8_data[::-1][0:8]  # top 1-8 user data
        day_8_not_qualified_data = day_8_data[::-1][8:14]  # top 9-15 user data


# ===================================Rounds=============================================

    #   ================Rounds -1===========
        round_1_data = day_1_data[::-1][0:8]
        round_1_data.extend(day_2_data[::-1][0:8] +
                            day_3_data[::-1][0:8] +
                            day_4_data[::-1][0:8] +
                            day_5_data[::-1][0:8] +
                            day_6_data[::-1][0:8] +
                            day_7_data[::-1][0:8] +
                            day_8_data[::-1][0:8]

                            )
        round_1_filter_data = []
        for i in list({v['profile_id']: v for v in round_1_data}.values()):
            print(i["total_daimon_amount"],
                  'total_daimon_amount', i["profile_id"])
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i['profile_id'], time__month=this_month)
            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i['profile_id'],
                    "user_id": i["user_id"],
                    "fast_name": i["fast_name"],
                    "last_name": i["last_name"],
                    "image": i["image"],
                    "custom_id": i["custom_id"],
                }
                round_1_filter_data.append(new_data)

            # print(sum(total_daimon_amount), 'total_daimon_amount----2')

        round_1_filter_data = sorted(
            round_1_filter_data, key=lambda k: k['total_daimon_amount'])
        round_1_filter_data = round_1_filter_data[::-1][0:63]
        # print(round_1_filter_data, 'round')


# ================================Rounds -1=======================================

        round_2_filter_data = []
        for i in list({v['profile_id']: v for v in round_2_filter_data}.values()):
            print(i["total_daimon_amount"],
                  'total_daimon_amount', i["profile_id"])
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i['profile_id'], time__month=this_month)
            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            if (sum(total_daimon_amount) > 0):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "profile_id": i['profile_id'],
                    "user_id": i["user_id"],
                    "fast_name": i["fast_name"],
                    "last_name": i["last_name"],
                    "image": i["image"],
                    "custom_id": i["custom_id"],
                }
                round_2_filter_data.append(new_data)

            # print(sum(total_daimon_amount), 'total_daimon_amount----2')

        round_2_filter_data = sorted(
            round_2_filter_data, key=lambda k: k['total_daimon_amount'])
        round_2_filter_data = round_2_filter_data[::-1][0:63]
        
        # x = [1, 2, 3,4,5,6,7,8,9,10]
        # y = [1, 2, 3,4,5,6,7,8,9,10]
        round_1_filter_update_data=[]
        for i, j in zip(round_1_filter_data[0::2], round_1_filter_data[1::2]):
            tow_user_data_customize ={
                'user_1':i,
                "user_2":j
            }
            round_1_filter_update_data.append(tow_user_data_customize)


            # print(str(i) + " / " + str(j))


        print(round_1_filter_update_data, 'round')








        responseData = {
            'status': 'success',
            "round_1_filter_update_data":round_1_filter_update_data,





            #  ========================================================================
            'day_1_qualified_data': day_1_qualified_data,
            'day_1_not_qualified_data': day_1_not_qualified_data,
            'day_2_qualified_data': day_2_qualified_data,
            'day_2_not_qualified_data': day_2_not_qualified_data,
            'day_3_qualified_data': day_3_qualified_data,
            'day_3_not_qualified_data': day_3_not_qualified_data,
            'day_4_qualified_data': day_4_qualified_data,
            'day_4_not_qualified_data': day_4_not_qualified_data,
            'day_5_qualified_data': day_5_qualified_data,
            'day_5_not_qualified_data': day_5_not_qualified_data,
            'day_6_qualified_data': day_6_qualified_data,
            'day_6_not_qualified_data': day_6_not_qualified_data,
            'day_7_qualified_data': day_7_qualified_data,
            'day_7_not_qualified_data': day_7_not_qualified_data,
            'day_8_qualified_data': day_8_qualified_data,
            'day_8_not_qualified_data': day_8_not_qualified_data,

            # ==================================================
            "date_time_1": date_time_1,
            "date_time_2": date_time_2,
            "date_time_3": date_time_3,
            "date_time_4": date_time_4,
            "date_time_5": date_time_5,
            "date_time_6": date_time_6,
            "date_time_7": date_time_7,
            "date_time_8": date_time_8,



        }

        return JsonResponse(responseData, status=HTTP_200_OK)


class HostAgentsUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        Id = request.data['id']
        userId = request.data['userId']
        joinUserId = request.data['joinUserId']
        status = request.data['status']

        # print(buyerUserId,'buyerUserId')

        buy_coin_from_agents_update = HostAgents.objects.filter(
            id=Id
        )
        buy_coin_from_agents_update.update(
            status=status
        )

        responseData = {'status': 'success'}

        return JsonResponse(responseData, status=HTTP_200_OK)


class HostAgentsCreateView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        userProfileId = request.data['userProfileId']
        agentUserId = request.data['agentUserId']
        agentProfileId = request.data['agentProfileId']
        status = ''
        isHostAgents = HostAgents.objects.filter(
            agent_user_id=agentUserId, join_user_id=userId)
        if (isHostAgents):
            status = 'errors'
            pass

        else:
            HostAgents.objects.create(
                agent_user_id=agentUserId,
                agent_user_profile_id=agentProfileId,
                join_user_id=userId,
                join_user_profile_id=userProfileId,
            )
            status = 'success'

        responseData = {'status': status}

        return JsonResponse(responseData, status=HTTP_200_OK)


class BuyCoinFromAgentsCreateUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        Id = request.data['id']
        userId = request.data['userId']
        buyerUserId = request.data['buyerUserId']
        status = request.data['status']

        # print(buyerUserId,'buyerUserId')

        buy_coin_from_agents_update = BuyCoinFromAgents.objects.filter(
            id=Id
        )
        buy_coin_from_agents_update.update(
            status=status
        )

        responseData = {'status': 'success'}

        return JsonResponse(responseData, status=HTTP_200_OK)


class BuyCoinFromAgentsCreateView(APIView):
    def post(self, request, *args, **kwargs):
        buyer_user = request.data['userId']
        buyer_user_profile = request.data['userProfileId']
        agent_user = request.data['agentUserId']
        agent_user_profile = request.data['agentProfileId']
        amount = request.data['amount']

        BuyCoinFromAgents.objects.create(
            buyer_user_id=buyer_user,
            buyer_user_profile_id=buyer_user_profile,
            agent_user_id=agent_user,
            agent_user_profile_id=agent_user_profile,
            amount=amount,


        )

        responseData = {'status': 'success'}

        return JsonResponse(responseData, status=HTTP_200_OK)


class MyRechargeView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        hostDataPending = BuyCoinFromAgents.objects.filter(
            agent_user_id=userId,
            status="Pending"
        ).order_by('-id').values(
            "id",
            "amount",
            "buyer_user_profile__id",
            "buyer_user_profile__fast_name",
            "buyer_user_profile__last_name",
            "buyer_user_profile__cover_image",
            "buyer_user_profile__image",
            "buyer_user_profile__custom_id",
            "buyer_user__id",
            "buyer_user__email",
            "buyer_user__username",
        )
        hostDataAccepted = BuyCoinFromAgents.objects.filter(
            agent_user_id=userId,
            status="Accepted"
        ).order_by('-id').values(
            "id",
            "amount",
            "buyer_user_profile__id",
            "buyer_user_profile__fast_name",
            "buyer_user_profile__last_name",
            "buyer_user_profile__cover_image",
            "buyer_user_profile__image",
            "buyer_user_profile__custom_id",
            "buyer_user__id",
            "buyer_user__email",
            "buyer_user__username",
        )
        hostDataCancel = BuyCoinFromAgents.objects.filter(
            agent_user_id=userId,
            status="Cancel"
        ).order_by('-id').values(
            "id",
            "amount",
            "buyer_user_profile__id",
            "buyer_user_profile__fast_name",
            "buyer_user_profile__last_name",
            "buyer_user_profile__cover_image",
            "buyer_user_profile__image",
            "buyer_user_profile__custom_id",
            "buyer_user__id",
            "buyer_user__email",
            "buyer_user__username",
        )

        hostDataPending = list(hostDataPending)
        hostDataAccepted = list(hostDataAccepted)
        hostDataCancel = list(hostDataCancel)

        responseData = {'status': 'success',

                        'hostDataPending': hostDataPending,
                        'hostDataAccepted': hostDataAccepted,
                        'hostDataCancel': hostDataCancel,

                        }

        return JsonResponse(responseData, status=HTTP_200_OK)


class HostDetailsDataView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        import datetime

        this_month = datetime.datetime.now().month
        pre_month = datetime.datetime.now().month - 1

        this_month_data = []
        is_this_month_host_agents = HostAgents.objects.filter(
            agent_user_id=userId)
        for i in is_this_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.join_user_profile.id, time__month=this_month)
            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            host_salary = 0
            agent_salary = 0
            if (sum(total_daimon_amount) >= 5000):
                host_salary = sum(total_daimon_amount)/250
                agent_salary = sum(total_daimon_amount)/1000
            if (sum(total_daimon_amount)):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "host_salary": host_salary,
                    "agent_salary": agent_salary,
                    "fast_name": i.join_user_profile.fast_name,
                    "last_name": i.join_user_profile.last_name,
                    "image": i.join_user_profile.image,
                    "custom_id": i.join_user_profile.custom_id,
                }

                this_month_data.append(new_data)
# =====================================================
        pre_month_data = []
        is_pre_month_host_agents = HostAgents.objects.filter(
            agent_user_id=userId)
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.join_user_profile.id, time__month=pre_month)

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            host_salary = 0
            agent_salary = 0
            if (sum(total_daimon_amount) >= 5000):
                host_salary = sum(total_daimon_amount)/250
                agent_salary = sum(total_daimon_amount)/1000
            if (sum(total_daimon_amount)):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "host_salary": host_salary,
                    "agent_salary": agent_salary,
                    "fast_name": i.join_user_profile.fast_name,
                    "last_name": i.join_user_profile.last_name,
                    "image": i.join_user_profile.image,
                    "custom_id": i.join_user_profile.custom_id,
                }

                pre_month_data.append(new_data)


# =====================================================
        today_data = []
        is_pre_month_host_agents = HostAgents.objects.filter(
            agent_user_id=userId)
        for i in is_pre_month_host_agents:
            isSentGifts = SentGifts.objects.filter(
                receive_user_profile=i.join_user_profile.id, time__day=datetime.datetime.now().strftime('%d'))

            total_daimon_amount = []
            for j in isSentGifts:
                total_daimon_amount.append(int(j.amount))

            host_salary = 0
            agent_salary = 0
            if (sum(total_daimon_amount) >= 5000):
                host_salary = sum(total_daimon_amount)/250
                agent_salary = sum(total_daimon_amount)/1000

            if (sum(total_daimon_amount)):
                new_data = {
                    "total_daimon_amount": sum(total_daimon_amount),
                    "host_salary": host_salary,
                    "agent_salary": agent_salary,
                    "fast_name": i.join_user_profile.fast_name,
                    "last_name": i.join_user_profile.last_name,
                    "image": i.join_user_profile.image,
                    "custom_id": i.join_user_profile.custom_id,
                }

                today_data.append(new_data)

        # print (isHostAgents,'isHostAgents')

        # print(hostDataPending, 'pa')

        # this_month_data = list(hostDataPending)
        # hostDataAccepted = list(hostDataAccepted)
        # hostDataCancel = list(hostDataCancel)

        responseData = {'status': 'success',
                        'this_month_data': this_month_data,
                        'pre_month_data': pre_month_data,
                        'today_data': today_data,
                        # 'hostDataAccepted': hostDataAccepted,
                        # 'hostDataCancel': hostDataCancel,

                        }

        return JsonResponse(responseData, status=HTTP_200_OK)


class HostDataView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']

        hostDataPending = HostAgents.objects.filter(
            agent_user_id=userId,
            status="Pending"
        ).order_by('-id').values(
            "id",
            "join_user_profile__id",
            "join_user_profile__fast_name",
            "join_user_profile__last_name",
            "join_user_profile__cover_image",
            "join_user_profile__image",
            "join_user_profile__custom_id",
            "join_user__id",
            "join_user__email",
            "join_user__username",
        )

        hostDataAccepted = HostAgents.objects.filter(
            agent_user_id=userId,
            status="Accepted"
        ).order_by('-id').values(
            "id",
            "join_user_profile__id",
            "join_user_profile__fast_name",
            "join_user_profile__last_name",
            "join_user_profile__cover_image",
            "join_user_profile__image",
            "join_user_profile__custom_id",
            "join_user__id",
            "join_user__email",
            "join_user__username",
        )

        hostDataCancel = HostAgents.objects.filter(
            agent_user_id=userId,
            status="Cancel"
        ).order_by('-id').values(
            "id",
            "join_user_profile__id",
            "join_user_profile__fast_name",
            "join_user_profile__last_name",
            "join_user_profile__cover_image",
            "join_user_profile__image",
            "join_user_profile__custom_id",
            "join_user__id",
            "join_user__email",
            "join_user__username",
        )

        hostDataPending = list(hostDataPending)
        hostDataAccepted = list(hostDataAccepted)
        hostDataCancel = list(hostDataCancel)

        responseData = {'status': 'success',

                        'hostDataPending': hostDataPending,
                        'hostDataAccepted': hostDataAccepted,
                        'hostDataCancel': hostDataCancel,

                        }

        return JsonResponse(responseData, status=HTTP_200_OK)


class RechargeAgentView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        data = Profile.objects.filter(user_id=userId, is_recharge_agent=True).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "country",
            "cover_image",
            "user__email",
            "user__username",
        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class HostAgentsView(APIView):
    def post(self, request, *args, **kwargs):
        userId = request.data['userId']
        data = Profile.objects.filter(is_host_agent=True).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",
            "user__email",
            "user__username",
        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


# =================================================================================================

class BannerImagesView(APIView):
    def get(self, request, *args, **kwargs):

        data = BannerImages.objects.all()

        data = list(data.values("image", 'name'))
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UploadBannerImagesAndVideosView(APIView):
    def post(self, request, *args, **kwargs):
        # caption = request.data.get('caption', None)
        images = request.data['image']
        name = request.data['name']
        print(request.data['image'], '.....')
        data = []
        image_url = cloudinary.uploader.upload(images)
        BannerImages.objects.create(
            name=name, image=image_url["secure_url"])
        responseData = {'status': 'success', 'data': "data"}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UserDetailsUpdateAdminView(APIView):
    def post(self, request, *args, **kwargs):

        userId = request.data['userId']
        fast_name = request.data['fastName']
        last_name = request.data['lastName']

        data = Profile.objects.filter(user_id=userId)
        data.update(
            fast_name=fast_name,
            last_name=last_name,
        )
        data = Profile.objects.filter(user_id=userId).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",
            "user__email",
            "user__username",


        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class UserDetailsAdminView(APIView):
    def post(self, request, *args, **kwargs):

        userId = request.data['userId']

        data = Profile.objects.filter(user_id=userId).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",
            "user__email",
            "user__username",


        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class AllUserListAdminView(APIView):
    def get(self, request, *args, **kwargs):

        data = Profile.objects.filter().order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",
            "user__email",
            "user__username",


        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class MyPostDelete(ListAPIView):
    def post(self, request, *args, **kwargs):

        postId = request.data['postId']
        data = Post.objects.filter(id=postId).delete()

        responseData = {
            'status': 'success',

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class RequestSendView(APIView):
    def post(self, request, *args, **kwargs):
        # proxy_dict = {
        #         "http"  : "http://127.0.0.1",
        #         "https" : "http://127.0.0.1",
        #         }
        # push_service = FCMNotification(api_key="AAAAE7z-Af4:APA91bHW9tBpU4835tbUqRiC9-tZh0LCq29UPwSFf3CxIJsXHY8r2airzRBU4y26gLOkgXBnEHf-6Lmgt9ao674yx7rs6LzHQkOOg3epYshxyud3GuQLv_bFn32foLIt0iNTyCcFKV1A")

        # registration_ids = ["cfxlxaTXTUCQj39gcgHBVt:APA91bFBw4MwC1dwfIyozVXYXdKulH7dn8aO_N-KgZTnU1TM_yNPoz_d_sEIZIhSaD062j4l5gifVRuLGl0y5mKBlucr5_Uyffp03qC6Y94QJFADCPT8QqTdOYlDefVgBMgKc-_jwd4k", ]
        # message_title = "Uber update"
        # message_body = "Hope you're having fun this weekend, don't forget to check today's news"
        # result = push_service.notify_multiple_devices(

        #     registration_ids=registration_ids,
        #       message_title=message_title,
        #         message_body=message_body,
        #         data ={"name":"kawsar khan"}

        #         )

        # cred = credentials.Certificate("/home/dulquer/LiveKit/orbitplug-back-end/home/peacegarden-ccbe4-firebase-adminsdk-q8oqd-a55b0951b4.json")
        # firebase_admin.initialize_app(cred)

        # message = messaging.MulticastMessage(
        # notification=messaging.Notification(
        # title="Title",
        # body="body line1\nbody line2"),
        # tokens=['e1X93H2WReGBZKBqr8_9L_:APA91bE4zCdyRkW5R1of3OjrlDVrTq5TiIcTOVehKdlNW56UsHR1hNExbzbPlWXIwlqk3VUNffrWfDCgPLQ3qUNoP_6NTVwHVepE5HGIhUHwdhfUQtz_Qm5foh8Qxp0UIUz2Gj2enmVy']
        # )
        # messaging.send_multicast(message)

        responseData = {'status': 'success', 'data': "data", }

        return JsonResponse(responseData, status=HTTP_200_OK)


class MyBannedListView(APIView):
    def post(self, request, *args, **kwargs):
        bandedUserList = request.data['bandedUserList']

        data = Profile.objects.filter(user__in=bandedUserList).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",

        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class MyRoomAdminListView(APIView):
    def post(self, request, *args, **kwargs):
        bandedUserList = request.data['bandedUserList']

        data = Profile.objects.filter(user__in=bandedUserList).order_by('-id').values(
            "id",
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",

        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class MyAllFriendListView(APIView):
    def post(self, request, *args, **kwargs):
        myUserId = request.data['myUserId']

        data = Profile.objects.all().order_by('-id').values(
            "user",
            "followers",
            "following",
            "custom_id",
            "about_me",
            "fast_name",
            "last_name",
            "gender",
            "phone",
            "address",
            "district",
            "division",
            "zip_code",
            "image",
            "cover_image",

        )

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class AllPostSearch(ListAPIView):
    def post(self, request, *args, **kwargs):

        print(request.data, 'dddddddddd')
        query = request.data['query']
        data = Post.objects.filter(Q(text__icontains=query))

        print(data)
        # results = Post.objects.filter(Q(text__icontains=query) | Q(intro__icontains=query) | Q(content__icontains=query))

        # following_users = list(request.user.profile.following.all())
        # following_users.append(request.user)
        # data = Post.objects.all().order_by('-created_at')
        # data = Post.objects.filter(user__in = following_users).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        if data:
            for i in data:
                full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
                fullName.append(full_name)
                profilePic.append(str(i.user.profile.image))
                profileId.append(str(i.user.profile.id))
                image = PostImages.objects.filter(post_id=int(i.id))
                image = image.values()
                images.append(list(image))
                like = i.likes.all()

                likeUserId = []

                for i in like:
                    likeUserId.append(i.id)

                like = (list(like))

                likes.append(likeUserId)
        data = list(data.values())

        responseData = {
            'status': 'success',
            'data': data,
            'userFullName': fullName,
            'profilePic': profilePic,
            'images': images,
            'likes': likes,
            "profileId": profileId

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


# class AllPostSearch(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'slug']


class CropImagesUploadView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data.getlist('image', None)
        MyUserId = request.data['MyUserId']

        if images:
            for image in images:
                check_profile = ProfileImages.objects.filter(user_id=MyUserId)
                if check_profile:
                    check_profile.delete()
                image_url = ProfileImages.objects.create(
                    user_id=MyUserId, image=image)
                image_url = image_url.image
                profile = Profile.objects.filter(user_id=MyUserId)

                profile.update(image=image_url)

        # data = list(data
        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class P2PMessageUniqueIdView(APIView):
    def post(self, request, *args, **kwargs):
        myUserId = request.data['myUserId']

        isdata = P2PMessageUniqueId.objects.filter(
            user_id=myUserId,).values(
            "user",
                "other_user",
                "uniqueId",
                "other_user__email",
                "other_user_profile__image",
                "other_user_profile__fast_name",
                "other_user_profile__last_name",
                "user_profile__fast_name",
                "user_profile__last_name",
                "user_profile__image",
        )
        isdata2 = P2PMessageUniqueId.objects.filter(other_user_id=myUserId).values(
            "user",
            "other_user",
            "uniqueId",
            "other_user__email",
            "other_user_profile__image",
            "other_user_profile__fast_name",
            "other_user_profile__last_name",
            "user_profile__fast_name",
            "user_profile__last_name",
            "user_profile__image",
        )

        data = []
        data.extend(isdata)
        data.extend(isdata2)
        print(data, 'otherUserIdotherUserIdotherUserIdotherUserId')

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class CreateP2PMessageUniqueIdView(APIView):
    def post(self, request, *args, **kwargs):
        myUserId = request.data['myUserId']
        otherUserId = request.data['otherUserId']
        uniqueId = request.data['uniqueId']
        print(myUserId, otherUserId, 'otherUserIdotherUserIdotherUserIdotherUserId')

        isdata = P2PMessageUniqueId.objects.filter(
            user_id=myUserId, other_user_id=otherUserId).values()
        isdata2 = P2PMessageUniqueId.objects.filter(
            user_id=otherUserId, other_user_id=myUserId).values()
        # data = []

        other_user_profile_id = Profile.objects.filter(
            user_id=otherUserId)

        user_profile_id = Profile.objects.filter(
            user_id=myUserId)

        print(other_user_profile_id[0].id,
              user_profile_id[0].id, 'user_profile_id')

        if isdata or isdata2:
            if isdata:
                data = isdata
            else:
                data = isdata2
        else:
            data = P2PMessageUniqueId.objects.create(
                user_id=myUserId,
                other_user_id=otherUserId,
                user_profile_id=user_profile_id[0].id,
                other_user_profile_id=other_user_profile_id[0].id,
                uniqueId=uniqueId,
            )

            data = P2PMessageUniqueId.objects.filter(id=data.id).values()

        data = list(data)
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)


class PostView(ListAPIView):
    def get(self, request, *args, **kwargs):
        following_users = list(request.user.profile.following.all())
        following_users.append(request.user)
        data = Post.objects.all().order_by('-created_at')
        # data = Post.objects.filter(user__in = following_users).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
            profileId.append(str(i.user.profile.id))
            image = PostImages.objects.filter(post_id=int(i.id))
            image = image.values()
            images.append(list(image))
            like = i.likes.all()

            likeUserId = []

            for i in like:
                likeUserId.append(i.id)

            like = (list(like))

            likes.append(likeUserId)
        data = list(data.values())

        responseData = {
            'status': 'success',
            'data': data,
            'userFullName': fullName,
            'profilePic': profilePic,
            'images': images,
            'likes': likes,
            "profileId": profileId

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class AddPostView(APIView):
    def post(self, request, *args, **kwargs):
        caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)

        creatPost = Post.objects.create(user=request.user, text=caption)
        if creatPost:

            for image in images:
                image_url = cloudinary.uploader.upload(image)
                PostImages.objects.create(
                    post_id=creatPost.id, image=image_url["secure_url"])

        return Response(status=HTTP_200_OK)


# <QueryDict: {'comment': ['test'], 'image': [<TemporaryUploadedFile: video-calling.mp4 (video/mp4)>]}>


class PostLikeDislikeLikeBackDeleteView(APIView):

    def post(self, request, *args, **kwargs):
        isLiked = request.data.get('isLiked', None)
        postId = request.data.get('postId', None)
# .....................Post  Liked ............................
        if isLiked == True:
            post = Post.objects.get(id=postId)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                try:
                    Like.objects.filter(user=request.user, post=post)[
                        0].delete()

                except:
                    pass

            return Response(status=HTTP_200_OK)


# ..................... Post Liked-Back ............................

        elif isLiked == False:

            post = Post.objects.get(id=postId)
            post.likes.add(request.user)
            Like.objects.create(user=request.user, post=post)
            return Response(status=HTTP_200_OK)

        return Response(status=HTTP_200_OK)


class FollowView(APIView):

    def post(self, request, *args, **kwargs):
        orther_user = request.data.get('otherUserId', None)
        following = get_object_or_404(User, id=orther_user)
        following.profile.followers.add(request.user)
        request.user.profile.following.add(following)
        return Response(status=HTTP_200_OK)


class UnfollowView(APIView):

    def post(self, request, *args, **kwargs):
        orther_user = request.data.get('otherUserId', None)
        following = get_object_or_404(User, id=orther_user)
        following.profile.followers.remove(request.user)
        request.user.profile.following.remove(following)
        return Response(status=HTTP_200_OK)


class SubCommentView(APIView):
    def post(self, request, *args, **kwargs):
        commentId = request.data.get('commentId', None)
        data = SubComment.objects.filter(comment_id=int(commentId))
        fullName = []
        profilePic = []
        for i in data:
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
        data = list(data.values())
        responseData = {'status': 'success', 'data': data,
                        'subCommentFullName': fullName, 'subProfilePic': profilePic}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class AddSubCommentView(APIView):

    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        comment = request.data.get('comment', None)

        obj = SubComment.objects.create(user=request.user,
                                        comment=Comment.objects.get(
                                            id=int(postId)),
                                        comm=comment,
                                        )

        return Response(status=HTTP_200_OK)


class AddCommentView(APIView):

    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        comment = request.data.get('comment', None)
        obj = Comment.objects.create(user=request.user,
                                     post=Post.objects.get(id=int(postId)),
                                     comm=comment,
                                     )
        return Response(status=HTTP_200_OK)


class CommentView(APIView):
    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        data = Comment.objects.filter(post_id=int(postId))
        fullName = []
        profilePic = []
        subComment = []
        for i in data:
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
            subcomment = SubComment.objects.filter(comment_id=int(i.id))
            subcomment = subcomment.values()
            subComment.append(list(subcomment))

        data = list(data.values())
        responseData = {
            'status': 'success',
            'data': data,
            'fullName': fullName,
            'profilePic': profilePic,
            'subComment': subComment
        }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class OtherOwnPostView(ListAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        OtherUserId = request.data.get('OtherUserId', None)

        data = Post.objects.filter(user_id=OtherUserId).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
            profileId.append(str(i.user.profile.id))
            image = PostImages.objects.filter(post_id=int(i.id))
            image = image.values()
            images.append(list(image))
            like = i.likes.all()

            likeUserId = []

            for i in like:
                likeUserId.append(i.id)

            like = (list(like))

            likes.append(likeUserId)
        data = list(data.values())

        responseData = {
            'status': 'success',
            'data': data,
            'userFullName': fullName,
            'profilePic': profilePic,
            'images': images,
            'likes': likes,
            "profileId": profileId

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class OtherPostView(ListAPIView):
    def post(self, request, *args, **kwargs):
        OtherUserPostId = request.data.get('OtherUserPostId', None)
        PostOtherUserId = request.data.get('PostOtherUserId', None)
        # print(request.data)

        # singelData1 = get_object_or_404(Post, id = OtherUserPostId)
        singelData = Post.objects.filter(id=OtherUserPostId)
        alldata = Post.objects.filter(
            user_id=PostOtherUserId).order_by('-created_at')

        alldata = alldata.filter(~Q(id=OtherUserPostId))
        print(singelData, 'results = Model.objects.exclude(a=True, x!=5)')

        data = list(chain(singelData, alldata))
        data1 = list(chain(singelData.values(), alldata.values()))
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            # print(i.values)
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
            profileId.append(str(i.user.profile.id))

            image = PostImages.objects.filter(post_id=int(i.id))

            image = image.values()
            images.append(list(image))
            like = i.likes.all()

            likeUserId = []

            for i in like:
                likeUserId.append(i.id)

            like = (list(like))

            likes.append(likeUserId)

        responseData = {
            'status': 'success',
            'data': data1,
            'userFullName': fullName,
            'profilePic': profilePic,
            'images': images,
            'likes': likes,
            "profileId": profileId

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class OwnPostView(ListAPIView):
    def get(self, request, *args, **kwargs):

        data = Post.objects.filter(user=request.user).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:

            print(i.user.profile.id)
            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.image))
            profileId.append(str(i.user.profile.id))

            image = PostImages.objects.filter(post_id=int(i.id))

            image = image.values()
            images.append(list(image))
            like = i.likes.all()

            likeUserId = []

            for i in like:
                likeUserId.append(i.id)

            like = (list(like))

            likes.append(likeUserId)
        data = list(data.values())

        print(data, 'datadatadata')

        responseData = {
            'status': 'success',
            'data': data,
            'userFullName': fullName,
            'profilePic': profilePic,
            'images': images,
            'likes': likes,
            "profileId": profileId

        }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class OtherUserProfileView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class OwnUserView(ListAPIView):
    # permission_classes = (IsAuthenticated )
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


# class SearchProfileView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = [ 'fast_name']


class ProfileView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class LikesView(APIView):
    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        data = Like.objects.filter(post_id=int(postId))

        fullName = []
        profilePic = []
        for i in data:

            full_name = i.user.profile.fast_name + " " + i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))

        data = list(data.values())

        responseData = {
            'status': 'success',
            'data': data,
            'fullName': fullName,
            'profilePic': profilePic,
        }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UpdateProfileCoverImagesView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data.getlist('image', None)
        # MyUserId = request.data.getlist('MyUserId', None)
        MyUserId = request.data['MyUserId']

        cloudinary.config(cloud_name='swadexpress',
                          api_key='357258774133196',
                          api_secret='DcCF1TZG2yXPOLlY0tr3Ok2yzug')

        if images:
            for image in images:
                image_url = cloudinary.uploader.upload(image)
                # print (d["url"],'............................ddd')
                # check_profile = ProfileImages.objects.filter(user_id=MyUserId)
                # if check_profile:
                #     check_profile.delete()
                # image_url = ProfileImages.objects.create(
                #     user_id=MyUserId, image=image)
                # image_url = image_url.image
                profile = Profile.objects.filter(user_id=MyUserId)

                profile.update(cover_image=image_url["secure_url"])

        # data = list(data
        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UpdateProfileImagesView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data.getlist('image', None)

        MyUserId = request.data['MyUserId']

        print(MyUserId, 'asdfjaskldfjal')

        cloudinary.config(cloud_name='swadexpress',
                          api_key='357258774133196',
                          api_secret='DcCF1TZG2yXPOLlY0tr3Ok2yzug')

        if images:
            for image in images:
                image_url = cloudinary.uploader.upload(image)
                # print (d["secure_url"],'............................ddd')
                # check_profile = ProfileImages.objects.filter(user_id=MyUserId)
                # if check_profile:
                #     check_profile.delete()
                # image_url = ProfileImages.objects.create(
                #     user_id=MyUserId, image=image)
                # image_url = image_url.image
                profile = Profile.objects.filter(user_id=MyUserId)

                profile.update(image=image_url["secure_url"])

        # data = list(data
        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UploadImagesAndVideosView(APIView):
    def post(self, request, *args, **kwargs):
        # caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)
        # type = request.data.getlist('type', None)
        # print(request.data['_parts'][0],'.....')
        print(request.data, '.....')
        # print(request.data['image'],'.....')
        data = []

        if images:
            for image in images:
                image_url = Images.objects.create(image=image)
                print(image_url.image)
                data.append(str(image_url.image))

        # data = list(data
        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UserProfileUpdateView(ListAPIView):
    permission_classes = (AllowAny, )

    def post(self, request,  *args, **kwargs):
        d = request.data

        userId = request.data['userId']
        fastName = request.data['fastName']
        lastName = request.data['lastName']
        email = request.data['email']
        gender = request.data['gender']
        dateOfBirth = request.data['dateOfBirth']
        country = request.data['country']
        language = request.data['language']

        data = Profile.objects.filter(user_id=userId)
        data = data.update(
            fast_name=fastName,
            last_name=lastName,
            gender=gender,
            date_of_birth=dateOfBirth,
            country=country,
            language=language,
            profile_email=email,
        )
        data = Profile.objects.filter(user_id=userId)

        data = list(data.values())

        responseData = {'status': 'success', 'data': data}
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UserProfileView(ListAPIView):
    permission_classes = (AllowAny, )

    def post(self, request,  *args, **kwargs):
        d = request.data
        userId = request.data['userId']

        data = Profile.objects.filter(user_id=userId).values()

        data = list(data)

        responseData = {'status': 'success', 'data': data}
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)
