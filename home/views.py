import datetime
import json
import timeit
# import googlemaps
from datetime import datetime
from itertools import chain

import cloudinary
import cloudinary.api
import cloudinary.uploader
import firebase_admin
from authentication.models import *
from django.conf import settings
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import credentials, messaging
from pyfcm import FCMNotification
from rest_framework import filters, generics, status
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import *
from .serializers import *

cloudinary.config(
    cloud_name="dwths7llt",
    api_key="229115325844843",
    api_secret="63PLbpuiklhXaApr7PadCvm_7lI"
)


# push_service = FCMNotification(api_key="AAAAE7z-Af4:APA91bHW9tBpU4835tbUqRiC9-tZh0LCq29UPwSFf3CxIJsXHY8r2airzRBU4y26gLOkgXBnEHf-6Lmgt9ao674yx7rs6LzHQkOOg3epYshxyud3GuQLv_bFn32foLIt0iNTyCcFKV1A")


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class UpdateProfileImagesView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data.getlist('image', None)
        productName = request.data.get('productName', None)
        productPrice = request.data.get('productPrice', None)
        productDis = request.data.get('productDis', None)

        print(productName, 'productName')

        if images:
            for image in images:
                image_url = cloudinary.uploader.upload(image)
                image_url = image_url["secure_url"]
        Product.objects.create(
            product_name=productName,
            product_price=productPrice,
            product_image=image_url,
            product_dis=productDis,

        )

        responseData = {
            'status': 'success',
        }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class AllProduct(APIView):
    def get(self, request, *args, **kwargs):

        data = Product.objects.all().values()
        data = list(data)

        responseData = {
            'status': 'success',
            "data": data
        }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class FollowersListView(APIView):
    def post(self, request, *args, **kwargs):
        usersId = request.data['usersId']

        data = list([])
        responseData = {'status': 'success', 'data': data, }

        return JsonResponse(responseData, status=HTTP_200_OK)
