# Show Recent News

The authenticated user can access all recent news.


**URL** : `/api/v1/news/`

**Method** : `GET`

**Auth required** : YES

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Condition** : User is authenticated.

**Code** : `200 OK`

**Content** : User can see all news.

```json
{
    "count": 2,
    "next": null,
    "previous": null,
    "facets": {},
    "results": [
        {
            "title": "Chelsea boss confirms double injury boost for Brighton trip",
            "link": "https://www.eyefootball.com/news/45596/Chelsea-boss-confirms-double-injury-boost-Brighton-trip.html",
            "published": "2020-09-11 02:36:12",
            "description": "Chelsea manager Frank Lampard has confirmed that Christian Pulisic and Cesar Azpilicueta are available for selection for the Premier League opener at Brighton and Hove Albion on Monday.",
            "author": "Unknown",
            "language": "en"
        },
        {
            "title": "Frank Lampard confirms three Chelsea signings will miss Brighton game",
            "link": "https://www.eyefootball.com/news/45595/Frank-Lampard-confirms-three-Chelsea-signings-Brighton-game.html",
            "published": "2020-09-11 02:28:20",
            "description": "Chelsea manager Frank Lampard has confirmed that Hakim Ziyech, Ben Chilwell and Thiago Silva are unavailable for the Premier League opener against Brighton and Hove Albion on Monday.",
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