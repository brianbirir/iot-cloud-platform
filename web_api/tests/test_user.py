import unittest
import requests
from flask import Flask
from flask_testing import TestCase


class UserTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_get_user_details(self):
        # login user
        login_response = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com",
                  "password": "1234567891"}
        )
        token = login_response.json()['auth_token']
        headers = {'Authorization': 'Bearer ' + token}
        
        # get user details
        user_response = requests.get(
            'http://127.0.0.1:5000/api/user',
            headers=headers
        )
        self.assert200(user_response)

    def test_invalid_token(self):
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\
            .eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ\
                .SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        headers = {'Authorization': 'Bearer ' + token}
        user_response = requests.get(
            'http://127.0.0.1:5000/api/user',
            headers=headers
        )
        self.assert403(user_response)

    def test_expired_token(self):
        token = ''
        headers = {'Authorization': 'Bearer ' + token}
        user_response = requests.get(
            'http://127.0.0.1:5000/api/user',
            headers=headers
        )
        self.assert403(user_response)


if __name__ == '__main__':
    unittest.main()
