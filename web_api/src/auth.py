from flask_restful import Resource, reqparse
from flask import current_app
from src.model import UserModel, BlacklistedTokens
from src.utils.security.jwt_security import encode_jwt, decode_jwt
from src.utils.security.helper import get_auth_token, get_secret_key


class Login(Resource):

    @staticmethod
    def get_login_details():
        """Parses login data from the POST requests
        
        Returns:
            JSON object: Email and password keys containing the mapped values from the POST request

        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='The email of the user is required', required=True)
        parser.add_argument('password', type=str, help='The password of the user', required=True)
        return parser.parse_args()
    
    def post(self):
        """Receives data from HTTP POST request

        Returns:
            JSON object: 200 HTTP response with a dictionary of a user's details

            JSON object: 403 HTTP response with a dictionary of an error message
            
            JSON object: 404 HTTP response with a dictionary of an error message
            
            JSON object: 500 HTTP response with a dictionary of an error message

        """
        data = self.get_login_details()

        try:
            user = UserModel.query.filter_by(email=data['email']).first()

            # return 404 response if user's email does not exist
            if not user:
                return {"message": "This user does not exist"}, 404
            else:
                # get authentication token
                auth_token = encode_jwt(subject_id=user.id, secret=get_secret_key())

                # verify password and return 403 response if it's wrong
                if UserModel.verify_hash(data['password'], user.password):
                    response = {
                        "user_id": user.id,
                        "message": "Logged in as {}".format(user.name),
                        "auth_token": auth_token.decode()  # decode from bytes to string
                    }
                    return response, 200
                else:
                    return {"message": "wrong user credentials"}, 401
        except Exception as e:
            return {"message": str(e)}, 500


class Logout(Resource):

    def post(self):
        data_token = get_auth_token()

        try:
            # check token validity
            decoded_token_response = decode_jwt(data_token, get_secret_key())

            if isinstance(decoded_token_response, int):
                # check if token is in the blacklist
                token_check = BlacklistedTokens.check_blacklisted_token(data_token)

                if token_check:  # if true mention given token has been blacklisted
                    return {"message": "The token has been revoked. Please log in again"}, 401
                else:  # when false save token to table for black listed tokens
                    blacklisted_token = BlacklistedTokens(token=data_token)
                    blacklisted_token.save_to_db()
                    return {"message": "Logged out successfully"}, 200
            else:
                return {"message": decoded_token_response}, 401
        except Exception as e:
            print(str(e))
            return {"message": str(e)}, 500
