import os
import unittest

from config import Config


class ConfigTest(unittest.TestCase):
    """Testing of application configurations"""

    c = Config()

    def test_app_env_variables(self):
        """Test if env variables are loaded"""
        self.assertEqual(self.c.SQLALCHEMY_TRACK_MODIFICATIONS, "False")


if __name__ == "__main__":
    unittest.main()
