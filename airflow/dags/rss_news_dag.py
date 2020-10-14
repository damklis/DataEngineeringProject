from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dags_config import Config as config

from rss_news import export_news_to_broker
from proxypool import update_proxypool


LANGUAGE = "en"


def dummy_callable(task_id, action, dag):
    def foo(action):
        return f"{datetime.now()}: {action} scrapping RSS feeds!"

    return PythonOperator(
        task_id=task_id,
        python_callable=foo,
        op_kwargs={"action": action},
        dag=dag
    )


def exporting_events(config, rss_feed, language, dag):
    return PythonOperator(
        task_id=f"exporting_{rss_feed}_news_to_broker",
        python_callable=export_news_to_broker,
        op_kwargs={
            "config": config, "rss_feed": rss_feed, "language": language
        },
        dag=dag
    )


dag = DAG(
    "rss_news_dag",
    description="scrape rss feeds and export events to broker via proxypool",
    schedule_interval="*/10 * * * *",
    start_date=datetime(2020, 1, 1),
    catchup=False,
    is_paused_upon_creation=False
)

proxypool = PythonOperator(
    task_id="updating_proxypoool",
    python_callable=update_proxypool,
    op_kwargs={"config": config},
    dag=dag
)

start = dummy_callable("starting_pipeline", "started", dag)

exporting_tasks = [
    exporting_events(config, rss_feed, LANGUAGE, dag)
    for rss_feed in config.RSS_FEEDS[LANGUAGE]
]

finish = dummy_callable("finishing_pipeline", "finished", dag)

start >> proxypool >> exporting_tasks >> finish
