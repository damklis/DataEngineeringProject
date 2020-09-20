#!/bin/sh

docker-compose run airflow sh -c "python -m pytest -v --show-capture=no" \
&& docker-compose up -d mongo \
&& docker exec -it mongo /usr/local/bin/init.sh \
&& docker-compose run api sh -c "./manage.py test -k" \
&& python -m flake8 -v 