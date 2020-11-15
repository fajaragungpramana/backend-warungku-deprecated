import os
import uuid

from flask import request
from datetime import datetime

# This function to get .env variable configuration
# @params var - fill with the same variable name in .env configuration
def get_env(var: str):
    return str(os.environ.get(var))

# This function to get date time now with custom format
def date_now(pattern: str):
    return datetime.now().strftime(pattern)

# This function to get user ip address
def get_ip_address():
    return request.remote_addr

# This to generate unique id
def get_unique_id():
    return str(uuid.uuid4())