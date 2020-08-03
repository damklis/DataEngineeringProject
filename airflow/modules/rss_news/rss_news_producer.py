
import re
from dataclasses import dataclass
import atoma
from dateutil import parser
import langdetect
from parser import WebParser
from rss_news.rss_news_exporter import NewsExporter


@dataclass(frozen=True)
class News:
    _id: str
    title: str
    link: str
    published: str
    description: str
    author: str
    language: str
    
    def as_dict(self):
        return self.__dict__


class NewsProducer:
    def __init__(self, rss_feed):
        self.parser = WebParser(rss_feed, rotate_header=True)
        self.formatter = NewsFormatter()

    def _extract_news_feed_items(self, proxies):
        content = self.parser.get_content(proxies=proxies)
        news_feed = atoma.parse_rss_bytes(content)
        return news_feed.items

    def get_news_stream(self, proxies):
        news_feed_items = self._extract_news_feed_items(proxies) 
        for entry in news_feed_items:
            formatted_entry = self.formatter.format_entry(entry)
            yield formatted_entry


class NewsFormatter:
    def __init__(self):
        self.date_format = "%Y-%m-%d %H:%M:%S"
        self.id_regex = "[^0-9a-zA-Z_-]+"
        self.default_author = "Unknown"

    def format_entry(self, entry):
        _id = self.construct_id(entry.title)
        published_date = self.unify_date(entry.pub_date)
        description = self.format_description(entry)
        author = self.assign_author(entry.author)
        language = self.detect_language(entry.title)
        return News(
            _id,
            entry.title,
            entry.link,
            published_date,
            description,
            author,
            language
        )
    def assign_author(self, author):
        return self.default_author if not author else author

    def construct_id(self, title):
        return re.sub(self.id_regex, "", title).lower()

    def unify_date(self, date):
        return date.strftime(self.date_format)

    @staticmethod
    def format_description(entry):
        tmp_description = re.sub("<.*?>", "", entry.description[:1000])
        index = tmp_description.rfind(".")
        short_description = tmp_description[:index+1]
        return (
            short_description if short_description
            else entry.title
        )

    @staticmethod
    def detect_language(title):
        lower_title = title.lower()
        return langdetect.detect(lower_title)
