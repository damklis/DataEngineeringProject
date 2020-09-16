from elasticsearch.exceptions import NotFoundError
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient


SEARCH_NEWS_URL = reverse("search:search-list")
SEARCH_DETAIL_NEWS_URL = reverse(
    "search:search-detail", kwargs={"id":"missing_news"}
)


class PublicNewsApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required_news_list(self):
        response = self.client.get(SEARCH_NEWS_URL)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )

    def test_login_required_news_detail(self):
        response = self.client.get(SEARCH_DETAIL_NEWS_URL)

        self.assertEqual(
            response.status_code, status.HTTP_401_UNAUTHORIZED
        )


class PrivateNewsApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test_user@test.com",
            "testpass123"
        )
        self.client.force_authenticate(
            self.user
        )

    def test_retrieve_news_list(self):
        response = self.client.get(SEARCH_NEWS_URL)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_retrieve_missing_news_detail(self):
        with self.assertRaises(NotFoundError):
            self.client.head(
                SEARCH_DETAIL_NEWS_URL
            )
