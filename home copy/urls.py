
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('s' ,home, name='home' ),
    path('UserProfileUpdateView/', UserProfileUpdateView.as_view(),
         name='UserProfileUpdateView'),

    path('UserProfileView/', UserProfileView.as_view(), name='UserProfileView'),
    
    path('UpdateProfileImagesView/', UpdateProfileImagesView.as_view(),
         name='UpdateProfileImagesView'),
    path('OtherUserProfileView/<pk>/', OtherUserProfileView.as_view(), name='OtherUserProfileView'),
#     path('ProfileUpdateView/<pk>/', ProfileUpdateView.as_view(), name='ProfileUpdateView'),
    path('FollowView/', FollowView.as_view(), name='FollowView'),
    path('UnfollowView/', UnfollowView.as_view(), name='UnfollowView'),
#     path('UnauthorizedPostView/', UnauthorizedPostView.as_view(), name='UnauthorizedPostView'),
    path('OtherPostView/', OtherPostView.as_view(), name='OtherPostView'),
    path('OtherOwnPostView/', OtherOwnPostView.as_view(), name='OtherOwnPostView'),
    path('OwnPostView/', OwnPostView.as_view(), name='OwnPostView'),
    path('PostView/', PostView.as_view(), name='PostView'),
    path('ProfileView/', ProfileView.as_view(), name='ProfileView'),
#     path('SearchProfileView/', SearchProfileView.as_view(), name='SearchProfileView'),
    path('LikesView/', LikesView.as_view(), name='LikesView'),
    path('CommentView/', CommentView.as_view(), name='CommentView'),
    path('SubCommentView/', SubCommentView.as_view(), name='SubCommentView'),
    path('AddPostView/', AddPostView.as_view(), name='AddPostView'),
    path('OwnUserView/', OwnUserView.as_view(), name='OwnUserView'),
    path('AddCommentView/', AddCommentView.as_view(), name='AddCommentView'),
    path('AddSubCommentView/', AddSubCommentView.as_view(), name='AddSubCommentView'),
    path('PostLikeDislikeLikeBackDeleteView/', PostLikeDislikeLikeBackDeleteView.as_view(), name='PostLikeDislikeLikeBackDeleteView'),
    path('ckeditor/', include('ckeditor_uploader.urls')),



]
