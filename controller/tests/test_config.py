import os
import unittest

from config import Config


class ConfigTest(unittest.TestCase):

    c = Config()

    def test_env_path(self):
        self.assertTrue(os.path.exists(self.c.env_file))

    def test_env_variables(self):
        self.assertEquals(self.c.BROKER_PORT, "1883")


if __name__ == "__main__":
    unittest.main()
