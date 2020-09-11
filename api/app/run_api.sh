#!/bin/sh

echo "Starting API..."

python manage.py makemigrations &
python manage.py migrate &
echo -e "Waiting for Elasticsearch to start listening..."
while [ $(curl -s -o /dev/null -w %{http_code} http://elasticsearch:9200) -ne 200 ] ; do 
  echo -e $(date) " Elasticsearch HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://elasticsearch:9200) " (waiting for 200)"
  sleep 5 
done
echo -e $(date) "Elasticsearch is ready!"
python manage.py search_index --create &
python manage.py runserver 0.0.0.0:5000 