import unittest
from db import Database


class DatabaseTest(unittest.TestCase):
    def test_db_connection(self):
        d = Database()
        self.assertTrue(d.check_db())

    def test_sensor_data_compilation(self):
        d = Database(sensor_topic="test/dht11",
                     sensor_data="{\"temp\": 23.3, \"humidity\": 30.3}")

        compiled_data = d.compile_sensor_data()
        print(compiled_data)
        self.assertIsInstance(compiled_data, list)
