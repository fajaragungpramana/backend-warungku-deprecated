from application.utils import get_env

# This is to configuration database mysql with the api
class Config:
    APPLICATION_ROOT = get_env('APPLICATION_ROOT')
    SQLALCHEMY_DATABASE_URL = get_env('SQLALCHEMY_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_RECORD_QUERIES = get_env('SQLALCHEMY_RECORD_QUERIES')