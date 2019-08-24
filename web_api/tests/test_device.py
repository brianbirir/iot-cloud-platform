import unittest

from src import create_app


class DeviceTest(unittest.TestCase):

    def setUp(self):
        """create application and client"""
        self.app = create_app(config_object='config.TestingConfig')
        self.app_client = self.app.test_client()

    def tearDown(self):
        pass

    def test_failing_device_endpoint(self):
        """test when a single device is not found"""
        resp = self.app_client.get('api/device')
        self.assertEqual(404, resp.status_code)

    def test_get_single_device(self):
        device_id = 1
        resp = self.app_client.get('api/device?device_id={}'.format(device_id=device_id))
        self.assertEqual(200, resp.status_code)

    def test_register_device(self):
        self.app_client.post()
        pass

    def test_update_device(self):
        pass

    def test_delete_device(self):
        pass
