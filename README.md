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

- Run other services

```sh
docker-compose up -d
```

- Go to localhost:8080, turn on DAG `rss_news` and trigger it.
- Go to API page `http://localhost:5000/api/v1/` register and login.
- And Voila! Check the latest news about your favourite team!

    Example:
    http://localhost:5000/api/v1/news/?search=juventus
