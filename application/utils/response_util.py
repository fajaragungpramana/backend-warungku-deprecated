from http import HTTPStatus

from . import json_response

# Handle response invalid api key
def http_forbidden():
    return json_response({
        'status': 'Forbidden',
        'message': 'Invalid api key!',
        'data': None
    }, HTTPStatus.FORBIDDEN)

# Handle response bad data sent from client
def http_bad_request(message: str, data = None):
    return json_response({
        'status': 'Bad Request',
        'message': message,
        'data': data
    }, HTTPStatus.BAD_REQUEST)