from rest_framework import generics
from rest_framework.response import Response
from posts.models import Post, Like


class LikesCountView(generics.GenericAPIView):

    @staticmethod
    def get(request, date_from, date_to):
        likes_number = request.user.likes_number_per_date(date_from, date_to)
        return Response(data={'likes_number': likes_number})
