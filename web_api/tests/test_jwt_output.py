import datetime
from src.utils.security.jwt_security import encode_jwt, decode_jwt

expiry_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

# subject id
subject_id = 1
algo = 'HS256'


class JwtTest:

    @staticmethod
    def test_jwt_encode():
        auth_token = encode_jwt(alg=algo, subject_id=subject_id)
        print(auth_token)

    @staticmethod
    def test_jwt_decode():
        auth_token = encode_jwt(subject_id)
        payload_result = decode_jwt(auth_token)
        print(payload_result)
        pass


if __name__ == '__main__':
    JwtTest.test_jwt_encode()
    JwtTest.test_jwt_decode()
