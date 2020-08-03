from unittest.mock import patch
import pytest


@patch("rss_news.NewsExporter.export_news_to_broker")
def test_export_news_to_broker(export_news_to_broker):
    topic = "test_topic"
    news = {
        "_id": "test_id",
        "title": "test_title",
        "link": "www.test.com",
        "date": "2020-01-01 00:00:00",
        "description": "Test",
        "author": "Test",
        "language": "pl"
    }

    export_news_to_broker(topic, news)
    
    export_news_to_broker.assert_called_once_with(topic, news)
