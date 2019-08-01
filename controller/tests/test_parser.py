import unittest
import datetime
from helpers import parser


class ParserTest(unittest.TestCase):
    def test_sensor_type(self):
        sensor_topic = "sensor/temperature"
        sensor_type = parser.get_sensor_type(sensor_topic)
        self.assertEqual(sensor_type, "temperature")

    def test_single_sensor_data_type(self):
        sensor_data = "25.00"
        int_sensor_data_type = parser.convert_single_sensor_data(sensor_data, 
                                                                 data_type="int")
        float_sensor_data_type = parser.convert_single_sensor_data(sensor_data, 
                                                                   data_type="float")
        string_sensor_data_type = parser.convert_single_sensor_data(sensor_data)
        self.assertIsInstance(int_sensor_data_type, int)
        self.assertIsInstance(float_sensor_data_type, float)
        self.assertIsInstance(string_sensor_data_type, str)

    def test_parse_multiple_sensor_data_to_dict(self):
        timestamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        sensor_data = "{\"temp\": 23.3, \"humidity\": 30.3, \"last_valid_input\": "+"\""+timestamp+"\""+" }"
        parsed_data = parser.parse_multiple_sensor_data_to_dict(sensor_data)
        self.assertIsInstance(parsed_data, dict)


if __name__ == "__main__":
    unittest.main()
