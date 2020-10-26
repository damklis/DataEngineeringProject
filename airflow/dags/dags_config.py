

class Config:

    PROXY_WEBPAGE = "https://free-proxy-list.net/"

    TESTING_URL = "https://google.com"

    REDIS_CONFIG = {
        "host": "redis",
        "port": "6379",
        "db": 0
    }

    REDIS_KEY = "proxies"

    MAX_WORKERS = 50

    NUMBER_OF_PROXIES = 50

    RSS_FEEDS = {
        "en": [
            "https://www.goal.com/feeds/en/news",
            "https://www.eyefootball.com/football_news.xml",
            "https://www.101greatgoals.com/feed/",
            "https://sportslens.com/feed/",
            "https://deadspin.com/rss"
        ],
        "pl": [
            "https://weszlo.com/feed/",
            "https://sportowefakty.wp.pl/rss.xml",
            "https://futbolnews.pl/feed",
            "https://igol.pl/feed/"
        ],
        "es": [
            "https://as.com/rss/tags/ultimas_noticias.xml",
            "https://e00-marca.uecdn.es/rss/futbol/mas-futbol.xml",
            "https://www.futbolred.com/rss-news/liga-de-espana.xml",
            "https://www.futbolya.com/rss/noticias.xml"
        ],
        "de": [
            "https://www.spox.com/pub/rss/sport-media.xml",
            "https://www.dfb.de/news/rss/feed/"
        ]
    }

    BOOTSTRAP_SERVERS = ["kafka:9092"]

    TOPIC = "rss_news"

    VALIDATOR_CONFIG = {
        "description_length": 10,
        "languages": [
            "en", "pl", "es", "de"
        ]
    }
