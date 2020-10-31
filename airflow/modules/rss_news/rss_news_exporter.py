import json
import time
from kafka import KafkaProducer


class NewsExporter:
    def __init__(self, bootstrap_servers):
        self._producer = self._connect_producer(
            bootstrap_servers
        )

    def _connect_producer(self, bootstrap_servers):
        def encode_news(value):
            return json.dumps(value).encode("utf-8")

        producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda x: encode_news(x)
        )
        return producer

    def __enter__(self):
        return self

    def export_news_to_broker(self, topic, record, sleep_time=0.01):
        response = self._producer.send(
            topic,
            value=record
        )
        time.sleep(sleep_time)
        return response.get(
            timeout=60
        )

    def __exit__(self, type, value, traceback):
        self._producer.close()
