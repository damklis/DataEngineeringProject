# Data Engineering Project 
[![Build Status](https://travis-ci.org/damklis/DataEngineeringProject.svg?branch=master)](https://travis-ci.org//damklis/DataEngineeringProject) [![Coverage Status](https://coveralls.io/repos/github/damklis/DataEngineeringProject/badge.svg?branch=master)](https://coveralls.io/github/damklis/DataEngineeringProject?branch=master)


**Data Engineering Project** is an implementation of the data pipeline which consumes the latest news from RSS Feeds and makes them available for users via handy API.
The pipeline infrastructure is built using popular, open-source projects.

**Access latest news and headlines in one place.** :muscle:

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [Architecture diagram](#architecture-diagram)
* [How it works](#how-it-works)
    * [Data scraping](#data-scraping)
    * [Data flow](#data-flow)
    * [Data access](#data-access)
* [Prerequisites](#prerequisites)
* [Running project](#running-project)
* [API](#api)
* [Testing](#testing)
* [References](#references)
* [Contributions](#contributions)
* [License](#license)
* [Contact](#contact)

<!-- ARCHITECTURE DIAGRAM -->
## Architecture diagram

![MVP Architecture](./images/architecture_diagram.png)


<!-- HOW IT WORKS -->
## How it works

#### Data Scraping
Airflow DAG is responsible for the execution of Python scraping modules.
- First task updates **proxypool**. Using proxies in combination with rotating user agents can help get scrapers past most of the anti-scraping measures and prevent being detected as a scraper.

- Second task extracts news from RSS feeds provided in the configuration file, validates the quality and sends data into **Kafka topic A**. The extraction process is using proxies from **proxypool**.

#### Data flow
- Kafka Connect **Mongo Sink** consumes data from **Kafka topic A** and stores news in MongoDB.
- **Debezium MongoDB Source** tracks a MongoDB replica set for document changes in databases and collections, recording those changes as events in **Kafka topic B**.
- Kafka Connect **Elasticsearch Sink** consumes data from **Kafka topic B** and stores news in Elasticsearch. Data replication between topics **A** and **B** ensures MongoDB and ElasticSearch Synchronization.

#### Data access
- Data gathered by previous steps can be easily accessed using [API](api) endpoints.

<!-- PREREQUISITES -->
## Prerequisites
Software required to run project:
- [Docker](https://docs.docker.com)
- [Python 3.8+ (pip)](https://www.python.org/)
- [docker-compose](https://docs.docker.com)

```sh
python -m pip install docker-compose
```

<!-- RUNNING PROJECT -->
## Running project
Script `manage.sh` - wrapper for `docker-compose` works as a managing tool.

- Build project infrastructure
```sh
./manage.sh up
```

- Stop project infrastructure
```sh
./manage.sh stop
```

- Delete project infrastructure
```sh
./manage.sh down
```


<!-- API -->
## API
See detailed documentation in [API](api) module.

Example searches:
- see all news
```
http://0.0.0.0:5000/api/v1/news/ 
```
-  add `search_fields` title and description, see all of the news containing the `Robert Lewandowski` phrase
```
http://0.0.0.0:5000/api/v1/news/?search=Robert%20Lewandowski 
```

- find news containing the `Lewandowski` phrase in their titles

```
http://0.0.0.0:5000/api/v1/news/?search=title|Lewandowski 
```

- see all of the polish news containing the `Lewandowski` phrase

```
http://0.0.0.0:5000/api/v1/news/?search=lewandowski&language=pl
```

<!-- TESTING -->
## Testing
Script `run_tests.sh` executes unit tests against Airflow scraping modules and Django Rest Framework applications.

```sh
./run_tests.sh
```

<!-- REFERENCES -->
## References
Inspired by following codes, articles and videos:

* [How we launched a data product in 60 days with AWS](https://towardsdatascience.com/launching-beta-data-product-within-two-month-with-aws-6ac6b55a9b5d)
* [Toruń JUG #55 - "Kafka Connect - szwajcarski scyzoryk w rękach inżyniera?" - Mariusz Strzelecki](https://www.youtube.com/watch?v=iiz6t8g5t6Q)
* [Kafka Elasticsearch Sink Connector and the Power of Single Message Transformations](https://sap1ens.com/blog/2020/05/23/kafka-elasticsearch-sink-connector-and-the-power-of-single-message-transformations/)


<!-- CONTRIBUTIONS -->
## Contributions
Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.


<!-- CONTACT -->
## Contact
If you have any questions or suggestions please feel free to contact me.
Damian Kliś [@DamianKlis](https://twitter.com/DamianKlis)