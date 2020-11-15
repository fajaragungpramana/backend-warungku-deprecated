import os


# This function to get .env variable configuration
# @params var - fill with the same variable name in .env configuration
def get_env(var: str):
    return os.environ.get(var)