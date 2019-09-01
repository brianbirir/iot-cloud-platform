import unittest
import datetime
from src.utils.security.jwt_security import encode_jwt, decode_jwt, set_payload

# set expiry time for token to be 24 hours from time of creation
expiry_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)

# subject id
first_subject_id = 1
second_subject_id = 2


class JwtTest(unittest.TestCase):

    # check if returned token in bytes encoded
    def test_jwt_encode(self):
        auth_token = encode_jwt(first_subject_id)
        self.assertTrue(isinstance(auth_token, bytes))

    # check if decoded subject id in the payload result is the same as the actual subject id used in the initial payload
    # before token encoding
    def test_jwt_decode(self):
        auth_token = encode_jwt(second_subject_id)
        payload_result = decode_jwt(auth_token)
        self.assertEqual(payload_result, 2)

    def test_payload(self):
        payload = set_payload(first_subject_id)
        self.assertIsInstance(payload['sub'], int)
        self.assertIsInstance(payload['iat'], float)
        self.assertIsInstance(payload['exp'], float)


if __name__ == '__main__':
    unittest.main()
