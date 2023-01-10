### Token validation for Flask

This package provides `jwt_required` decorator to validate JWT token in flask/flask_restx views. 
Requires `AUTH_PUBLIC_KEY` environment variable to be configured with Auth service public key.


### Usage
##### To use publickey from `AUTH_PUBLIC_KEY` env variable  (by default)
```python
from pocket_flask_jwt_validate.decorators import jwt_required

class BadgeInsertAuth(Resource):
    @jwt_required()
    def post(self):
        return {}
```
 
##### To use publickey from any other source
```python
from pocket_flask_jwt_validate.decorators import jwt_required

AUTH_PUBLIC_KEY = get_auth_public_key()

class BadgeInsertAuth(Resource):
    @jwt_required(AUTH_PUBLIC_KEY)
    def post(self):
        return {}
```

### Dependencies
Package does not declare any dependencies itself , 
however since it's made for Flask applications with JWT - it still depends on Flask and PyJWT libraries. 
