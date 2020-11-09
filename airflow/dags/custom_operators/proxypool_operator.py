import json
from concurrent.futures import ThreadPoolExecutor
from retry import RetryOnException as retry
from proxypool import (
    ProxyPoolValidator,
    ProxyPoolScraper,
    RedisProxyPoolClient
)

from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults


class ProxyPoolOperator(BaseOperator):

    @apply_defaults
    def __init__(
            self,
            proxy_webpage,
            number_of_proxies,
            testing_url,
            max_workers,
            redis_config,
            redis_key,
            *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.proxy_webpage = proxy_webpage
        self.testing_url = testing_url
        self.number_of_proxies = number_of_proxies
        self.max_workers = max_workers
        self.redis_config = redis_config
        self.redis_key = redis_key

    @retry(5)
    def execute(self, context):
        proxy_scraper = ProxyPoolScraper(self.proxy_webpage)
        proxy_validator = ProxyPoolValidator(self.testing_url)
        proxy_stream = proxy_scraper.get_proxy_stream(self.number_of_proxies)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(
                proxy_validator.validate_proxy, proxy_stream
            )
            valid_proxies = filter(lambda x: x.is_valid is True, results)
            sorted_valid_proxies = sorted(
                valid_proxies, key=lambda x: x.health, reverse=True
            )

        with RedisProxyPoolClient(self.redis_key, self.redis_config) as client:
            client.override_existing_proxies(
                [
                    json.dumps(record.proxy)
                    for record in sorted_valid_proxies[:5]
                ]
            )
