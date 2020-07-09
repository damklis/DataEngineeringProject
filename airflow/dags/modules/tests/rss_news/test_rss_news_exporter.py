from unittest.mock import patch
import pytest


@patch("rss_news.NewsExporter.export_news_to_broker")
def test_export_news_to_broker(export_news_to_broker):
    topic = "test_topic"
    news = {
        "id": "test_id",
        "title": "test_title",
        "date": "2020-01-01 00:00:00"
    }

    export_news_to_broker(topic, news)
    
    export_news_to_broker.assert_called_once_with(topic, news)
