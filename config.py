from application.utils import get_env

# This is to configuration the api
class Config(object):
    SQLALCHEMY_DATABASE_URI = get_env('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = get_env('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_RECORD_QUERIES = get_env('SQLALCHEMY_RECORD_QUERIES')

    JWT_SECRET_KEY = get_env('ACCESS_TOKEN')

    MAIL_SERVER = get_env('MAIL_SERVER')
    MAIL_PORT = get_env('MAIL_PORT')
    MAIL_USERNAME = get_env('MAIL_USERNAME')
    MAIL_PASSWORD = get_env('MAIL_PASSWORD')
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
