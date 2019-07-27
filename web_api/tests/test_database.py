import unittest
import psycopg2
from config import DatabaseInitializationConfig


db_config = DatabaseInitializationConfig()


class TestDatabase(unittest.TestCase):
    def test_connection(self):
        conn = psycopg2.connect(dbname=db_config.POSTGRES_DATABASE_NAME,
                                user=db_config.POSTGRES_DATABASE_USER,
                                password=db_config.POSTGRES_DATABASE_PASSWORD,
                                host=db_config.POSTGRES_DATABASE_HOST,
                                port=db_config.POSTGRES_DATABASE_PORT)
        self.assertIsInstance()
