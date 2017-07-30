# this module pushes data to mysql database
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='toor',
                             db='sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def sensor_handler(sensor_topic,sensor_data):
    # parse the json data
    json_Dict = json.loads(sensor_data)

    try:
        with connection.cursor() as cursor:
            # create a new record
            sql = "INSERT INTO 'sensor' ('device_id', 'sensor_data') VALUES (%s, %s)"
            cursor.execute(sql, (sensor_topic, sensor_data))
        # save changes to database
        connection.commit()
    except:
        print "Unable to save data"
    finally:
        connection.close()
