import jwt
import os


def _format_keystring_as_pem(key_string: str):
    return f"""-----BEGIN PUBLIC KEY-----
{key_string}
-----END PUBLIC KEY-----"""


PUBLIC_KEY = os.environ.get('AUTH_PUBLIC_KEY')


class JwtValidationException(Exception):
    pass


def validate_jwt(auth_header: str) -> dict:
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        pk = _format_keystring_as_pem(public_key)
        try:
            decoded = jwt.decode(auth_token, key=pk, algorithms=["ES256"])
            return decoded
            # here we can provide some info from JWT to view function if required
        except jwt.exceptions.PyJWTError as e:
            raise Unauthorized()
        except Exception as e:
            raise Unauthorized()
        # if all is fine - we'll call a view function
    else:
        raise Unauthorized()
