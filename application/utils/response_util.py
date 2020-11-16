from flask import jsonify, make_response
from http import HTTPStatus

# Handle response invalid api key
def http_forbidden():
    return make_response(jsonify({
        'status' : 'Forbidden',
        'message' : 'Invalid api key!'
    })), HTTPStatus.FORBIDDEN