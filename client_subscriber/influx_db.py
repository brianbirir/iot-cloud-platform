# this module pushes data from the subscriber to Influx DB

from influxdb import InfluxDBClient

# using Http to connect to InfluxDB database
db_name = 'ruleblox'
db_host = '138.197.6.61'
db_port = 8086
db_user = 'admin'
db_password = 'ruleblox@2017#!'

client_db = InfluxDBClient(db_host, db_port, db_user, db_password)

# get all databases
all_dbs_list = client_db.get_list_database()

# check if current database exists and if not create it
if db_name not in [str(x['name']) for x in all_dbs_list]:
    print "Creating db {0}".format(db_name)
    client_db.create_database(db_name)
else:
    print "Reusing db {0}".format(db_name)

client_db.switch_database(db_name)

# data in JSON format
json_body = [
    {
        "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
    }
]

# write points
client_db.write_points(json_body)

result = client_db.query('select value from cpu_load_short;')

print("Result: {0}".format(result))
