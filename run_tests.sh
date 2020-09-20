#!/bin/sh

docker-compose run airflow sh -c "python -m pytest -v --show-capture=no" \
&& python -m flake8 -v \
&& docker-compose run api sh -c "./manage.py test -k"