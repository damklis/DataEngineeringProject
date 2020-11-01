from unittest.mock import patch, Mock
import pytest
from rss_news import NewsExporter


@patch("rss_news.rss_news_exporter.KafkaProducer")
def test_connect_producer(mock_producer):

    exporter = NewsExporter(["test_broker:9092"])

    assert exporter._producer is not None


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


@patch("rss_news.rss_news_exporter.KafkaProducer")
def test_export_news_to_broker_context_manager(mock_producer):
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

    with NewsExporter(["test_broker:9092"]) as exporter:
        exporter.export_news_to_broker(topic, news)
        exporter._producer.send.assert_called_once_with(
            topic, value=news
        )
