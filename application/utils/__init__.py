import os
import uuid
import requests

from datetime import datetime

# This function to get .env variable configuration
# @params var - fill with the same variable name in .env configuration
def get_env(var: str):
    return str(os.environ.get(var))

# This function to get date time now with custom format
def date_now(pattern: str = '%d %b %Y %H:%M:%S'):
    return datetime.now().strftime(pattern)

# This function to get user ip address
def get_ip_address():
    return requests.get('https://ipinfo.io/').json()['ip']

# This to generate unique id
def get_unique_id():
    return str(uuid.uuid4())

# This to verify value is none or not
def is_none(value):
    if value is not None:
        return True
    return False