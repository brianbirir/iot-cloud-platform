import json
import uuid
from helpers import logger as app_logger
from helpers import parser
from influxdb import InfluxDBClient, exceptions
from config import Config


class Database:
    """Storing of data from sensors in InfluxDB time series database
    """
    cnf = Config()
    db_client = InfluxDBClient(host=cnf.INFLUX_HOST,
                               port=cnf.INFLUX_PORT,
                               username=cnf.INFLUX_USER,
                               password=cnf.INFLUX_PASSWORD)

    def __init__(self, sensor_topic, sensor_data):
        self._sensor_topic = sensor_topic
        self._sensor_data = sensor_data

    # check if database exists, if not create it
    @staticmethod
    def check_db():
        # get all databases
        all_dbs_list = Database.db_client.get_list_database()

        # check if current database exists and if not create it
        if Database.cnf.INFLUX_DB not in [str(x['name']) for x in all_dbs_list]:
            try:
                app_logger.info("Creating db {0}".format(Database.cnf.INFLUX_DB))
                Database.db_client.create_database(Database.cnf.INFLUX_DB)
            except exceptions.InfluxDBClientError as e:
                app_logger.error(str(e))
            except exceptions.InfluxDBServerError as e1:
                app_logger.error(str(e1))
        else:
            try:
                app_logger.info("Reusing db {0}".format(Database.cnf.INFLUX_DB))
                Database.db_client.switch_database(Database.cnf.INFLUX_DB)
            except exceptions.InfluxDBClientError as e:
                app_logger.error(str(e))
            except exceptions.InfluxDBServerError as e1:
                app_logger.error(str(e1))

    def parse_json_sensor_data(self):
        """Parse JSON data from sensors gateway"""
        try:
            json_sensor_data = json.loads(self._sensor_data)
            device_id = str(json_sensor_data['gateway_id'])
            data = str(json_sensor_data['gateway_data'])
            json_body = [
                {
                    "measurement": self._sensor_topic,
                    "tags": {
                        "gateway_id": device_id
                    },
                    "fields": {
                        "feeds": data
                    }
                }
            ]
            app_logger.info("Gateway data parsed successfully.")
            return json_body
        except Exception as e:
            app_logger.error(str(e))

    def compile_sensor_data(self):
        """Compiles sensor related data into a single object

        Return:
             db_data (list): compiled sensor data object
        """
        try:
            sensor_type = parser.get_sensor_type(self._sensor_topic)
            db_data = [
                {
                    "measurement": sensor_type,
                    "tags": {
                        "id": uuid.uuid4()
                    },
                    "fields": parser.parse_multiple_sensor_data_to_dict(self._sensor_data)
                }
            ]
            app_logger.info("Sensor data compiled successfully.")
            return db_data
        except Exception as e:
            app_logger.error(str(e))

    def save(self):
        self.check_db()
        try:
            self.db_client.write_points(self.compile_sensor_data(), time_precision='s')
            app_logger.info("Save to database")
        except exceptions.InfluxDBClientError as e:
            app_logger.error(str(e))
        except exceptions.InfluxDBServerError as e1:
            app_logger.error(str(e1))
