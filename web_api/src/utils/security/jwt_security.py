# module that handles the securing of API resources using JSON Web Tokens
import jwt
from datetime import datetime, timedelta


def set_payload(subject_id):
    """Generates JWT payload
    
    Args:
        subject_id : An integer value representing the user's id obtained from Users table
    
    Returns:
        dict: A dictionary mapping the payload values consisting of subject id, current UTC time
        and expiry UTC time
    """
    # set expiry time for token to be 2 hours from time of creation
    current_time = datetime.utcnow()
    expiry_time = current_time + timedelta(hours=24)  # add 2 hours to the current time

    payload = {
        "sub": subject_id,
        "iat": current_time.timestamp(),
        "exp": expiry_time.timestamp()
    }
    return payload


def encode_jwt(subject_id='', secret='', alg='HS256'):
    """Generates JWT authentication token
    
    Args:
        subject_id: An integer value representing the user's id obtained from Users table

        secret: Secret key from environment variable

        algorithm: The type of algorithm used to encrypt the JWT

    Returns:
        str: Encoded JWT
    """
    try:
        return jwt.encode(set_payload(subject_id), secret, algorithm=alg)
    except Exception as e:
        return str(e)


def decode_jwt(encoded_jwt, secret='', alg='HS256'):
    """Decodes JWT authentication token

    Args:
        encoded_jwt: A string of the JWT

        secret: Secret key from environment variable

        algorithm: The type of algorithm used to decode the JWT

    Returns:
        int: The user's id

    Raises:
        ExpiredSignatureError: An error generated when token signature has expired

        InvalidTokenError: An error generated when submitted token is invalid
    """
    try:
        payload = jwt.decode(encoded_jwt, secret, algorithms=alg)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again."
    except jwt.InvalidTokenError:
        return "Invalid token. Please log in again."
