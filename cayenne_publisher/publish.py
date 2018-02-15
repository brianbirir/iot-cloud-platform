from __future__ import print_function
import paho.mqtt.publish as publish
import time
import json
import os

# get config current file path
config_file_path = os.path.dirname(os.path.abspath(__file__))

print(config_file_path)

# get Temperature and Humidity values
# cTemp = sensor.getTemperature()['cTemp']
# cHumidity = sensor.getHumdity()


# get configuration
def get_configs():
    with open(config_file_path + '/' +'config.json') as json_data_file:
        config = json.load(json_data_file)
    return config


def publish(data):
    # connection_configuration
    general_conf = get_configs()['general']

    # get thingspeak configuration
    cayenne_conf = get_configs()['env']['cayenne']

    # payload string
    # cayenne_payload = 'field1=' + str(cTemp) + '&field2=' + str(cHumidity)

    '''
    
    cayenne server topic format: 
    
    /v1/username/things/clientID/data/channel
    
    '''
    cayenne_topic = 'v1/'+ cayenne_conf['username'] + '/things/' + cayenne_conf['client_id'] + '/data/' + cayenne_conf['channel']

    # print temperature and humidity output
    print (" Temperature =",str(cTemp),"   Humidity =",str(cHumidity))

    # attempt to publish this data to the topic 
    try:
        print ("Publishing data")
        publish.single(thingspeak_topic, cayenne_payload, cayenne_conf['qos'], retain=False, hostname=cayenne_conf['broker_address'], port=general_conf['broker_port'], keepalive=general_conf['broker_keep_alive'])
        time.sleep(3)

    except KeyboardInterrupt:
        print ("Keyboard interrupt")

    except:
        print ("There was an error while publishing the data.")