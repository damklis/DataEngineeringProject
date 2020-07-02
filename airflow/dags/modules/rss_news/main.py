import argparse
from rss_news.rss_news_producer import NewsProducer
from rss_news.rss_news_exporter import NewsExporter
from proxypool import RedisProxyPoolClient
from log import Logger


def export_news_to_broker(config, rss_feed):
    logger = Logger().get_logger(__name__)
    rss_feed = config.RSS_FEEDS[rss_feed]
    redis = RedisProxyPoolClient(config.REDIS_KEY, config.REDIS_CONFIG)
    # a = NewsProducer(rss_feed)
    # for news in a.get_news_stream():
    #      logger.info(news)
    with NewsExporter(config.BOOTSTRAP_SERVERS) as exporter:
        proxy = redis.get_random_proxy()
        for news in NewsProducer(rss_feed, proxy).get_news_stream():
            logger.info(news)
            exporter.export_news_to_broker(
                config.TOPIC,
                news.as_dict()
            )

