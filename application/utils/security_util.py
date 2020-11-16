from functools import wraps
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

from application.utils import get_env, response_util

# Access key owner, using this to end point WarungKu-Owner
def access_key_owner(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('access_key_owner') == get_env('ACCESS_KEY_OWNER'):
            return view_function(*args, **kwargs)
        else:
            return response_util.http_forbidden()
    return decorated_function

# Hashing password from user
def hash_password(password: str):
    return generate_password_hash(password)

# Verify password from user
def verify_password(hashed_password: str, password: str):
    return check_password_hash(hashed_password, password)
