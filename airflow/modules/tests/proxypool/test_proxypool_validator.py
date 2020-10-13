from unittest.mock import patch
from proxypool import ProxyPoolValidator

from ..fixtures import web_parser, raw_content, proxy_record


@patch("parser.web_parser.WebParser.get_content")
def test_validate_proxy(get_content, raw_content, web_parser, proxy_record):
    expected = True

    get_content.return_value = raw_content("proxy_list_file.txt")
    validator = ProxyPoolValidator("https://google.com", sleep_interval=0)
    validator.parser = web_parser

    proxy_record = validator.validate_proxy(proxy_record)
    result = proxy_record.is_valid

    assert result == expected

@patch("parser.web_parser.WebParser.get_content")
def test_invalid_proxy(get_content, raw_content, web_parser, proxy_record):
    expected = False

    get_content.return_value = None
    validator = ProxyPoolValidator("https://google.com", sleep_interval=0)
    validator.parser = web_parser

    proxy_record = validator.validate_proxy(proxy_record)
    result = proxy_record.is_valid

    assert result == expected

@patch("parser.web_parser.WebParser.get_content")
def test_unstable_valid_proxy(get_content, raw_content, web_parser, proxy_record):
    expected = True

    valid_content = raw_content("proxy_list_file.txt")
    get_content.side_effect = [valid_content, valid_content, None]
    validator = ProxyPoolValidator("https://google.com", sleep_interval=0)
    validator.parser = web_parser

    proxy_record = validator.validate_proxy(proxy_record)
    result = proxy_record.is_valid

    assert result == expected
    assert round(proxy_record.health, 2) == 0.67

@patch("parser.web_parser.WebParser.get_content")
def test_unstable_invalid_proxy(get_content, raw_content, web_parser, proxy_record):
    expected = False

    valid_content = raw_content("proxy_list_file.txt")
    get_content.side_effect = [None, None, valid_content]
    validator = ProxyPoolValidator("https://google.com", sleep_interval=0)
    validator.parser = web_parser

    proxy_record = validator.validate_proxy(proxy_record)
    result = proxy_record.is_valid

    assert result == expected
    assert round(proxy_record.health, 2) == 0.33
