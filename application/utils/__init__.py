import os
import uuid
import requests

from datetime import datetime

from dotenv import load_dotenv
from flask import jsonify, make_response, request

# get .env path and set it
load_dotenv('../backend-warungku/.env')

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

# This to make json response
def json_response(response: dict, http_code: int):
    return make_response(jsonify(response)), http_code

# This to verify value is none or not
def is_none(value):
    return isinstance(value, type(None))

# This to get body or form data
def get_post(var: str):
    return request.form.get(var)

# This to get parameter
def get_param(var: str):
    return request.args.get(var)