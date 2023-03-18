
from django.contrib.auth import authenticate
from authentication.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed

# from shop.models import ShippingAddress
from authentication.models import Profile
from shop.models import ShippingAddress


def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 100000))
        return generate_username(random_username)


def register_social_user_with_details(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
            return {
                'id': registered_user.id,
                'username': registered_user.username,
                'email': registered_user.email,
                'personal_WS_ID': registered_user.personal_WS_ID,
                'tokens': registered_user.tokens()}
        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
    else:
        user = {
            'username': generate_username(name),
            'email': email,
            'password': 'kawsarkhan01794910680prantokhan57706swadexpress'}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.personal_WS_ID = str(email)+generate_username(name)
        user.save()
        new_user = authenticate(
            email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
        data = Profile()
        shipping_address_data = ShippingAddress()
        data.user_id = new_user.id
        new_user_create = "2023" + str(new_user.id)
        data.custom_id = int(new_user_create)
        # data.image = "images/users/user.png"
        data.save()
        shipping_address_data.user_id = new_user.id
        shipping_address_data.save()

        return {
            'id': new_user.id,
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens(),
            'personal_WS_ID': new_user.personal_WS_ID,
        }


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                # email=email, password=os.environ.get('SOCIAL_SECRET'))
                email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
            return {
                'id': registered_user.id,
                'username': registered_user.username,
                'email': registered_user.email,
                'personal_WS_ID': registered_user.personal_WS_ID,
                'tokens': registered_user.tokens()}
        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
    else:
        user = {
            'username': generate_username(name),
            'email': email,
            'password': 'kawsarkhan01794910680prantokhan57706swadexpress'}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.personal_WS_ID = str(email)+generate_username(name)
        user.save()
        new_user = authenticate(
            email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
        data = Profile()
        shipping_address_data = ShippingAddress()
        data.user_id = new_user.id
        new_user_create = "2023" + str(new_user.id)
        data.custom_id = int(new_user_create)
        # data.image = "images/users/user.png"
        data.save()
        shipping_address_data.user_id = new_user.id
        shipping_address_data.save()

        return {
            'id': new_user.id,
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens(),
            'personal_WS_ID': new_user.personal_WS_ID,
        }


def register_phone_number_user(email, name, provider):
    filtered_user_by_email = User.objects.filter(email=email)
    if filtered_user_by_email.exists():
        if filtered_user_by_email:
            registered_user = authenticate(
                # email=email, password=os.environ.get('SOCIAL_SECRET'))
                email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
            return {
                'id': registered_user.id,
                'username': registered_user.username,
                'email': registered_user.email,

                'personal_WS_ID': registered_user.personal_WS_ID,
                'tokens': registered_user.tokens()


            }
        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
    else:
        user = {
            'username': generate_username(name),
            'email': email,
            'password': 'kawsarkhan01794910680prantokhan57706swadexpress'}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.personal_WS_ID = str(email) + generate_username(name)
        user.auth_provider = provider
        user.save()
        new_user = authenticate(
            email=email, password="kawsarkhan01794910680prantokhan57706swadexpress")
        data = Profile()
        shipping_address_data = ShippingAddress()
        data.user_id = new_user.id
        data.user_id = new_user.id
        new_user_create = "2023" + str(new_user.id)
        data.custom_id = int(new_user_create)
        data.save()
        shipping_address_data.user_id = new_user.id
        shipping_address_data.save()

        return {
            'id': new_user.id,
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens(),
            'personal_WS_ID': new_user.personal_WS_ID,
        }
