# this module pushes data from the subscriber to Influx DB

from influxdb import InfluxDBClient

# using Http to connect to InfluxDB database
db_name = 'ruleblox'
client_db = InfluxDBClient(host='127.0.0.1', port=8086, database=db_name)
#client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')

# get all databases
all_dbs_list = client_db.get_database_list()

# check if current database exists and if not create it
if db_name not in [str(x['name']) for x in all_dbs_list]:
    print "Creating db {0}".format(db_name)
    client_db.create_database(db_name)
else:
    print "Reusing db {0}".format(db_name)
client_db.switch_db(db_name)