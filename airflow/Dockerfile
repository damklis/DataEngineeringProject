FROM puckel/docker-airflow:1.10.9

WORKDIR /usr/local/airflow

RUN mkdir python-dependencies

COPY ./requirements.txt python-dependencies

RUN pip install -r python-dependencies/requirements.txt 

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/airflow/dags/modules"
ENV EXECUTOR "Local"
ENV AIRFLOW__SCHEDULER__MIN_FILE_PROCESS_INTERVAL "15"
ENV AIRFLOW__WEBSERVER__WORKER_REFRESH_INTERVAL "450"
ENV AIRFLOW__WEBSERVER__WEB_SERVER_WORKER_TIMEOUT "150"

COPY ./run_unit_tests.sh /usr/local/airflow/dags