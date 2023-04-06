
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('s' ,home, name='home' ),
    path('P2PMessageUniqueIdView/', P2PMessageUniqueIdView.as_view(),
         name='P2PMessageUniqueIdView'),
    path('CreateP2PMessageUniqueIdView/', CreateP2PMessageUniqueIdView.as_view(),
         name='CreateP2PMessageUniqueIdView'),
    path('BuyCoinFromAgentsCreateView/', BuyCoinFromAgentsCreateView.as_view(),
         name='BuyCoinFromAgentsCreateView'),
    path('BuyCoinFromAgentsCreateUpdateView/',
         BuyCoinFromAgentsCreateUpdateView.as_view(), name='BuyCoinFromAgentsCreateUpdateView'),
    path('HostAgentsCreateView/', HostAgentsCreateView.as_view(), name='HostAgentsCreateView'),
    path('MyRechargeView/', MyRechargeView.as_view(), name='MyRechargeView'),
    path('HostAgentsView/', HostAgentsView.as_view(), name='HostAgentsView'),
    path('HostDataView/', HostDataView.as_view(), name='HostDataView'),
    path('RechargeAgentView/', RechargeAgentView.as_view(),
         name='RechargeAgentView'),
    path('AllPostSearch/', AllPostSearch.as_view(), name='AllPostSearch'),
    path('MyAllFriendListView/', MyAllFriendListView.as_view(),
         name='MyAllFriendListView'),
    path('RequestSendView/', RequestSendView.as_view(), name='RequestSendView'),
    path('MyRoomAdminListView/', MyRoomAdminListView.as_view(),
         name='MyRoomAdminListView'),
    path('MyBannedListView/', MyBannedListView.as_view(), name='MyBannedListView'),
    path('MyRoomAdminListView/', MyRoomAdminListView.as_view(),
         name='MyRoomAdminListView'),
    path('MyPostDelete/', MyPostDelete.as_view(), name='MyPostDelete'),
    path('UserDetailsAdminView/', UserDetailsAdminView.as_view(),
         name='UserDetailsAdminView'),
    path('AllUserListAdminView/', AllUserListAdminView.as_view(),
         name='AllUserListAdminView'),
    path('UserDetailsUpdateAdminView/', UserDetailsUpdateAdminView.as_view(),
         name='UserDetailsUpdateAdminView'),
    path('BannerImagesView/', BannerImagesView.as_view(), name='BannerImagesView'),
    path('UploadBannerImagesAndVideosView/', UploadBannerImagesAndVideosView.as_view(),
         name='UploadBannerImagesAndVideosView'),



    path('UserProfileUpdateView/', UserProfileUpdateView.as_view(),
         name='UserProfileUpdateView'),

    path('UserProfileView/', UserProfileView.as_view(), name='UserProfileView'),

    path('UpdateProfileImagesView/', UpdateProfileImagesView.as_view(),
         name='UpdateProfileImagesView'),
    path('UpdateProfileCoverImagesView/', UpdateProfileCoverImagesView.as_view(),
         name='UpdateProfileCoverImagesView'),
    path('HostAgentsUpdateView/', HostAgentsUpdateView.as_view(),
         name='HostAgentsUpdateView'),



    path('OtherUserProfileView/<pk>/',
         OtherUserProfileView.as_view(), name='OtherUserProfileView'),
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
    path('AddSubCommentView/', AddSubCommentView.as_view(),
         name='AddSubCommentView'),
    path('PostLikeDislikeLikeBackDeleteView/', PostLikeDislikeLikeBackDeleteView.as_view(),
         name='PostLikeDislikeLikeBackDeleteView'),
    path('ckeditor/', include('ckeditor_uploader.urls')),



]
