from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from parser import WebParser
from log import log


@dataclass
class ProxyRecord:
    ip_address: str
    port: int
    country_code: str
    country: str
    anonymity: str
    google: str
    https: str
    last_checked: str
    proxy: dict = field(init=False, default=None)

    def __post_init__(self):
        self.proxy = self.format_proxy()

    def format_proxy(self):
        protocol = "https" if self.https == "yes" else "http"
        url = f"{protocol}://{self.ip_address}:{self.port}"
        return {"http": url, "https": url}


@log
class ProxyPoolScraper:
    def __init__(self, url, bs_parser="lxml"):
        self.parser = WebParser(url)
        self.bs_parser = bs_parser

    def get_proxy_stream(self, limit):
        raw_records = self.extract_table_raw_records()
        clean_records = list(
            map(self._clear_up_record, raw_records)
        )
        for record in clean_records[:limit]:
            self.logger.info(f"Proxy record: {record}")
            if record:
                yield ProxyRecord(*record)

    def extract_table_raw_records(self):
        content = self.parser.get_content()
        soup_object = BeautifulSoup(content, self.bs_parser)
        return (
            soup_object
            .find(id="list")
            .find_all("tr")
        )

    def _clear_up_record(self, raw_record):
        return [
            val.text for val
            in raw_record.find_all("td")
        ]
