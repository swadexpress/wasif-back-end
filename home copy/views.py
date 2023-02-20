from authentication.models import *
from django.shortcuts import render, redirect
from .models import *
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from .models import *
# import googlemaps
from datetime import datetime
import timeit
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from django.db.models import Q
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView,
    UpdateAPIView, DestroyAPIView
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class PostView(ListAPIView):
    def get(self, request, *args, **kwargs):
        following_users = list(request.user.profile.following.all())
        following_users.append(request.user)
        data = Post.objects.filter(user__in = following_users).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))
            profileId.append(str(i.user.profile.id))

            image = Images.objects.filter(post_id=int(i.id))
           
            image = image.values()
            images.append(list(image))
            like = i.likes.all()


            likeUserId = []

            for i in like:
                likeUserId.append(i.id)


            like  = (list(like))

            likes.append(likeUserId)
        data = list(data.values())

        responseData = {
            'status': 'success',
             'data': data,
             'userFullName':fullName,
             'profilePic':profilePic,
             'images':images,
             'likes':likes,
             "profileId":profileId
             
             }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)






class AddPostView(APIView):
    def post(self, request, *args, **kwargs):
        caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)

        creatPost = Post.objects.create(user = request.user,text=caption)
        if  creatPost :
            for image in images:
                Images.objects.create(post_id = creatPost.id ,image=image)
   

        return Response(status=HTTP_200_OK)


# <QueryDict: {'comment': ['test'], 'image': [<TemporaryUploadedFile: video-calling.mp4 (video/mp4)>]}>





class PostLikeDislikeLikeBackDeleteView(APIView):

    def post(self, request, *args, **kwargs):
        isLiked = request.data.get('isLiked', None)
        postId = request.data.get('postId', None)
# .....................Post  Liked ............................
        if isLiked == True:
            post = Post.objects.get(id=postId)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
                try:
                    Like.objects.filter(user = request.user, post = post)[0].delete()

                except:
                    pass


            return Response(status=HTTP_200_OK)


# ..................... Post Liked-Back ............................

        elif isLiked == False:



            post = Post.objects.get(id=postId)
            post.likes.add(request.user)
            Like.objects.create(user=request.user, post=post)
            return Response(status=HTTP_200_OK)



        return Response(status=HTTP_200_OK)






class FollowView(APIView):

    def post(self, request, *args, **kwargs):
        orther_user = request.data.get('otherUserId', None)
        following = get_object_or_404(User, id = orther_user)
        following.profile.followers.add(request.user)
        request.user.profile.following.add(following)
        return Response(status=HTTP_200_OK)




class UnfollowView(APIView):

    def post(self, request, *args, **kwargs):
        orther_user = request.data.get('otherUserId', None)
        following = get_object_or_404(User, id = orther_user)
        following.profile.followers.remove(request.user)
        request.user.profile.following.remove(following)
        return Response(status=HTTP_200_OK)


class SubCommentView(APIView):
    def post(self, request, *args, **kwargs):
        commentId = request.data.get('commentId', None)
        data = SubComment.objects.filter(comment_id=int(commentId))
        fullName = []
        profilePic = []
        for i in data:
            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))
        data = list(data.values())
        responseData = {'status': 'success', 'data': data,'subCommentFullName':fullName,'subProfilePic':profilePic}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)







class AddSubCommentView(APIView):

    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        comment = request.data.get('comment', None)

        obj = SubComment.objects.create(user=request.user, 
            comment = Comment.objects.get(id=int(postId)),
            comm = comment,
            )

        return Response(status=HTTP_200_OK)




class AddCommentView(APIView):

    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        comment = request.data.get('comment', None)
        obj = Comment.objects.create(user=request.user, 
            post = Post.objects.get(id=int(postId)),
            comm = comment,
            )
        return Response(status=HTTP_200_OK)



class CommentView(APIView):
    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        data = Comment.objects.filter(post_id=int(postId))
        fullName = []
        profilePic = []
        subComment = []
        for i in data:
            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))
            subcomment = SubComment.objects.filter(comment_id=int(i.id))
            subcomment = subcomment.values()
            subComment.append(list(subcomment))


 
        data = list(data.values())
        responseData = {
            'status': 'success', 
            'data': data,
            'fullName':fullName,
            'profilePic':profilePic,
            'subComment':subComment
            }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)

























class OtherOwnPostView(ListAPIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        OtherUserId = request.data.get('OtherUserId', None)


        data = Post.objects.filter(user_id = OtherUserId).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))
            profileId.append(str(i.user.profile.id))

            image = Images.objects.filter(post_id=int(i.id))
           
            image = image.values()
            images.append(list(image))
            like = i.likes.all()


            likeUserId = []

            for i in like:
                likeUserId.append(i.id)


            like  = (list(like))

            likes.append(likeUserId)
        data = list(data.values())

        responseData = {
            'status': 'success',
             'data': data,
             'userFullName':fullName,
             'profilePic':profilePic,
             'images':images,
             'likes':likes,
             "profileId":profileId
             
             }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)






class OtherPostView(ListAPIView):
    def post(self, request, *args, **kwargs):
        OtherUserPostId = request.data.get('OtherUserPostId', None)
        PostOtherUserId = request.data.get('PostOtherUserId', None)
        # print(request.data)

 
        # singelData1 = get_object_or_404(Post, id = OtherUserPostId)
        singelData = Post.objects.filter(id = OtherUserPostId)
        alldata = Post.objects.filter(user_id = PostOtherUserId).order_by('-created_at')
        
        alldata = alldata.filter(~Q(id=OtherUserPostId))
        print (singelData,'results = Model.objects.exclude(a=True, x!=5)')
        
        data =list(chain(singelData, alldata))
        data1 =list(chain(singelData.values(), alldata.values()))
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:
            # print(i.values)
            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))
            profileId.append(str(i.user.profile.id))
            

            image = Images.objects.filter(post_id=int(i.id))
           
            image = image.values()
            images.append(list(image))
            like = i.likes.all()


            likeUserId = []

            for i in like:
                likeUserId.append(i.id)


            like  = (list(like))

            likes.append(likeUserId)

        responseData = {
            'status': 'success',
             'data': data1,
             'userFullName':fullName,
             'profilePic':profilePic,
             'images':images,
             'likes':likes,
             "profileId":profileId
             
             }
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class OwnPostView(ListAPIView):
    def get(self, request, *args, **kwargs):

        data = Post.objects.filter(user = request.user).order_by('-created_at')
        fullName = []
        profilePic = []
        profileId = []
        images = []
        likes = []
        for i in data:

            print (i.user.profile)
        #     full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
        #     fullName.append(full_name)
        #     profilePic.append(str(i.user.profile.profile_pic))
        #     profileId.append(str(i.user.profile.id))

        #     image = Images.objects.filter(post_id=int(i.id))
           
        #     image = image.values()
        #     images.append(list(image))
        #     like = i.likes.all()


        #     likeUserId = []

        #     for i in like:
        #         likeUserId.append(i.id)


        #     like  = (list(like))

        #     likes.append(likeUserId)
        # data = list(data.values())

        # responseData = {
        #     'status': 'success',
        #      'data': data,
        #      'userFullName':fullName,
        #      'profilePic':profilePic,
        #      'images':images,
        #      'likes':likes,
        #      "profileId":profileId
             
        #      }
        return JsonResponse("responseData", safe=False, status=HTTP_200_OK)





class OtherUserProfileView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class OwnUserView(ListAPIView):
    # permission_classes = (IsAuthenticated )
    serializer_class = ProfileSerializer
    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


# class SearchProfileView(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = [ 'fast_name']



class ProfileView(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()



class LikesView(APIView):
    def post(self, request, *args, **kwargs):
        postId = request.data.get('postId', None)
        data = Like.objects.filter(post_id=int(postId))


        fullName = []
        profilePic = []
        for i in data:

            full_name = i.user.profile.fast_name +" "+ i.user.profile.last_name
            fullName.append(full_name)
            profilePic.append(str(i.user.profile.profile_pic))

        data = list(data.values())
        
        responseData = {
            'status': 'success', 
            'data': data,
            'fullName':fullName,
            'profilePic':profilePic,
            }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class UpdateProfileImagesView(APIView):
    def post(self, request, *args, **kwargs):
        images = request.data.getlist('image', None)
        # MyUserId = request.data.getlist('MyUserId', None)
        MyUserId = request.data['MyUserId']

        if images:
            for image in images:
                check_profile = ProfileImages.objects.filter(user_id=MyUserId)
                if check_profile:
                    check_profile.delete()
                image_url = ProfileImages.objects.create(
                    user_id=MyUserId, image=image)
                image_url = image_url.image
                profile = UserProfile.objects.filter(user_id=MyUserId)

                profile.update(image=image_url)

        # data = list(data
        responseData = {'status': 'success', }

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)

        # return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UploadImagesAndVideosView(APIView):
    def post(self, request, *args, **kwargs):
        # caption = request.data.get('caption', None)
        images = request.data.getlist('image', None)
        # type = request.data.getlist('type', None)
        # print(request.data['_parts'][0],'.....')
        print(request.data, '.....')
        # print(request.data['image'],'.....')
        data = []

        if images:
            for image in images:
                image_url = Images.objects.create(image=image)
                print(image_url.image)
                data.append(str(image_url.image))

        # data = list(data
        responseData = {'status': 'success', 'data': data}

        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)




class UserProfileUpdateView(ListAPIView):
    permission_classes = (AllowAny, )

    def post(self, request,  *args, **kwargs):
        d = request.data

        userId = request.data['userId']
        fastName = request.data['fast_name']
        lastName = request.data['last_name']
        data = UserProfile.objects.filter(user_id=userId)
        data = data.update(
            fast_name=fastName,
            last_name=lastName,
        )
        data = UserProfile.objects.filter(user_id=userId)

        data = list(data.values())

        responseData = {'status': 'success', 'data': data}
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)


class UserProfileView(ListAPIView):
    permission_classes = (AllowAny, )

    def post(self, request,  *args, **kwargs):
        d = request.data
        print(request.data, '.......asdfasdfsadfddddddddddddddddd..............')
        userId = request.data['userId']

        data = UserProfile.objects.filter(user_id=userId).values(
            'user_id',
            'user__email',
            'fast_name',
            'last_name',
            'image',

        )

        data = list(data)

        responseData = {'status': 'success', 'data': data}
        return JsonResponse(responseData, safe=False, status=HTTP_200_OK)

