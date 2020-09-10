#!/bin/sh

# Launch the worker
/etc/confluent/docker/run &
echo -e "\n\n=============\nWaiting for Kafka Connect to start listening on localhost ⏳\n=============\n"
while [ $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) -ne 200 ] ; do 
  echo -e $(date) " Kafka Connect listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) " (waiting for 200)"
  sleep 5 
done
echo -e $(date) "\n\n--------------\n\o/ Kafka Connect is ready! Listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) "\n--------------\n"

curl -s -X "POST" "http://localhost:8083/connectors" -H "Content-Type: application/json" -d @mongo-sink.json 
curl -s -X "POST" "http://localhost:8083/connectors" -H "Content-Type: application/json" -d @mongo-dbz-source.json 
curl -s -X "POST" "http://localhost:8083/connectors" -H "Content-Type: application/json" -d @elasticsearch-sink.json

sleep infinity