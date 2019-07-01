import unittest
from cloud_gateway.db import Database


sensor_topic = ""
sensor_data = ""
database_name = Database.cnf.INFLUX_DB


class DatabaseTest(unittest.TestCase):

    def test_db_creation(self):
        pass

    def test_existing_database(self):
        pass

    def test_save_data(self):
        pass


if __name__ == "__main__":
    unittest.main()
