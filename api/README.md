# NEWS API

This API project is written in [Django Rest Framework](https://github.com/tomchristie/django-rest-framework).
MongoDB is the main database. Additionally, Elasticsearch serves as a query search engine.

Easily search for the latest news!

## Open Endpoints

Open endpoints require no Authentication.

* [Swagger Documentation](login.md) : `GET /api/v1/`
* [User Register](docs/user-register.md) : `POST /api/v1/user/register/`
* [User Login](docs/user-login.md) : `POST /api/v1/user/login/`


## Endpoints that require Authentication

Closed endpoints require a valid Token to be included in the header of the
request. A Token can be acquired from the `User Login` view above.

### News related

Each endpoint displays News information:

* [Show all news](docs/news-all.md) : `GET /api/v1/news/`
* [Search news](docs/news-search.md) : `GET /api/v1/news/?search=<phrase>`


### Examples
- see all news
```
http://0.0.0.0:5000/api/v1/news/ 
```
-  add `search_fields` title and description, see all of the news containing the `Robert Lewandowski` value
```
http://0.0.0.0:5000/api/v1/news/?search=Robert%20Lewandowski 
```

- find news containing the `Lewandowski` value in their titles

```
http://0.0.0.0:5000/api/v1/news/?search=title|Lewandowski 
```

- see all of the polish news containing the `Lewandowski` 

```
http://0.0.0.0:5000/api/v1/news/?search=lewandowski&language=pl
```