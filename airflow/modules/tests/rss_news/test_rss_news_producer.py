import datetime
from unittest.mock import patch
import pytest
from rss_news import News

from ..fixtures import web_parser, raw_content, producer, proxies, formatter


@patch("parser.web_parser.WebParser.get_content")
def test_get_news_stream(get_content, web_parser, raw_content, producer, proxies):

    get_content.return_value = raw_content("rss_news_file.txt")
    producer.parser = web_parser

    stream = producer.get_news_stream(proxies)
    result = list(stream)[-1]

    assert isinstance(result, News)


@pytest.mark.parametrize(
    "title, expected_id",
    [
        ("example////1 example", "example1example"),
        ("example%%%%%%%2 example", "example2example"),
        ("*******example-3_  xx  example", "example-3_xxexample")]
)
def test_construct_id(formatter, title, expected_id):

    result = formatter.construct_id(title)

    assert result == expected_id


def test_unify_date(formatter):
    expected = "2020-05-17 00:00:00"

    date = datetime.datetime(2020, 5, 17)
    result = formatter.unify_date(date)

    assert result == expected


def test_format_description(formatter):
    expected = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

    class Entry:
        description = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation"""
        title = "Lorem ipsum"

    class EmptyEntry:
        description = ""
        title = "Lorem ipsum"

    result = formatter.format_description(Entry)
    result_empty = formatter.format_description(EmptyEntry)

    assert result == expected
    assert result_empty == EmptyEntry.title


@pytest.mark.parametrize(
    "author, expected",[(None, "Unknown"), ("Test", "Test")]
)
def test_assing_author(formatter, author, expected):

    result = formatter.assign_author(author)

    assert result == expected
