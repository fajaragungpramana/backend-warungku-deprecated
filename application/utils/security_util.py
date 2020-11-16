from functools import wraps
from flask import request

from application.utils import get_env, response_util

def access_key(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('access_key_owner') == get_env('ACCESS_KEY_OWNER'):
            return view_function(*args, **kwargs)
        else:
            return response_util.http_forbidden()
    return decorated_function