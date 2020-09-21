#!/bin/sh

argument=$1

if [ $argument = "up" ]; then
    echo "Creating infrastructure..."
    docker-compose up -d mongo
    sleep 2
    docker exec -it mongo /usr/local/bin/init.sh
    sleep 2
    docker-compose up -d
elif [ $argument = "stop" ]; then
    echo "Stopping infrastructure..."
    docker-compose stop
elif [ $argument = "down" ]; then
    echo "Deleting infrastructure..."
    docker-compose down
else
  echo "Unknown argumnet! Options: up, stop, down"
fi