from django.test import TestCase
from news.models import News


class NewsModelTests(TestCase):

    TEST_NEWS_DATA = {
        "_id": "test_id",
        "title": "test titile",
        "link": "www.testnews.com",
        "published": "2020-01-01 00:00:00",
        "description": "test description",
        "author": "test author",
        "language": "en"
    }

    def test_news_model_create(self):

        news = News.objects.create(**self.TEST_NEWS_DATA)

        self.assertEqual(
            news.link, self.TEST_NEWS_DATA["link"]
        )
        self.assertEqual(
            news.title, self.TEST_NEWS_DATA["title"]
        )

    def test_news_model_retrive(self):
        News.objects.create(**self.TEST_NEWS_DATA)
        
        news = News.objects.get(_id="test_id")

        self.assertTrue(news)
