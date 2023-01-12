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
    """
    On each JwtValidationException the application should return 401 response.
    :param auth_header: String like `Bearer sdfkjhsdfkjhsdkfjhsdkfjhsdkfjhsdkjf`
    :return: Decoded JWT. Or raises JwtValidationException

    """
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''

    if auth_token:
        pk = _format_keystring_as_pem(PUBLIC_KEY)
        try:
            decoded = jwt.decode(auth_token, key=pk, algorithms=["ES256"])
            return decoded
            # here we can provide some info from JWT to view function if required
        except jwt.exceptions.PyJWTError as e:
            raise JwtValidationException()
        except Exception as e:
            raise JwtValidationException()
        # if all is fine - we'll call a view function
    else:
        raise JwtValidationException()
