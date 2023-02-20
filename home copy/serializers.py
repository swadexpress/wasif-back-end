from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import *
from authentication.models import *
# variation = Size
from home.models import *
from rest_framework_recursive.fields import RecursiveField


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
             'user',
             'fast_name',
             'last_name',
             'about_me',
             'birthday',
             'profile_pic',
            #  'cover_image',
             'gender',
             'gender',
             'followers',
             'following',
             'division',
             'bloodGroup',
             'area',
             'towns',
             'phone',
             'age',
             'donated',
             'request',
             'lifeSave',
             'win',
             'F_area',
             'F_division',
             'F_towns',
             'birthday',
             'create_at',
             'id',
             'bloodDonationStatus',
             
             ]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['post', 'user','time','comm']






class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            
            'user',
            'text',
            'likes',
            'dislikes',
            'created_at',
            'id'
  
        
        ]

