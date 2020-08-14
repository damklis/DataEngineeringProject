import pytest
from rss_news import News

from ..fixtures import validator


def test_check_null_values(validator):
    expected = True

    news = News(
        "test_id", "test_title", "test_link",
        "test_pub","test_desc", "test_author",
        "test_lang"
    )

    result = validator.check_null_values(news)
    
    assert result is expected


def test_check_null_values_raises_error(validator):
    news = News(
        "test_id", None, "test_link",
        "test_pub", "test_desc", None,
        "test_lang"
    )
    
    with pytest.raises(AssertionError):
        validator.check_null_values(news)
