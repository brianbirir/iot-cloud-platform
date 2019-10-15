"""Parse data received from sensors and return in acceptable format"""
import ast


def get_sensor_type(s_topic):
    """Returns sensor type from topic string

    Args:
        s_topic (str): string object sent by sensor as MQTT topic

    Returns:
        sensor_type (str): string object containing sensor type at index 1 of split string
    """
    sensor_type = s_topic.split("/")
    return sensor_type[1]


def convert_single_sensor_data(sensor_data, data_type="str"):
    """Converts sensor data to a specific data type

    Args:
        sensor_data (str): sensor data that comes as string by default
        data_type (str): defined data type

    Returns:
        sensor_data (int): sensor data as an integer
        sensor_data (float): sensor data as a float

    """
    if data_type == "float":
        return float(sensor_data)
    elif data_type == "int":
        return int(float(sensor_data))
    else:
        return sensor_data


def parse_multiple_sensor_data_to_dict(sensor_data):
    """Converts sensor data into valid dict
    
    Args:
        sensor_data (str): sensor data from mqtt client publisher

    Returns:
        parsed_sensor_data (dict): sensor data as valid dictionary
    """
    return ast.literal_eval(sensor_data)


def convert_from_byte_literal(sensor_data):
    """Converts from byte literal to string

    Only if parameter value is a byte
    
    Args:
        sensor_data (string or bytes): incoming sensor data
    
    Returns:
        [string]: sensor data
    """
    if isinstance(sensor_data, bytes):
        return str(sensor_data, encoding='utf-8')
    else:
        return sensor_data
