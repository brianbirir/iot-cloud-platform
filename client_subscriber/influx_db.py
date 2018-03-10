# this module pushes data from the subscriber to Influx DB
from influxdb import InfluxDBClient
import json
from pprint import pprint
import re # for regular expressions matching


# get configuration
def get_configs():
    with open("./config.json") as config_file:
        config = json.load(config_file)
    return config

# using HTTP to connect to InfluxDB database
db_name = get_configs()['influxdb']['name']
db_host = get_configs()['influxdb']['host']
db_port = get_configs()['influxdb']['port']
db_user = get_configs()['influxdb']['user']
db_password = get_configs()['influxdb']['password']

# instantiate influx db client
client_db = InfluxDBClient(db_host, db_port, db_user, db_password)

# check if DB exists, if not create it
def check_db():
    # get all databases
    all_dbs_list = client_db.get_list_database()

    # check if current database exists and if not create it
    if db_name not in [str(x['name']) for x in all_dbs_list]:
        print "Creating db {0}".format(db_name)
        client_db.create_database(db_name)
    else:
        print "Reusing db {0}".format(db_name)

    client_db.switch_database(db_name)


def sensor_handler(sensor_topic,sensor_data):

    # parse the json data
    json_sensor_data = json.loads(sensor_data)
    SensorID = str(json_sensor_data['Gateway_ID'])
    # SensorData = json.dumps(json_sensor_data['Sensor_data'])
    SensorData = json_sensor_data['Sensor_data']

    # json data
    json_body = [
        {
            "measurement":'GatewayDemo',
            "tags":{
                "device_id":re.sub('[!@#$:]', '', SensorID),# remove colons from MAC Address value
                "node_id": SensorData['ID'],
                "sensor_topic": sensor_topic
            },
            "fields":{
                "RTC":SensorData['RTC'],
                "Leak_Sensor": SensorData['LS'],
                "Flame_Sensor": SensorData['FS'],
                "Smoke_Sensor": SensorData['SS'],
                "Water_Flow_Sensor": SensorData['FL']
            }
        }
    ]

    # pprint(json.dumps(json_body))

    # check database existence
    check_db()

    # write points
    print("Save to database")
    client_db.write_points(json_body,time_precision='s')
