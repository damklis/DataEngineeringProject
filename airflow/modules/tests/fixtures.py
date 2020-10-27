from pkg_resources import resource_string
import pytest
import fakeredis

from parser import WebParser
from requests import Response
from rss_news import NewsProducer, NewsFormatter, NewsValidator, News
from proxypool import ProxyPoolScraper, ProxyRecord
from retry import RetryOnException as retry


TEST_URL = "https://test.com"


@pytest.fixture
def web_parser():
    yield WebParser(TEST_URL)


@pytest.fixture
def scraper():
    yield ProxyPoolScraper(TEST_URL)


@pytest.fixture
def proxies():
    yield [
        {
            "http": "http://127.0.0.1:8080",
            "https": "http://127.0.0.1:8080"
        }
    ]


@pytest.fixture
def proxy_record():
    yield ProxyRecord(
        "127.0.0.1",
        8080,
        "PL",
        "POLAND",
        "gold",
        "no",
        "no",
        "30 minutes ago"
    )


@pytest.fixture
def producer():
    yield NewsProducer(TEST_URL, "en")


@pytest.fixture
def formatter():
    yield NewsFormatter("en")


@pytest.fixture
def validator():
    yield NewsValidator(
        {
            "description_length": 10,
            "languages": ["en"]
        }
    )


@pytest.fixture
def news_record():
    yield News(
        "test_id", "test_title", "test_link",
        "test_pub", "test_desc", "test_author", "en"
    )


@pytest.fixture
def redis_mock():
    yield fakeredis.FakeStrictRedis()


@pytest.fixture
def redis_config():
    yield {
        "host": "redis",
        "port": "6379",
        "db": 0
    }


@pytest.fixture
def response():
    def helper(status_code):
        response = Response()
        response.status_code = status_code
        response.headers['Content-Type'] = "text/html"
        return response
    yield helper


@pytest.fixture
def raw_content():
    def helper(filename):
        return resource_string(
            "tests",
            f"dataresources/{filename}"
        )

    yield helper


@pytest.fixture
def add_function():

    @retry(5)
    def func(a, b):
        return a + b

    yield func
