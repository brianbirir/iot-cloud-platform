import uuid
import random
import unittest

from src import create_app


class DeviceTest(unittest.TestCase):

    def setUp(self):
        """create application and client"""
        self.app = create_app(config_object='config.TestingConfig')
        self.app_client = self.app.test_client()
        self._post_test_data = {
            "device_name": "device_{random_num}".format(random_num=random.randint(1, 1000)),
            "device_uuid": "{random_uuid}".format(random_uuid=uuid.uuid4()),
            "project_id": 1
        }

    def tearDown(self):
        pass

    def test_successful_device_registration(self):
        """test successful registration of a new device"""
        resp = self.app_client.post('api/device', json=self._post_test_data)
        self.assertEqual(200, resp.status_code)

    def test_get_single_device(self):
        """test when retrieving a single device"""
        device_id = 1
        resp = self.app_client.get('api/device?device_id={device_id}'.format(device_id=device_id))
        self.assertEqual(200, resp.status_code)

    def test_get_missing_device(self):
        """test when a device is missing"""
        device_id = 10000
        resp = self.app_client.get('api/device?device_id={device_id}'.format(device_id=device_id))
        self.assertEqual(404, resp.status_code)

    def test_update_device(self):
        """test when updating a device"""
        pass

    def test_delete_device(self):
        """test when a device is deleted"""
        pass
