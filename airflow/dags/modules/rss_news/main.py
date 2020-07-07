import argparse
from proxypool import RedisProxyPoolClient
from log import Logger
from rss_news.rss_news_producer import NewsProducer
from rss_news.rss_news_exporter import NewsExporter
from rss_news.retry_on_exception import (
    RetryOnException as retry
)


@retry(5)
def export_news_to_broker(config, rss_feed):
    logger = Logger().get_logger(__name__)
    rss_feed = config.RSS_FEEDS[rss_feed]
    redis = RedisProxyPoolClient(
        config.REDIS_KEY, config.REDIS_CONFIG
    )
    with NewsExporter(config.BOOTSTRAP_SERVERS) as exporter:
        proxy = redis.get_random_proxy()
        logger.info(proxy)
        for news in NewsProducer(rss_feed).get_news_stream(proxy):
            logger.info(news)
            exporter.export_news_to_broker(
                config.TOPIC,
                news.as_dict()
            )

