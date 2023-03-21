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



class BannerImages(models.Model):
	name = models.CharField(max_length=200,default='')
	image =  models.CharField(max_length=200,default='')
	uploaded = models.DateTimeField(auto_now_add=True)







def upload_post_to(instance,filename):
	return f'post_picture/{instance.user.username}/{filename}'
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name='likes',blank =True,default=None)
    dislikes = models.ManyToManyField(User,related_name='dislikes',blank =True,default=None)
    text = models.TextField()
    # picture = models.ImageField(null=True, upload_to = upload_post_to,default= None)
    created_at = models.DateTimeField(auto_now_add=True)

def get_image_filename(instance, filename):
    title = instance.post.text
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)  

class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,default=None)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image',null=True)

class PostImages(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE ,default=None)
	# image = CloudinaryField('image')
	image = models.CharField(max_length=500, default='')



class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='like_post')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)




class Dislike(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='dislike_post')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)	




class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comment_post')
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='comment_user')
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	# profile = models.ManyToManyField(Profile,related_name='Profile')



class SubComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)



class P2PMessageUniqueId(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
	other_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='other_user')
	user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='user_profile')
	other_user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='other_user_profile')
	uniqueId = models.CharField(max_length=500, default='')
	time = models.DateTimeField(auto_now_add=True)