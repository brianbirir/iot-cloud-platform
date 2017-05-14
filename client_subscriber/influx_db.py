# this module pushes data from the subscriber to Influx DB

from influxdb import InfluxDBClient
import json

# using HTTP to connect to InfluxDB database
db_name = 'ruleblox_production'
db_host = '138.197.6.61'
db_port = 8086
db_user = 'admin'
db_password = 'ruleblox@2017#!'

# instantiate influx db client
client_db = InfluxDBClient(db_host, db_port, db_user, db_password)

# check if DB exists, if not create it
def check_DB():
    # get all databases
    all_dbs_list = client_db.get_list_database()

    # check if current database exists and if not create it
    if db_name not in [str(x['name']) for x in all_dbs_list]:
        print "Creating db {0}".format(db_name)
        client_db.create_database(db_name)
    else:
        print "Reusing db {0}".format(db_name)

    client_db.switch_database(db_name)

# store sensor data
def sensor_data_handler(sensorData):
    # parse the json data
    json_Dict = json.loads(sensorData)
    SensorID = json_Dict['Sensor_ID']
    Temperature = json_Dict['Temperature']
    Humidity = json_Dict['Humidity']

    # json data
    json_body = [
        {
            "measurement": "room",
            "tags": {
                "device_id": SensorID,
            },
            "fields": {
                "temperture": Temperature,
                "humidity": Humidity
            }
        }
    ]

    # check database existence
    check_DB()

    # write points
    client_db.write_points(json_body)


# function to collect data from subscriber
def sensor_handler(topic, jsonSensorData):

    if topic == 'Room/Si7021':
        sensor_data_handler(jsonSensorData)
    else:
        print "No topic to subscribe to!"
