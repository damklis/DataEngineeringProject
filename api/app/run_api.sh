#!/bin/sh

set -xe

python manage.py makemigrations &&
python manage.py migrate &&
python manage.py search_index --create &&
python manage.py runserver 0.0.0.0:5000