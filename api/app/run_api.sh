#!/bin/sh

set -xe

echo "Starting API..."

python manage.py makemigrations &&
python manage.py migrate &&
sleep 5 &&
python manage.py search_index --create &&
python manage.py runserver 0.0.0.0:5000