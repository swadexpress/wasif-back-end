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


class HostAgents(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Cancel', 'Cancel'),
    )
    agent_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='host_agent_user')
    join_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='host_join_user')
    join_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='host_join_user_profile')
    agent_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='host_agent_user_profile')
    status = models.CharField(max_length=10, choices=STATUS,default="Pending")
    time = models.DateTimeField(auto_now_add=True)
    





class BuyCoinFromAgents(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Cancel', 'Cancel'),
    )
    buyer_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer_user')
    agent_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='agent_user')
    buyer_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='buyer_user_profile')
    agent_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='agent_user_profile')
    amount = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    
    status = models.CharField(max_length=10, choices=STATUS,default="Pending")

    time = models.DateTimeField(auto_now_add=True)
    





class SentGifts(models.Model):
    room_admin_user_profile = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    sent_user_user_profile = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    receive_user_profile = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    room_id = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    gift_name = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    amount = models.CharField(
        max_length=200, blank=True, default=None, null=True)
    time = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)
    # date = models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)


class BannerImages(models.Model):
    name = models.CharField(max_length=200, default='')
    image = models.CharField(max_length=200, default='')
    uploaded = models.DateTimeField(auto_now_add=True)


def upload_post_to(instance, filename):
    return f'post_picture/{instance.user.username}/{filename}'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='likes', blank=True, default=None)
    dislikes = models.ManyToManyField(
        User, related_name='dislikes', blank=True, default=None)
    text = models.TextField()
    # picture = models.ImageField(null=True, upload_to = upload_post_to,default= None)
    created_at = models.DateTimeField(auto_now_add=True)


def get_image_filename(instance, filename):
    title = instance.post.text
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image', null=True)


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    # image = CloudinaryField('image')
    image = models.CharField(max_length=500, default='')


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='like_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Dislike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='dislike_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment_user')
    time = models.DateTimeField(auto_now_add=True)
    comm = models.TextField()
    # profile = models.ManyToManyField(Profile,related_name='Profile')


class SubComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    comm = models.TextField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class P2PMessageUniqueId(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    other_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='other_user')
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='user_profile')
    other_user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='other_user_profile')
    uniqueId = models.CharField(max_length=500, default='')
    time = models.DateTimeField(auto_now_add=True)
