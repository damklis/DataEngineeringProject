from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:register")
GET_TOKEN_URL = reverse("user:login")


class UserApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    @staticmethod
    def create_user(**kwargs):
        return get_user_model().objects.create_user(
            **kwargs
        )

    def test_create_valid_user(self):
        attrs = {
            "email": "test_user_3@test.com",
            "password": "test123"
        }
        response = self.client.post(CREATE_USER_URL, attrs)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(attrs["password"]))
        self.assertNotIn("password", response.data)

    def test_password_too_short(self):
        attrs = {
            "email": "test_user_4@test.com",
            "password": "123"
        }
        response = self.client.post(CREATE_USER_URL, attrs)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_user_exists(self):
        attrs = {
            "email": "test_user_5@test.com",
            "password": "123"
        }
        self.create_user(**attrs)

        response = self.client.post(CREATE_USER_URL, attrs)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )

    def test_create_token_for_user(self):
        attrs = {
            "email": "test_user_5@test.com",
            "password": "123"
        }
        self.create_user(**attrs)
        response = self.client.post(GET_TOKEN_URL, attrs)
        self.assertIn("token", response.data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_create_token_invalid_credentials(self):
        attrs = {
            "email": "test_user_6@test.com",
            "password": "12345"
        }
        self.create_user(email="test_user_6@test.com", password="wrong")
        response = self.client.post(GET_TOKEN_URL, attrs)
        self.assertNotIn("token", response.data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
    
    def test_create_token_no_user(self):
        attrs = {
            "email": "test_user_7@test.com",
            "password": "12345"
        }
        response = self.client.post(GET_TOKEN_URL, attrs)
        self.assertNotIn("token", response.data)
        self.assertEqual(
            response.status_code, status.HTTP_400_BAD_REQUEST
        )
