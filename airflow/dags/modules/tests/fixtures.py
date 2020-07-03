from pkg_resources import resource_string
import pytest
import fakeredis
from parser import WebParser
from requests import Response
from rss_news import NewsProducer
from proxypool import ProxyPoolScraper, ProxyRecord


TEST_URL = "https://test.com"


@pytest.fixture
def web_parser():
    yield WebParser(TEST_URL)


@pytest.fixture
def scraper():
    yield ProxyPoolScraper(TEST_URL)


@pytest.fixture
def proxy():
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
    yield NewsProducer(
        TEST_URL,
        {
            "http": "http://127.0.0.1:8080", 
            "https": "http://127.0.0.1:8080"
        }
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


@pytest.fixture()
def raw_content():
    def helper(filename):
        return resource_string(
            "tests",
            f"dataresources/{filename}"
        )
    
    yield helper
