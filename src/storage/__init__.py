# this module stores data in Influx DB from the subscriber
from influxdb import InfluxDBClient
from definitions import load_config
import json
import re
from src.utils.logger import info_logger


class InfluxStore:

    def __init__(self):

        self._host = load_config()['influxdb']['host']
        self._port = load_config()['influxdb']['port']
        self._dbname = load_config()['influxdb']['db_name']
        self._password = load_config()['influxdb']['password']
        self._user = load_config()['influxdb']['user']

        # instantiate influx db client
        self._client = InfluxDBClient(self._host, self._port, self._user, self._password)

    # check if database exists, if not create it
    def check_db(self):

        # get all databases
        all_dbs_list = self._client.get_list_database()

        # check if current database exists and if not create it
        if self._dbname  not in [str(x['name']) for x in all_dbs_list]:
            info_logger("Creating db {0}".format(self._dbname ))
            self._client.create_database(self._dbname)
        else:
            info_logger("Reusing db {0}".format(self._dbname))
            self._client.switch_database(self._dbname)

    # save data to influxDB
    def save(self, sensor_topic, sensor_data):

        # parse the json data
        json_sensor_data = json.loads(sensor_data)
        device_id = str(json_sensor_data['device_id'])
        mac_address = str(json_sensor_data['device_mac_address'])
        data = str(json_sensor_data['device_data'])

        json_body = [
            {
                "measurement": sensor_topic,
                "tags": {
                    "device_id": device_id,
                    "device_mac_address": re.sub('[!@#$:]', '', device_mac_address) # remove colons from MAC Address value
                },
                "fields": {
                    "feeds": data
                }
            }
        ]

        # check database existence first
        self.check_db()

        # write points to database
        info_logger("Saved to database")
        self._client.write_points(json_body, time_precision='s')
