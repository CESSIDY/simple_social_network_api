from accounts.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate

from accounts.views import RegisterView, CustomTokenObtainPairView


class ApiTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user', 'user@gmail.com')
        self.user1.set_password('Qwerty1!')
        self.user1.save()
        self.factory = APIRequestFactory()

    def test_registration(self):
        view = RegisterView.as_view()
        registration_url = reverse('accounts:auth_register')
        request = self.factory.post(registration_url, {'username': 'user_1',
                                                       'email': 'user_1@gmail.com',
                                                       'password': 'Qwerty1!',
                                                       'password2': 'Qwerty1!',
                                                       'first_name': 'first_name',
                                                       'last_name': 'last_name'}, format='json')
        response = view(request)
        self.assertEquals(response.status_code, 201)

    def test_login(self):
        view = CustomTokenObtainPairView.as_view()
        registration_url = reverse('accounts:token_obtain_pair')
        request = self.factory.post(registration_url, {'username': 'user',
                                                       'password': 'Qwerty1!'})
        response = view(request)
        self.assertEquals(response.status_code, 200)

