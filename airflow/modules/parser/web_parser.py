
import re
import random
from contextlib import closing
from requests import get
from log import log
from parser.random_headers_list import headers_list


@log
class WebParser:
    def __init__(self, website_url, rotate_header=True):
        self.url = website_url
        self._rotate_header = rotate_header

    def get_random_header(self):
        if self._rotate_header:
            return random.choice(headers_list)

    def get_content(self, timeout=30, proxies=None):
        kwargs = {
            "timeout": timeout,
            "proxies": proxies,
            "headers": self.get_random_header()
        }
        try:
            with closing(get(self.url, **kwargs)) as response:
                if self.is_good_response(response):
                    return (
                        response.content
                    )
        except Exception as err:
            self.logger.info(f"Error occurred: {err}")

    @staticmethod
    def is_good_response(response):
        content_type = response.headers['Content-Type'].lower()
        return (
            response.status_code == 200
            and content_type is not None
        )

    def __str__(self):
        domain = re.sub("(http[s]?://|www.)", "", self.url)
        return f"WebParser of {domain.upper()}"
