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
        User, on_delete=models.CASCADE, related_name='room_admin_user')
   
    room_admin_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='room_admin_profile')
   
   
    room_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_coustom_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_welcome_message = models.CharField(
        max_length=200, blank=True, default="Welcome", null=True)
    room_tag = models.CharField(
        max_length=200, blank=True, default="Welcome", null=True)
    room_image = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_media_status = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_user_can_join = models.CharField(
        max_length=200, blank=True, default=None, null=True)

    time = models.DateTimeField(auto_now_add=True)
    
class IsJoinRoomsUsers(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='room_is_join_user')
    room_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_coustom_unique_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_join_sit_position = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    # time = models.DateTimeField(auto_now_add=True)
    