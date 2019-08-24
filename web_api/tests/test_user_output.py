import requests


class UserTest:

    @staticmethod
    def test_get_user_details():
        # login user
        login_response = requests.post(
            'http://127.0.0.1:8000/api/login',
            data={"email": "test@gmail.com",
                  "password": "1234567891"}
        )
        token = login_response.json()['auth_token']
        headers = {'Authorization': 'Bearer ' + token}
        
        # get user details
        get_user_response = requests.get(
            'http://127.0.0.1:8000/api/user',
            headers=headers
        )
        print(get_user_response.json())

    @staticmethod
    def test_invalid_token():
            token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\
                .eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ\
                    .SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
            headers = {'Authorization': 'Bearer ' + token}
            user_response = requests.get(
                'http://127.0.0.1:8000/api/user',
                headers=headers
            )
            print(user_response.json())

    @staticmethod
    def test_expired_token():
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9\
            .eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ\
                .SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        headers = {'Authorization': 'Bearer ' + token}
        user_response = requests.get(
            'http://127.0.0.1:8000/api/user',
            headers=headers
        )
        print(user_response.json())


if __name__ == '__main__':
    UserTest.test_invalid_token()
    UserTest.test_get_user_details()
