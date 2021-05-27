from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator
from django.utils.timezone import now

from posts.models import Post


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('user', 'title', 'body')

    def create(self, validated_data):
        post = Post.objects.create(
            user=validated_data['user'],
            title=validated_data['title'],
            body=validated_data['body'],
        )
        post.save()

        return post