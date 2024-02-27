from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
import random
import string

from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')


        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


AUTH_PROVIDERS = {'facebook': 'facebook', 'google': 'google',
                  'twitter': 'twitter', 'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    personal_WS_ID = models.CharField(max_length=255,default='')
    is_verified = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_rider = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(max_length=255, blank=False,null=False, default=AUTH_PROVIDERS.get('email'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'email':self.email,
            'username':self.username,
            'personal_WS_ID':self.personal_WS_ID
        }


class OTPToken(models.Model):
    token = models.CharField(max_length=300)
    token_number = models.CharField(max_length=300, default="")
    uidb64 = models.CharField(max_length=100)

    def __str__(self):
        return self.token_number

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def get_image_filename(instance, filename):
    title = random_string_generator()
    slug = slugify(title)
    return "profile_images/%s-%s" % (slug, filename) 


class ProfileImages(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile_images')

    image = CloudinaryField('image')
    # image = models.ImageField(upload_to=get_image_filename,
    #                           verbose_name='Image',null=True)

class GroupImages(models.Model):
    image_unique_id = models.CharField(blank=True, max_length=120)
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to=get_image_filename,
    #                           verbose_name='Image',null=True)


class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	seen = models.BooleanField(default=False)



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile')
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    custom_id = models.CharField(max_length=10, null=True,blank=True)
    about_me = models.CharField(max_length=250, null=True,blank=True)
    fast_name = models.CharField( max_length=50,null=True,blank=True,default=' ')
    last_name = models.CharField( max_length=50,null=True,blank=True,default=' ')
    gender = models.CharField( max_length=10, null=True,blank=True)
    date_of_birth = models.CharField( max_length=300, null=True,blank=True)
    country = models.CharField( max_length=300, null=True,blank=True)
    language = models.CharField( max_length=300, null=True,blank=True)
    profile_email = models.CharField( max_length=300, null=True,blank=True)
    phone = models.CharField(blank=True, max_length=11)
    address = models.CharField(blank=True, max_length=300)
    district = models.CharField(blank=True, max_length=120)
    division = models.CharField(blank=True, max_length=110)
    zip_code = models.CharField(blank=True, max_length=20)
    image = models.CharField(blank=True, max_length=400)
    cover_image = models.CharField(blank=True, max_length=400)
    is_vip = models.CharField( max_length=300, null=True,blank=True)
    is_mvip = models.CharField( max_length=300, null=True,blank=True)
    # ======================================================
    coin = models.CharField(blank=True, max_length=400,default=0)
    total_coin = models.CharField(blank=True, max_length=400,default=0)
    diamond = models.CharField(blank=True, max_length=400,default=0)
    total_diamond = models.CharField(blank=True, max_length=400,default=0)
    # ======================================================
    is_blocked = models.BooleanField(default=False)
    is_host_agent = models.BooleanField(default=False)
    is_recharge_agent = models.BooleanField(default=False)



    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email

    def user_id(self):
        return self.user.id

    def user_name(self):
        return self.fast_name + " "+ self.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


    def non_followed_user(self):
        return set(User.objects.filter(is_active=True))-set(self.following.all())-{self.user}

    def get_notifications(self):
        return Notification.objects.filter(user=self.user, seen = False)



class ShopProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='ShopProfile')
    about_me = models.CharField(max_length=250, null=True,blank=True)
    fast_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    gender = models.CharField( max_length=6, null=True,blank=True)
    phone = models.CharField(blank=True, max_length=11)
    address = models.CharField(blank=True, max_length=300)
    district = models.CharField(blank=True, max_length=120)
    division = models.CharField(blank=True, max_length=110)
    zip_code = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/users/')



    def __str__(self):
        return self.user.email

    def email(self):
        return self.user.email

    def user_id(self):
        return self.user.id

    def user_name(self):
        return self.fast_name + " "+ self.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


    def non_followed_user(self):
        return set(User.objects.filter(is_active=True))-set(self.following.all())-{self.user}

    def get_notifications(self):
        return Notification.objects.filter(user=self.user, seen = False)


