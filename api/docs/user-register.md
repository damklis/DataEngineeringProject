# Register

Used to register a new User.

**URL** : `/api/v1/user/register/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[valid email address]",
    "password": "[password in plain text]"
}
```

**Data example**

```json
{
    "username": "exampleuser@example.com",
    "password": "abcd1234"
}
```

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "exampleuser@example.com"
}
```

## Error Response

**Condition** : If `password` is to short.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "password": [
        "Ensure this field has at least 5 characters."
    ]
}
```