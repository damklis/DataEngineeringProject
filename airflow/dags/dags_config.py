

class Config:

    PROXY_WEBPAGE = "https://free-proxy-list.net/"

    TESTING_URL = "https://google.com"

    REDIS_CONFIG = {
        "host": "redis",
        "port": "6379",
        "db": 0 
    }

    REDIS_KEY = "proxies"

    MAX_WORKERS = 15

    NUMBER_OF_PROXIES = 50

    RSS_FEEDS = {
        "sportowefakty": "https://sportowefakty.wp.pl/rss.xml",
        "przegladsportowy": "https://deadspin.com/rss"
    }

    BOOTSTRAP_SERVERS = ["kafka:9092"] 

    TOPIC = "rss"
