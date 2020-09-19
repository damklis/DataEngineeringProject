# DataEngineeringProject
[![Build Status](https://travis-ci.org/damklis/DataEngineeringProject.svg?branch=master)](https://travis-ci.org//damklis/DataEngineeringProject)

## Architecture


![MVP Architecture](./images/mvp_architecture.png)

## Project setup

- Run infrastructure

```sh
./manage.sh up
```

- Go to localhost:8080, turn on DAG `rss_news` and trigger it.
- Go to API page `http://localhost:5000/api/v1/` register and login.
- And Voila! Check the latest news about your favourite team!
Example:

```
http://localhost:5000/api/v1/news/?search=juventus
```