import os

from datetime import datetime

# This function to get .env variable configuration
# @params var - fill with the same variable name in .env configuration
def get_env(var: str):
    return os.environ.get(var)

# This function to get date time now with custom format
def date_now(pattern: str):
    return datetime.now().strftime(pattern)