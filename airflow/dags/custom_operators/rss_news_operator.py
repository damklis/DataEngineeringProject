from log import log
from retry import RetryOnException as retry
from proxypool import RedisProxyPoolClient
from rss_news import (
    NewsProducer,
    NewsExporter,
    NewsValidator
)

from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults


@log
class RSSNewsOperator(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            validator_config,
            rss_feed,
            language,
            redis_config,
            redis_key,
            bootstrap_servers,
            topic,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validator_config = validator_config
        self.rss_feed = rss_feed
        self.language = language
        self.redis_config = redis_config
        self.redis_key = redis_key
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    @retry(5)
    def execute(self, context):
        validator = NewsValidator(self.validator_config)
        producer = NewsProducer(self.rss_feed, self.language)
        redis = RedisProxyPoolClient(self.redis_key, self.redis_config)

        with NewsExporter(self.bootstrap_servers) as exporter:
            proxy = redis.get_proxy()
            self.logger.info(proxy)
            try:
                for news in producer.get_news_stream(proxy):
                    self.logger.info(news)
                    validator.validate_news(news)
                    exporter.export_news_to_broker(
                        self.topic,
                        news.as_dict()
                    )
            except Exception as err:
                redis.lpop_proxy()
                self.logger.error(f"Exception: {err}")
                raise err
