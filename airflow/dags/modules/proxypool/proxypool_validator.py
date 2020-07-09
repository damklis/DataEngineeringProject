from dataclasses import dataclass, asdict
from parser import WebParser


@dataclass(frozen=True)
class ProxyStatus:
    proxy: str 
    is_valid: bool


class ProxyPoolValidator:
    def __init__(self, url, timeout=10):
        self.timeout = timeout 
        self.parser = WebParser(url)

    def validate_proxy(self, proxy_record):
        content = self.parser.get_content(
            timeout=self.timeout,
            proxies=proxy_record.proxy
        )
        return ProxyStatus(
            proxy_record.proxy, 
            content is not None
        )
