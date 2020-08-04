from dataclasses import dataclass
from parser import WebParser
from log import log


@dataclass(frozen=True)
class ProxyStatus:
    proxy: str
    is_valid: bool


@log
class ProxyPoolValidator:
    def __init__(self, url, timeout=10):
        self.timeout = timeout
        self.parser = WebParser(url, rotate_header=True)

    def validate_proxy(self, proxy_record):
        content = self.parser.get_content(
            timeout=self.timeout,
            proxies=proxy_record.proxy
        )
        proxy_status = ProxyStatus(
            proxy_record.proxy,
            content is not None
        )
        self.logger.info(f"Proxy status: {proxy_status}")
        return proxy_status
