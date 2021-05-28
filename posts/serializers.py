from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueValidator
from django.utils.timezone import now

from posts.models import Post, Like


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


class PostSerializer(serializers.Serializer):
    class Meta:
        fields = ('pk',)

    def validate(self, attrs):
        if 'pk' not in self.initial_data:
            raise serializers.ValidationError({"pk": "Pk fields not valid."})
        post = Post.objects.get(pk=self.initial_data['pk'])
        if post is None:
            raise serializers.ValidationError({"post": "Post exists"})
        attrs['post'] = post
        return attrs

    def like(self, user_pk):
        if 'post' in self.validated_data:
            user = User.objects.get(pk=user_pk)
            self.validated_data['post'].like(user)

    def unlike(self, user_pk):
        if 'post' in self.validated_data:
            user = User.objects.get(pk=user_pk)
            self.validated_data['post'].unlike(user)

