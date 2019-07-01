import unittest
from cloud_gateway.config import Config
from pathlib import PosixPath


class ConfigTest(unittest.TestCase):

    c = Config()

    def test_env_path(self):
        path = self.c.env_path
        self.assertEqual(path, PosixPath('.env'))

    def test_env_variables(self):
        c = Config()
        self.assertEqual(c.BROKER_PORT, 1883)
        pass


if __name__ == "__main__":
    unittest.main()
