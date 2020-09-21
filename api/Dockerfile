FROM python:3

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD app/ /app

WORKDIR /app

RUN chmod +x ./run_api.sh

CMD [ "./run_api.sh" ]