#!/bin/sh

docker-compose run airflow sh -c "python -m pytest -v --show-capture=no" \
&& docker-compose up -d mongo \
&& sleep 5 \
&& docker exec -it mongo /usr/local/bin/init.sh \
&& docker-compose up -d api \
&& sleep 5 \
&& docker exec -it api ./manage.py test -k \
&& python -m flake8 -v 