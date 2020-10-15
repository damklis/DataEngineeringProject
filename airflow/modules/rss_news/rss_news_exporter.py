import json
import time
from kafka import KafkaProducer


class NewsExporter:
    def __init__(self, bootstrap_servers):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: self._encode_news(x)
        )

    def _encode_news(self, value):
        return json.dumps(value).encode("utf-8")

    def __enter__(self):
        return self

    def export_news_to_broker(self, topic, record, sleep_time=0.01):
        response = self.producer.send(
            topic,
            value=record
        )
        time.sleep(sleep_time)
        return response.get(
            timeout=60
        )

    def __exit__(self, type, value, traceback):
        self.producer.close()
