from application.utils import get_env

# This is to configuration database mysql with the api
class Config(object):
    SQLALCHEMY_DATABASE_URI = get_env('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_RECORD_QUERIES = get_env('SQLALCHEMY_RECORD_QUERIES')