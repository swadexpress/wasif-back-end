import datetime

import django
from authentication.models import *
from ckeditor_uploader.fields import RichTextUploadingField
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.db import models
from django.db.models import Avg, Count, Sum
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe
from django_countries.fields import CountryField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class BannerImages(models.Model):
    name = models.CharField(max_length=200, default='')
    image =CloudinaryField(resource_type='raw', default=None, blank=True,null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
class Product(models.Model):
    product_name = models.CharField(max_length=200, default=None, blank=True,null=True)
    product_price = models.CharField(max_length=200,default=None, blank=True,null=True)
    product_image = models.CharField(max_length=200, default=None, blank=True,null=True)
    product_dis = models.CharField(max_length=200, default=None, blank=True,null=True)
    uploaded = models.DateTimeField(auto_now_add=True)
