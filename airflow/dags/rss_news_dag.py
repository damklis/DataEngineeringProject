from urllib.parse import urlparse
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from dags_config import Config as config
from rss_news import export_news_to_broker
from proxypool import update_proxypool


def extract_feed_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc.replace("www.", "")


def dummy_callable(action):
    return f"{datetime.now()}: {action} scrapping RSS feeds!"


def export_events(config, rss_feed, language, dag):
    feed_name = extract_feed_name(rss_feed)
    return PythonOperator(
        task_id=f"exporting_{feed_name}_news_to_broker",
        python_callable=export_news_to_broker,
        op_kwargs={
            "config": config, "rss_feed": rss_feed, "language": language
        },
        dag=dag
    )


def create_dag(dag_id, interval, config, language, rss_feeds):
    with DAG(
        dag_id=dag_id,
        description=f"Scrape latest ({language}) sport RSS feeds",
        schedule_interval=interval,
        start_date=datetime(2020, 1, 1),
        catchup=False,
        is_paused_upon_creation=False
    ) as dag:

        start = PythonOperator(
            task_id="starting_pipeline",
            python_callable=dummy_callable,
            op_kwargs={"action": "starting"},
            dag=dag
        )

        proxypool = PythonOperator(
            task_id="updating_proxypoool",
            python_callable=update_proxypool,
            op_kwargs={"config": config},
            dag=dag
        )

        events = [
            export_events(config, rss_feed, language, dag)
            for rss_feed in rss_feeds.values()
        ]

        finish = PythonOperator(
            task_id="finishing_pipeline",
            python_callable=dummy_callable,
            op_kwargs={"action": "finishing"},
            dag=dag
        )

        start >> proxypool >> events >> finish

    return dag


for n, item in enumerate(config.RSS_FEEDS.items()):
    language, rss_feeds = item
    dag_id = f"rss_news_{language}"
    interval = f"{n*5}-59/10 * * * *"

    globals()[dag_id] = create_dag(
        dag_id, interval, config, language, rss_feeds
    )
