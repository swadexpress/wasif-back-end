
from django.urls import include, path

from .views import *

urlpatterns = [
    # path('s' ,home, name='home' ),
    path('FollowersListView/', FollowersListView.as_view(),
         name='FollowersListView'),
    path('AllProduct/', AllProduct.as_view(),
         name='AllProduct'),
    path('UpdateProfileImagesView/', UpdateProfileImagesView.as_view(),
         name='UpdateProfileImagesView'),

    path('ckeditor/', include('ckeditor_uploader.urls')),



]
