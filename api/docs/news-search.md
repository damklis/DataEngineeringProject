# Search News

The authenticated user can search for the specific news.


**URL** : `/api/v1/news/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Query parameters** : 
```
search=<search phrase>:
    - title=<news title>
    - description=<news description>
language=<news language>
ordering=<ordering field>
```

**Example query** : 
```
http://0.0.0.0:5000/api/v1/news/?search=title|Juventus&language=en&ordering=published
```

## Success Responses

**Condition** : User is authenticated.

**Code** : `200 OK`

**Content** : User can see the recent English news with `Juventus` phrase ordered by `published` date.

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "facets": {},
    "results": [
        {
            "title": "Juventus, Atletico Madrid keen on signing Arsenal striker",
            "link": "https://www.eyefootball.com/news/45583/Juventus-Atletico-Madrid-signing-Arsenal-striker.html",
            "published": "2020-09-10 00:19:10",
            "description": "Juventus and Atletico Madrid have explored the possibility of signing Arsenal striker Alexandre Lacazette this summer.",
            "author": "Unknown",
            "language": "en"
        }
    ]
}
```
## Error Response

**Condition** : Unauthorized User

**Code** : `401 UNAUTHORIZED`

**Content** : 
```json
{
    "detail": "Authentication credentials were not provided."
}
```