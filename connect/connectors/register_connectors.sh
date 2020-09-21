#!/bin/sh

/etc/confluent/docker/run &
echo -e "Waiting for Kafka Connect to start listening on localhost"
while [ $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) -ne 200 ] ; do 
  echo -e $(date) " Kafka Connect listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) " (waiting for 200)"
  sleep 5 
done
echo -e $(date) "Kafka Connect is ready! Listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors)


for connector in *.json; do
  curl -s -X "POST" "http://localhost:8083/connectors" -H "Content-Type: application/json" -d @$connector
  sleep 10
done

sleep infinity