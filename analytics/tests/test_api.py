from accounts.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate
from datetime import datetime, timedelta
from accounts.views import RegisterView, CustomTokenObtainPairView
from analytics.views import LikesCountView
from posts.models import Post, Like
from django.utils.timezone import now, make_aware


class ApiTestCase(TestCase):
    def setUp(self):
        self.password = 'Qwerty1'
        self.user = self.create_user(name='name', password=self.password)
        self.user_1 = self.create_user(name='name1', password=self.password)
        self.user_2 = self.create_user(name='name2', password=self.password)

        self.post_lower_date = datetime.now() - timedelta(days=5)
        self.post_upper_date = datetime.now()

        self.client = APIClient()

    @staticmethod
    def create_user(name, password):
        user = User.objects.create_user(name, f'{name}@gmail.com')
        user.set_password(password)
        user.save()
        return user

    def create_posts_for_user(self, user):
        _ = Post.objects.create(title="title", user=user, created_at=make_aware(self.post_lower_date))
        _ = Post.objects.create(title="title", user=user, created_at=make_aware(self.post_upper_date))

    def get_user_token(self, name):
        registration_url = reverse('accounts:token_obtain_pair')
        response = self.client.post(registration_url, {'username': name,
                                                       'password': self.password})
        return response.data['access']

    def like_post_in_date(self, user, date=None):
        if date is None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(created_at=make_aware(date))
        for post in posts:
            post.like(user)

        for like in Like.objects.all()[:Like.objects.all().count()//2]:
            like.created_at = make_aware(self.post_lower_date)
            like.save()

    def test_likes_count(self):
        self.create_posts_for_user(self.user_1)
        self.like_post_in_date(self.user)
        token = self.get_user_token(self.user.username)

        date_from = self.post_lower_date
        date_to = self.post_lower_date + timedelta(days=1)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
        url = reverse('analytics:likes_count', kwargs={'date_from': date_from.strftime('%Y-%m-%d'),
                                                       'date_to': date_to.strftime('%Y-%m-%d')})
        response = self.client.get(url)

        self.assertEquals(response.data['likes_number'], 1)

        date_from = self.post_lower_date
        date_to = self.post_upper_date + timedelta(days=1)

        url = reverse('analytics:likes_count',
                      kwargs={'date_from': date_from.strftime('%Y-%m-%d'),
                              'date_to': date_to.strftime('%Y-%m-%d')})
        response = self.client.get(url)

        self.assertEquals(response.data['likes_number'], 2)
