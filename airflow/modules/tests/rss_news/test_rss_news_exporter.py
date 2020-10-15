from unittest.mock import patch
import pytest


@patch("rss_news.NewsExporter")
def test_export_news_to_broker(exporter):
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
    exporter.export_news_to_broker(topic, news)

    exporter.export_news_to_broker.assert_called_once_with(
        topic, news
    )
