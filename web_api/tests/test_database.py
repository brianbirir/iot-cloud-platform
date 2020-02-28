import unittest
import psycopg2
from config import DatabaseInitializationConfig


class TestDatabase(unittest.TestCase):
    """Test database connection and configurations"""

    db_config = DatabaseInitializationConfig()

    def test_connection(self):
        """Tests connection to database"""
        conn = psycopg2.connect(dbname=self.db_config.POSTGRES_DATABASE_NAME,
                                user=self.db_config.POSTGRES_DATABASE_USER,
                                password=self.db_config.POSTGRES_DATABASE_PASSWORD,
                                host=self.db_config.POSTGRES_DATABASE_HOST,
                                port=self.db_config.POSTGRES_DATABASE_PORT)
        self.assertIsInstance()
