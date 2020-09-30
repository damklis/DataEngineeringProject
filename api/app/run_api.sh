#!/bin/sh

echo "Starting API..."

python manage.py makemigrations &
python manage.py migrate --run-syncdb &
echo -e "Waiting for Elasticsearch to start listening..."
while [ $(curl -s -o /dev/null -w %{http_code} http://$ELASTIC_HOST:9200) -ne 200 ] ; do 
  echo -e $(date) " Elasticsearch HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://$ELASTIC_HOST:9200) " (waiting for 200)"
  sleep 5 
done
echo -e $(date) "Elasticsearch is ready! HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://$ELASTIC_HOST:9200)

echo -e "Creating Django-Elastic index"
python manage.py search_index --create &
python manage.py collectstatic --noinput &
uwsgi --socket :8000 --master --enable-threads --module core.wsgi
