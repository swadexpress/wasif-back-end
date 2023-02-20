from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from .models import *
from authentication.models import *
# variation = Size
from home.models import *
from rest_framework_recursive.fields import RecursiveField


class PostSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()
    # variations = VariationSerializer( many=True, read_only=True, source='variants_set')
    # images = ProductImagesSerializer(many=True, read_only=True, source='productimages_set')

    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'






class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

