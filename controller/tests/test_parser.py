import unittest
from helpers import parser


class ParserTest(unittest.TestCase):

    def test_sensor_type(self):
        sensor_topic = "sensor/temperature"
        sensor_type = parser.get_sensor_type(sensor_topic)
        self.assertEqual(sensor_type, "temperature")

    def test_sensor_data_type(self):
        sensor_data = "25.00"
        int_sensor_data_type = parser.convert_sensor_data(sensor_data)
        float_sensor_data_type = parser.convert_sensor_data(sensor_data, data_type="float")
        self.assertIsInstance(int_sensor_data_type, int)
        self.assertIsInstance(float_sensor_data_type, float)


if __name__ == "__main__":
    unittest.main()
