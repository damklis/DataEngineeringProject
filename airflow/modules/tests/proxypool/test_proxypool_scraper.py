from proxypool import ProxyRecord
from unittest.mock import patch

from ..fixtures import web_parser, scraper, raw_content


@patch("parser.web_parser.WebParser.get_content")
def test_get_proxy_stream(get_content, raw_content, web_parser, scraper):
    get_content.return_value = raw_content("proxy_list_file.txt")

    scraper.parser = web_parser
    stream = scraper.get_proxy_stream(5)

    result = list(stream)[-1]

    assert isinstance(result, ProxyRecord)
