
import re
from dataclasses import dataclass
import atoma
from dateutil import parser
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

    def format_entry(self, entry):
        _id = self.construct_id(entry.title)
        published_date = self.unify_date(entry.pub_date)
        description = self.format_description(entry)
        author = self.assign_author(entry.author)
        return News(
            _id,
            entry.title,
            entry.link,
            published_date,
            description,
            author
        )

    @staticmethod
    def construct_id(title):
        return re.sub("[^0-9a-zA-Z_-]+", "", title).lower()

    @staticmethod
    def unify_date(date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

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
    def assign_author(author):
        return "Unknown" if not author else author
