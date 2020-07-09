import json
from unittest.mock import patch
import pytest
import fakeredis
from proxypool import RedisProxyPoolClient

from ..fixtures import redis_config, redis_mock, proxies


@patch("proxypool.redis_proxypool_client.redis.StrictRedis")
def test_override_existing_proxies(redis, redis_config, redis_mock, proxies):
    new_proxies = [{"http": "http://127.0.0.1:8081", "https": "http://127.0.0.1:8081"}]
    key = "test"
    redis_mock.lpush(key, *[json.dumps(_) for _ in proxies])

    redis_client = RedisProxyPoolClient(key, redis_config)
    redis_client.redis = redis_mock
    redis_client.override_existing_proxies(
        [json.dumps(_) for _ in new_proxies]
    )

    current_proxies = redis_mock.lrange(key, 0, -1)
    result = [json.loads(_) for _ in current_proxies]

    assert result != proxies


@patch("proxypool.redis_proxypool_client.redis.StrictRedis")
def test_list_existing_proxies(redis, redis_config, redis_mock, proxies):
    key = "test"
    redis_mock.lpush(key, *[json.dumps(_) for _ in proxies])

    redis_client = RedisProxyPoolClient(key, redis_config)
    redis_client.redis = redis_mock
    
    result = redis_client.list_existing_proxies()
    
    assert result == proxies
