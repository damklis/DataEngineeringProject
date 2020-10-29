import time
from dataclasses import dataclass
from parser import WebParser
from log import log


@dataclass(frozen=True)
class ProxyStatus:
    proxy: str
    health: float
    is_valid: bool


@log
class ProxyPoolValidator:
    def __init__(self, url, timeout=10, checks=3, sleep_interval=0.1):
        self.timeout = timeout
        self.checks = checks
        self.sleep_interval = sleep_interval
        self.parser = WebParser(url, rotate_header=True)

    def validate_proxy(self, proxy_record):
        consecutive_checks = []
        for _ in range(self.checks):
            content = self.parser.get_content(
                timeout=self.timeout,
                proxies=proxy_record.proxy
            )
            time.sleep(self.sleep_interval)
            consecutive_checks.append(int(content is not None))

        health = sum(consecutive_checks) / self.checks
        proxy_status = ProxyStatus(
            proxy=proxy_record.proxy,
            health=health,
            is_valid=health > 0.66
        )
        self.logger.info(f"Proxy status: {proxy_status}")
        return proxy_status
