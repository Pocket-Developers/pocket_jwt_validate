### JWT Token validation for Pocket services


### Usage

```python
from pocket_jwt_validate.utils import validate_jwt, JwtValidationException

try:
    jwt_token = validate_jwt(request.header.get('Authorization'))
except JwtValidationException:
    raise Unauthorized()
```
