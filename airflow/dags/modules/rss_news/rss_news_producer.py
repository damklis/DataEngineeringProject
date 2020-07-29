
import re
from dataclasses import dataclass, asdict
import atoma
from dateutil import parser
from rss_news.rss_news_exporter import NewsExporter
from parser import WebParser


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

    def _extract_rss_feed(self, proxies):
        content = self.parser.get_content(proxies=proxies)
        return atoma.parse_rss_bytes(content)

    def get_news_stream(self, proxies):
        rss_feed = self._extract_rss_feed(proxies) 
        for entry in rss_feed.items:
            _id = self.construct_id(entry.title)
            published_date = self.unify_date(entry.pub_date)
            description = self.format_description(
                entry.description, entry.title
            )
            author = self.assign_author(entry.author)
            yield News(
                _id,
                entry.title,
                entry.link,
                published_date,
                description,
                author
            )

    @staticmethod
    def construct_id(title):
        return (
            re.sub("[^0-9a-zA-Z_-]+", "", title).lower()
        )

    @staticmethod
    def unify_date(date):
        return date.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def format_description(description, title):

        def short_description(description):
            tmp_description = re.sub("<.*?>", "", description[:1000])
            index = tmp_description.rfind(".")
            return tmp_description[:index+1]
        return (
            title if not description
            else short_description(description)
        )

    @staticmethod
    def assign_author(author):
        return "Unknown" if not author else author
