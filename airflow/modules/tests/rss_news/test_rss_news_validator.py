import pytest
from rss_news import News

from ..fixtures import validator, news_record


def test_check_null_values(validator, news_record):
    expected = True

    news = news_record.as_dict()

    result = validator.check_null_values(news)
    
    assert result is expected


def test_check_null_values_with_nones(validator, news_record):
    expected = False

    news = news_record.as_dict()
    news["id"] = None
    
    result = validator.check_null_values(news)

    assert result is expected


def test_check_languages(validator, news_record):
    expected = True

    news = news_record.as_dict()
    
    result = validator.check_languages(news)

    assert result is expected


def test_validate_news_raises_error(validator, news_record):
    
    with pytest.raises(AssertionError):
        validator.validate_news(news_record)
