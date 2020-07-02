from pkg_resources import resource_string
import pytest
from pytest import fixture
from parser import WebParser
from requests import Response
from proxypool import ProxyPoolScraper, ProxyRecord
from rss_news import NewsProducer


@pytest.fixture
def web_parser():
    yield WebParser("https://test.com")


@pytest.fixture
def scraper():
    yield ProxyPoolScraper("https://test.com")


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
        "https://test.com",
        {
            "http": "http://127.0.0.1:8080", 
            "https": "http://127.0.0.1:8080"
        }
    )


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
