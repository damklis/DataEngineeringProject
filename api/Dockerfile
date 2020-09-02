FROM python:3

ADD app/ /app

WORKDIR /app 

RUN pip install -r requirements.txt \ 
    && python manage.py makemigrations news \
    && python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]