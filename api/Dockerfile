FROM python:3

ADD service/ /service

WORKDIR /service

RUN apt-get update -y 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]