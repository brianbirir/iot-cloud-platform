# this module pushes data from the subscriber to Influx DB

from influxdb import InfluxDBClient
import json
from pprint import pprint

# using HTTP to connect to InfluxDB database
db_name = 'ruleblox'
db_host = '127.0.0.1'
db_port = 8086
db_user = 'admin'
db_password = 'ruleblox@2017#!'

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


def sensor_handler(sensor_data):

    # parse the json data
    json_sensor_data = json.loads(sensor_data)

    #for key in json_sensor_data:
    SensorID = json_sensor_data['Sensor_ID']
    SensorData = json_sensor_data['Sensor_Data']

    # json data
    json_body = [
        {
            "measurement":"pyblox",
            "tags":{
                "device_id":SensorID,
            },
            "fields":{
                "sensor_data":SensorData,
            }
        }
    ]

    pprint(json.dumps(json_body))

    # check database existence
    # check_db()

    # write points
    # print("Save to database")
    # client_db.write_points(json_body)
