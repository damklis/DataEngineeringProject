# DataEngineerWannabeProject

MVP - work in progress.

Check `develop` branch.

![MVP Architecture](./images/mvp_architecture.png)

## Project setup

- Run Mongo

```sh
docker-compose up -d mongo
```

```sh
docker exec mongo /usr/local/bin/init.sh
```
- Run other services

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

- Run API endpoint

```sh
python api/api.py
```