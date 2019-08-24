from datetime import datetime
from flask import current_app
from flask_restful import Resource, reqparse
from src.model import UserModel
from src.utils.security.jwt_security import decode_jwt


class User(Resource):

    @staticmethod
    def get_secret_key():
        """Provides secret key config via application context
        
        Returns:
            str: Secret key from env
        
        """
        return current_app.config['SECRET_KEY']

    @staticmethod
    def get_user_details_parsed_args():
        """Parses arguments received from the request.
        
        Returns:
            A dictionary of the parsed request arguments

        """
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str,
                            help='Email address used to login. This should be a string',
                            required=True)
        parser.add_argument('name', type=str, help='The name of the user', required=True)
        return parser.parse_args()

    @staticmethod
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

    @staticmethod
    def get_user_id_parsed_args():
        """Parses user id arg received from the HTTP request.

        Returns:
            A dictionary of the parsed request argument
        
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, help='The ID for the user', required=True)
        return parser.parse_args()

    @staticmethod
    def get_user_password_parsed_args():
        """Parses user password arg received from the HTTP request.

        Returns:
            A dictionary of the parsed request argument

        """
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, help='The password for the user', required=True)
        return parser.parse_args()

    @staticmethod
    def check_existing_user(email_address):
        """Returns query object of an existing user or null"""
        return UserModel.query.filter_by(email=email_address).first()

    def get(self):
        """Returns user details as HTTP response based on HTTP request
        
        Returns:
            JSON object: A 200 HTTP status response with details of a user

            JSON object: A 404 HTTP status response for a non-existing user

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status 
            and JSON content-type response

        """
        data_token = self.get_auth_token()
        
        try:
            # check token validity
            decoded_token_response = decode_jwt(data_token, self.get_secret_key())

            if isinstance(decoded_token_response, int):
                user = UserModel.query.filter_by(id=decoded_token_response).first()

                if user:
                    response = {
                        "user_id": user.id,
                        "name": user.name,
                        "email": user.email
                    }
                    return response, 200
                else:
                    return {"message": "This user does not exist"}, 404
            else:
                return {"message": decoded_token_response}, 403
        except Exception as e:
            return {"message": str(e)}, 500

    def post(self):
        """Registers a new user via POST HTTP request
        
        Returns:
            JSON object: A 200 HTTP status response with name of the user

            JSON object: A 404 HTTP status response for an existing user

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and 
                JSON content-type response

        """
        data_user_details = self.get_user_details_parsed_args()
        data_password = self.get_user_password_parsed_args()

        try:
            # check if user exists by using email address value
            if not self.check_existing_user(data_user_details['email']):
                user = UserModel(
                    email=data_user_details['email'],
                    name=data_user_details['name'],
                    password=UserModel.generate_hash(data_password['password'])
                )
                user.save_to_db()
                return {"message": "User {} was created".format(data_user_details['name'])}, 200
            else:
                return {"message": "That email address already exists"}, 400
        except Exception as e:
            return {"message": str(e)}, 500

    def put(self):
        """Updates details of a user via PUT HTTP request
        
        Returns:
            JSON object: A 200 HTTP status response with name of the user that was updated

            JSON object: A 404 HTTP status response for a user that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and 
                JSON content-type response

        """
        data_user_id = self.get_user_id_parsed_args()
        data_user_details = self.get_user_details_parsed_args()
        data_password = self.get_user_password_parsed_args()

        try:
            user = UserModel.query.filter_by(id=data_user_id['user_id']).first()

            if user:
                user.email = data_user_details['email']
                user.name = data_user_details['name']
                user.password = UserModel.generate_hash(data_password['password'])
                user.updated_at = datetime.utcnow()
                user.save_to_db()
                return {"message": "User {} was updated".format(data_user_details['name'])}, 200
            else:
                return {"message": "This user does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500

    def delete(self):
        """Deletes a user via DELETE HTTP request
        
        Returns:
            JSON object: A 200 HTTP status response with confirmation message of the deleted user

            JSON object: A 404 HTTP status response for a user that does not exist

        Raises:
            Exception: General exceptions aligned to SQLAlchemy in the form of a 500 HTTP status and 
                JSON content-type response

        """
        data_user_id = self.get_user_id_parsed_args()

        try:
            user = UserModel.query.filter_by(id=data_user_id['user_id']).first()

            if user:
                user.delete_from_db()
                return {"message": "This user has been deleted successfully"}, 200
            else:
                return {"message": "This user does not exist"}, 404
        except Exception as e:
            return {"message": str(e)}, 500
