from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import *
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.crypto import get_random_string
# from .models import User,OTPToken
from authentication.models import *


from .register import register_phone_number_user
from random import randint


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


class LoadingOTView(GenericAPIView):

    serializer_class = PhoneNumberAuthSerializer

    def post(self, request):

        phone_number = request.data['number']
        otp = request.data['otp']
        print (phone_number,'.................')

        data = OTPToken.objects.filter(token_number=phone_number).order_by('-id')[0:1]
        
        data = list(data.values())
        responseData = {'status': 'success', 'data': data}


        # responseData = {'status': 'success'}


        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)










class CheckOTPAuthView(GenericAPIView):

    serializer_class = PhoneNumberAuthSerializer

    def post(self, request):

        phone_number = request.data['number']
        otp = request.data['otp']
        print (phone_number,'.................')

        data = OTPToken.objects.filter(token_number=phone_number).order_by('-id')[0:1]
        
        if data:
            data = data.values()
            data = data[0]['token']

            if data == otp:
                print ('okay................................')

            else:
                return Response({'err': 'Your OTP is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'err': 'Your OTP is not valid.'}, status=status.HTTP_400_BAD_REQUEST)

        responseData = {'status': 'success'}


        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class PhoneNumberAuthView(GenericAPIView):

    serializer_class = PhoneNumberAuthSerializer

    def post(self, request):

        phone_number = request.data['number']
        rider = request.data['rider']
        email =phone_number
        name ='kawsarkkhan'
        token_number = random_with_N_digits(4)

        print (phone_number,'.................')
        token_save = OTPToken.objects.create(token=token_number,token_number=phone_number,uidb64='')

        data = (register_phone_number_user(email,name,rider))
        data = list(data.values())

        print (data)


        responseData = {'status': 'success', 'data': data}


        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)









class GoogleSocialAuthView(GenericAPIView):

    serializer_class = GoogleSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an idtoken as from google to get user information

        """
        # print(request.data)

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class FacebookSocialAuthView(GenericAPIView):

    serializer_class = FacebookSocialAuthSerializer

    def post(self, request):
        """

        POST with "auth_token"

        Send an access token as from facebook to get user information

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = ((serializer.validated_data)['auth_token'])
        return Response(data, status=status.HTTP_200_OK)


class TwitterSocialAuthView(GenericAPIView):
    serializer_class = TwitterAuthSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
