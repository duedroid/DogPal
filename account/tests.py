from django.test import TestCase
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from .models import Account
from django.urls import reverse


class LoginEmailTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.default_email = 'nattapadtanasak.kon@conicle.com'
        self.default_password = 'beer2972'
        user = Account.objects.create_superuser(self.default_email, self.default_password)

    def test_login_email_and_password_null(self):
        response = self.client.post('/api/login/', {'email': '',
                                                    'password': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_password_is_null(self):
        response = self.client.post('/api/login/', {'email': self.default_email,
                                                    'password': ''}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_email_is_null(self):
        response = self.client.post('/api/login/', {'email': '',
                                                    'password': self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_email_is_wrong(self):
        response = self.client.post('/api/login/', {'email': '_@conicle.com',
                                                    'password': self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_password_is_wrong(self):
        response = self.client.post('/api/login/', {'email': self.default_email,
                                                    'password': '_%s' % self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_email_wrong_format(self):
        response = self.client.post('/api/login/', {'email': 'demo@conicle',
                                                    'password': self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_by_email(self):
        response = self.client.post('/api/login/', {'email': self.default_email,
                                                    'password': self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_but_session_is_exist(self):
        self.client.login(email=self.default_email, password=self.default_password)
        response = self.client.post('/api/login/', {'email': self.default_email,
                                                    'password': self.default_password}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
