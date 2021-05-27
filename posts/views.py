from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from posts.models import Post
from posts.serializers import CreatePostSerializer


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


class LikePostView(APIView):
    def get(self, request, format=None):
        return Response({"status": "OK"})


class UnLikePostView(APIView):
    def get(self, request, format=None):
        return Response({"status": "OK"})
