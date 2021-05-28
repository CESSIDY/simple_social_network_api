from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from posts.models import Post, Like
from posts.serializers import CreatePostSerializer, PostSerializer


class CreatePostView(generics.CreateAPIView):
    model = Post
    serializer_class = CreatePostSerializer

    @staticmethod
    def get_data_from_request(request):
        data = dict(request.data)
        data['user'] = request.user.pk
        if data['title'] and data['title'] is list:
            data['title'] = data['title'][0]
        if data['body'] and data['body'] is list:
            data['body'] = data['body'][0]
        return data

    def create(self, request, *args, **kwargs):
        data = self.get_data_from_request(request)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BasePostView(generics.GenericAPIView):
    model = Post
    serializer_class = PostSerializer


class LikePostView(BasePostView):
    def post(self, request, pk):
        serializer = self.serializer_class(data={'pk': pk})
        serializer.is_valid(raise_exception=True)
        serializer.like(request.user.pk)

        return Response(status=status.HTTP_201_CREATED)


class UnLikePostView(BasePostView):
    def post(self, request, pk):
        serializer = self.serializer_class(data={'pk': pk})
        serializer.is_valid(raise_exception=True)
        serializer.unlike(request.user.pk)

        return Response(status=status.HTTP_201_CREATED)
