# Admin News Management

The Admin User can manage all news.


**URL** : `/admin/api/news/`

**Method** : `GET/POST/DELETE/PATCH/PUT`

**Auth required** : YES

**Permissions required** : `IsAdminUser`

**Data constraints** : `{}`

## Success Responses

**Condition** : Admin User is authenticated.

**Code** : `200 OK`

**Content** : Admin User can manage all news.

**Methods** :

- List all available resources `GET /admin/api/news/`
- Create a new entry `POST /admin/api/news/`
- Delete existing resource`DELETE /admin/api/news/{_id}/`
- Get individual resource`GET /admin/api/news/{_id}/`
- Make partial changes `PATCH /admin/api/news/{_id}/`
- Create a new resource/Replace target resource `PUT /admin/api/news/{_id}/`


## Error Response

**Condition** : Unauthorized User

**Code** : `401 UNAUTHORIZED`

**Content** : 
```json
{
    "detail": "Authentication credentials were not provided."
}
```