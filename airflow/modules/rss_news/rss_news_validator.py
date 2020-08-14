

class NewsValidator:
    def __init__(self, description_length=100):
        self.description_length = description_length

    def validate_news(self, news):
        assert self.check_null_values(news), "Null values!"
        assert self.check_description_length(news), "Short description!"

    def check_null_values(self, news):
        news_values = list(news.as_dict().values())
        return all(news_values)

    def check_description_length(self, news):
        _news = news.as_dict()
        return len(
            _news.get("description") >= self.description_length
        )
