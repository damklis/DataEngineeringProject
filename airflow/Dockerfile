FROM puckel/docker-airflow:1.10.9

WORKDIR /usr/local/airflow

RUN mkdir python-dependencies

COPY ./requirements.txt python-dependencies

RUN pip install -r python-dependencies/requirements.txt 

ENV PYTHONPATH "${PYTHONPATH}:/usr/local/airflow/dags/modules"