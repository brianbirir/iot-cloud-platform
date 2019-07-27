"""Parse data received from sensors and return in acceptable format"""


def get_sensor_type(s_topic):
    """Returns sensor type from topic string

    Args:
        s_topic (str): string object sent by sensor as MQTT topic

    Returns:
        sensor_type (str): string object containing sensor type at index 1 of split string
    """
    sensor_type = s_topic.split("/")
    return sensor_type[1]


def convert_sensor_data(sensor_data, data_type="str"):
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
