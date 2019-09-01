from flask_restful import reqparse
from flask import current_app


def get_secret_key():
    """Provides secret key config via application context

    Returns:
        str: Secret key from environment variable

    """
    return current_app.config['SECRET_KEY']


def get_auth_token():
    """Parses the authentication token from the HTTP request body.

    Returns:
        A dictionary of the parsed request argument

    """
    parser = reqparse.RequestParser()
    parser.add_argument('Authorization',
                        location='headers',
                        help='The authentication token in the Authorization header \
                             is required to access this resource',
                        required=True)

    auth_token = parser.parse_args()
    return auth_token['Authorization'].split()[1]