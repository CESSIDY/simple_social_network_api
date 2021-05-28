from accounts.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from posts.models import Post


class ApiTestCase(TestCase):
    def setUp(self):
        self.password = 'Qwerty1'
        self.user = self.create_user(name='name', password=self.password)

        self.client = APIClient()

    @staticmethod
    def create_user(name, password):
        user = User.objects.create_user(name, f'{name}@gmail.com')
        user.set_password(password)
        user.save()
        return user

    def get_user_token(self, name):
        registration_url = reverse('accounts:token_obtain_pair')
        response = self.client.post(registration_url, {'username': name,
                                                       'password': self.password})
        return response.data['access']

    def test_post_creating(self):
        token = self.get_user_token(self.user.username)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
        url = reverse('posts:post_create')
        response = self.client.post(url, data={'title': 'title_1',
                                               'body': 'body_1'})

        self.assertEquals(response.status_code, 201)

    def test_post_like(self):
        post = Post.objects.create(title="title", user=self.user)
        token = self.get_user_token(self.user.username)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
        url = reverse('posts:post_like', kwargs={'pk': post.pk})
        response = self.client.post(url)

        self.assertEquals(response.status_code, 201)

    def test_post_unlike(self):
        post = Post.objects.create(title="title", user=self.user)
        token = self.get_user_token(self.user.username)

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
        url = reverse('posts:post_like', kwargs={'pk': post.pk})
        response = self.client.post(url)

        self.assertEquals(response.status_code, 201)
