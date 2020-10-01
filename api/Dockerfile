FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD app/ /app

WORKDIR /app

RUN chmod +x ./run_api.sh \
&& adduser api

USER api

CMD [ "./run_api.sh" ]