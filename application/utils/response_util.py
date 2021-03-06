from http import HTTPStatus

from . import json_response

# Handle response invalid api key
def http_forbidden():
    return json_response({
        'status': 'Forbidden',
        'message': 'Invalid api key!',
        'data': None
    }, HTTPStatus.FORBIDDEN)

# Handle response server error
def http_internal_server_error():
    return json_response({
        'status': 'Internal Server Error',
        'message': 'Something wrong. Please, try again!',
        'data': None
    }, HTTPStatus.INTERNAL_SERVER_ERROR)

# Handle response ok
def http_ok(message: str, data = None):
    return json_response({
        'status': 'Ok',
        'message': message,
        'data': data
    }, HTTPStatus.OK)

# Handle response server created new data
def http_created(message: str, data = None):
    return json_response({
        'status': 'Created',
        'message': message,
        'data': data
    }, HTTPStatus.CREATED)

# Handle response accepted
def http_accepted(message: str, data = None):
    return json_response({
        'status': 'Accepted',
        'message': message,
        'data': data
    }, HTTPStatus.ACCEPTED)

# Handle response bad data sent from client
def http_bad_request(message: str, data = None):
    return json_response({
        'status': 'Bad Request',
        'message': message,
        'data': data
    }, HTTPStatus.BAD_REQUEST)

# Handle response data sent not accepted
def http_not_acceptable(message: str, data = None):
    return json_response({
        'status': 'Not Acceptable',
        'message': message,
        'data': data
    }, HTTPStatus.NOT_ACCEPTABLE)

# Handle response user unauthorized
def http_unauthorized(message: str, data = None):
    return json_response({
        'status': 'Unauthorized',
        'message': message,
        'data': data
    }, HTTPStatus.UNAUTHORIZED)

# Handle response not found
def http_not_found(message: str, data = None):
    return json_response({
        'status': 'Not Found',
        'message': message,
        'data': data
    }, HTTPStatus.NOT_FOUND)