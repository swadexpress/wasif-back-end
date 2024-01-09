import datetime
import django
from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from authentication.models import *
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField


class AllRooms(models.Model):
    room_admin_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='room_admin_user'
    )
    room_admin_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='room_admin_profile'
    )

    room_sup_admin_profile = models.ManyToManyField(
        Profile,
        related_name="room_sup_admin_profile",
        blank=True
    )

    room_mute_mic_user_profile_list = models.ManyToManyField(
        Profile,
        related_name="room_mute_mic_user_profile_list",
        blank=True
    )

    room_mute_mic_user_profile_banded_list = models.ManyToManyField(
        Profile,
        related_name="room_mute_mic_user_profile_banded_list",
        blank=True)
    room_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_coustom_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_welcome_message = models.CharField(
        max_length=200, blank=True, default="Welcome", null=True)
    room_tag = models.CharField(
        max_length=200, blank=True, default="Welcome", null=True)
    room_image = models.CharField(
        max_length=200, blank=True, default='https://scontent.fjsr1-1.fna.fbcdn.net/v/t1.15752-9/384546080_253840144277334_7690290843335446763_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=8cd0a2&_nc_eui2=AeH9N_TFM_IuYw9LHpdVdNLgO50S_JO2B0c7nRL8k7YHR4msuxw4H9cZewENUY-nVcfs0BFwtzCwTCY2vpJ2wZoP&_nc_ohc=gZfCKE6JZfQAX-iQX89&_nc_ht=scontent.fjsr1-1.fna&oh=03_AdSHQkZy6RbxyfRr_aulKoGF51KovdqOUKkiqkYvo0L5Jw&oe=6561E4B7', null=True)
    room_media_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_user_can_join = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_lock = models.BooleanField(blank=True, default=False, null=True)
    room_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    # ==============================================

    room_sit_1_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_1_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_1_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_2_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_2_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_2_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_3_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_3_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_3_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_4_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_4_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_4_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_5_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_5_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_5_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_6_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_6_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_6_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_7_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_7_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_7_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    room_sit_8_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_8_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_8_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    

    room_sit_9_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_9_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_9_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    

    room_sit_10_lock_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_10_password = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_sit_10_mic_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    # time = models.DateTimeField(auto_now_add=True)


class IsJoinRoomsUsers(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='room_is_join_user')
    room_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_coustom_unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_join_sit_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_join_join_uniq_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    # time = models.DateTimeField(auto_now_add=True)


class AllP2PMessage(models.Model):
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='p2p_messages_user_profile')
    other_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='p2p_messages_other_user_profile')
    messages = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    time = models.CharField(
        max_length=200, blank=True, default=None, null=True)


class AllSentedGifts(models.Model):
    gift_sent_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gift_sent_user')
    gift_receive_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='gift_receive_user')
    gift_sent_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='gift_sent_user_profile')
    gift_receive_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='gift_receive_user_profile')
    room_coustom_unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    gift_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    gift_amount = models.CharField(
        max_length=200, blank=True, default=None, null=True)


class FruitInvestment(models.Model):

    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='fruit_investment_user_profile')

    investment = models.CharField(
        max_length=20000, blank=True, default=None, null=True)

    profile_data = models.CharField(
        max_length=20000, blank=True, default=None, null=True)
    # time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)

class FruitInvestmentWinRanking(models.Model):
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='fruit_investment_amount_user_profile')
    win_amount = models.FloatField(
        max_length=200, blank=True, default=0.0, null=True)
    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)
class FruitInvestmentWinLoseRecord(models.Model):

    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='fruit_investment_win_or_lose_user_profile')
    amount = models.FloatField(
         blank=True, default=0.0, null=True)
    win_amount = models.FloatField(
         blank=True, default=0.0, null=True)
    rounds = models.IntegerField(
         blank=True, default=0, null=True)
    win_fruit_name = models.CharField(
        max_length=200, blank=True, default='', null=True)
    fruit_name = models.CharField(
        max_length=200, blank=True, default='', null=True)
    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)
class FruitInvestmentRound(models.Model):

    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='fruit_investment_record_user_profile')
    rounds = models.IntegerField(
         blank=True, default=0, null=True)
    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)



class FruitInvestmentForHistory(models.Model):

    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='fruit_investment_for_history_user_profile')

    investment = models.CharField(
        max_length=20000, blank=True, default=None, null=True)

    profile_data = models.CharField(
        max_length=20000, blank=True, default=None, null=True)

    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)


class FruitInvestmentTimeline(models.Model):
    start_time = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    end_time = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)



class AllPK(models.Model):
    pk_request_sent_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pk_request_sent_user')
    pk_request_receive_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='pk_request_receive_user')

    pk_request_sent_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='pk_request_sent_user_profile',)
    pk_request_receive_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='pk_request_receive_user_profile')

    pk_request_sent_user_balance = models.CharField(
        max_length=200, blank=True, default=0, null=True)
    pk_request_receive_user_balance = models.CharField(
        max_length=200, blank=True, default=0, null=True)

    pk_unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_coustom_unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    pk_time = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    pk_start_time = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    pk_end_time = models.CharField(
        max_length=200, blank=True, default=None, null=True)
