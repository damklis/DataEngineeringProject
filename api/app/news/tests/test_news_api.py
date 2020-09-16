from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


ADMIN_SEARCH_NEWS_URL = reverse("admin:news-list")
ADMIN_SEARCH_NEWS_URL = reverse(
    "admin:news-detail", kwargs={"_id":"missing_news"}
)


class PublicAdminNewsApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required_news_list(self):
        response = self.client.get(ADMIN_SEARCH_NEWS_URL)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_login_required_news_detail(self):
        response = self.client.get(ADMIN_SEARCH_NEWS_URL)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )
