# DataEngineerWannabeProject
[![Build Status](https://travis-ci.org/damklis/DataEngineerWannabeProject.svg?branch=master)](https://travis-ci.org//damklis/DataEngineerWannabeProject)

MVP - work in progress.

Check `develop` branch.


![MVP Architecture](./images/mvp_architecture.png)

## Project setup

- Run & Init Mongo replica set

```sh
docker-compose up -d mongo
```

```sh
docker exec mongo /usr/local/bin/init.sh
```

- Run services

```sh
docker-compose up -d
```

- Post Kafka Connectors

```sh
http POST localhost:8083/connectors @connect/mongo-sink.json
```

```sh
http POST localhost:8083/connectors @connect/mongo-dbz-source.json
```

```sh
http POST localhost:8083/connectors @connect/elasticsearch-sink.json
```

- Go to localhost:8080, turn on DAG `rss_news` and trigger it.
- Go to API page `http://localhost:5000/v1/api/` register and login.
- And Voila! Check the latest news about your favourite team!

    Example:
    http://localhost:5000/v1/api/news/juventus
