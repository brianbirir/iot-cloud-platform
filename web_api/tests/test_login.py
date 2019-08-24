import unittest
import requests
from flask import Flask
from flask_testing import TestCase


class LoginTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_successful_login_request(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com", "password": "1234567891"}
        )

        self.assert200(r)

    def test_wrong_credentials_login_request(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com", "password": "1234567"}
        )
        self.assert403(r)

    def test_non_existent_user_login_request(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test_another@gmail.com", "password": "1234567891"}
        )
        self.assert404(r)

    def test_successful_login_response(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com", "password": "1234567891"}
        )
        response = r.json()
        self.assertIsInstance(response['user_id'], int)
        self.assertIsInstance(response['message'], str)
        self.assertIsInstance(response['auth_token'], str)

    def test_successful_login_response_headers(self):
        r = requests.post(
            'http://127.0.0.1:5000/api/login',
            data={"email": "test@gmail.com", "password": "1234567891"}
        )
        response_headers = r.headers
        self.assertEqual(response_headers['Content-Type'], 'application/json', msg="Not a JSON content type")
 
    
if __name__ == '__main__':
    unittest.main()
