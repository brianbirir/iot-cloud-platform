import os
import unittest

from config import Config


class ConfigTest(unittest.TestCase):

    c = Config()

    def test_env_path(self):
        """Test if file exists"""
        self.assertTrue(os.path.exists(self.c.env_file))

    def test_env_variables(self):
        """Test if env variables are loaded"""
        self.assertEqual(self.c.SQLALCHEMY_TRACK_MODIFICATIONS, "False")


if __name__ == "__main__":
    unittest.main()
