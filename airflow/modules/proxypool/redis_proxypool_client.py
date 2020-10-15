import json
import redis
from log import log


@log
class RedisProxyPoolClient:
    def __init__(self, key, redis_config):
        self.key = key
        self.redis = redis.StrictRedis(
            **redis_config
        )

    def __enter__(self):
        return self

    def override_existing_proxies(self, proxies):
        self.logger.info(f"Overriding existing proxies {proxies}")
        self.redis.delete(self.key)
        self.redis.lpush(self.key, *proxies)

    def list_existing_proxies(self):
        response = self.redis.lrange(self.key, 0, -1)
        return [
            json.loads(proxy) for proxy in response
        ]

    def get_proxy(self):
        existing_proxies = self.list_existing_proxies()
        if len(existing_proxies) > 0:
            return existing_proxies[0]

    def lpop_proxy(self):
        self.logger.info("Deleting proxy!")
        self.redis.lpop(self.key)

    def __exit__(self, type, value, traceback):
        client_id = self.redis.client_id()
        self.redis.client_kill_filter(
            _id=client_id
        )
