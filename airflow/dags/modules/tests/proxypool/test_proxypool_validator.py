import pytest
from unittest.mock import patch
from proxypool import ProxyPoolValidator

from ..fixtures import web_parser, raw_content, proxy


@patch("parser.web_parser.WebParser.get_content")
def test_validate_proxy(get_content, raw_content, web_parser, proxy):
    expected = True

    get_content.return_value = raw_content("proxy_list_file.txt")
    validator = ProxyPoolValidator("https://google.com")
    validator.parser = web_parser

    proxy_record = validator.validate_proxy(proxy)
    result = proxy_record.is_valid

    assert result == expected
