#!/bin/sh

wait="sleep 15"

docker-compose run airflow sh -c "python -m pytest -v --show-capture=no" \
&& python -m flake8 -v \
&& docker-compose up -d mongo \
&& eval $wait \
&& docker exec -it mongo /usr/local/bin/init.sh \
&& docker-compose up -d api \
&& eval $wait \
&& docker exec -it api ./manage.py test -k