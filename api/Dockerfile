FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD app/ /app

WORKDIR /app

ENTRYPOINT [ "./run_api.sh" ]