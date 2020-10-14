

class NewsValidator:
    def __init__(self, config):
        self._config = config

    def validate_news(self, news):
        news = news.as_dict()
        assert self.check_languages(news), "Wrong language!"
        assert self.check_null_values(news), "Null values!"
        assert self.check_description_length(news), "Short description!"

    def check_null_values(self, news):
        news_values = list(news.values())
        return all(news_values)

    def check_description_length(self, news):
        description_length = self._config.get("description_length")
        return len(news.get("description")) >= description_length

    def check_languages(self, news):
        languages = self._config.get("languages")
        lang = news.get("language")
        return any(
            filter(lambda x: x == lang, languages)
        )
