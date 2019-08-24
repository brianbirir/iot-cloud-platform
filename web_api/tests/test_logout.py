import unittest
import requests
from flask import Flask
from flask_testing import TestCase


class TestLogout(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_successful_logout_request(self):
        # login user first
        login_response = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com",
                  "password": "1234567891"}
        )
        token = login_response.json()['auth_token']
        headers = {'Authorization': 'Bearer ' + token}

        # finally logout user
        logout_response = requests.post(
            'http://127.0.0.1:5000/api/logout',
            headers=headers
        )
        self.assert200(logout_response)

    def test_logout_blacklisted_token_request(self):
        # include a token that has been blacklisted
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.\
        eyJzdWIiOjUsImlhdCI6MTU1NTA2MzYwMS44MDA0OCwiZXhwIjoxNTU1MTUwMDAxLjgwMDQ4fQ.\
        2R_AqhFVZfBcKwHRM7qM-6c5_jQx6WPZd8goBss6MC8'
        headers = {'Authorization': 'Bearer ' + token}

        logout_response = requests.post(
            'http://127.0.0.1:5000/api/logout',
            headers=headers
        )
        self.assert401(logout_response)


if __name__ == '__main__':
    unittest.main()
