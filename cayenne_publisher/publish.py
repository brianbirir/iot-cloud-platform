from __future__ import print_function
import paho.mqtt.publish as publish
import time
import json
import cayenne.client


# get configuration
def get_configs():
    with open("./config.json") as config_file:
        config = json.load(config_file)
    return config


# connection_configuration
general_conf = get_configs()['general']

# get cayenne configuration
cayenne_conf = get_configs()['env']['cayenne_test']

'''
cayenne server topic format: 

v1/username/things/clientID/data/channel
'''

cayenne_topic = 'v1/' + cayenne_conf['username'] + '/things/' + cayenne_conf['client_id'] + '/data/'

print(cayenne_topic)

client = cayenne.client.CayenneMQTTClient()

def on_message(message):
  print("message received: " + str(message))
  # If there is an error processing the message return an error string, otherwise return nothing.


def publish_cayenne(payload):

    client.on_message = on_message
    client.begin(cayenne_conf['username'], cayenne_conf['password'], cayenne_conf['client_id'])

    # attempt to publish this data to the topic 
    try:
        print("Publishing data to Cayenne")
        parsed_payload = json.loads(payload)

        '''
        cayenne payload should be in the form of:

        type,unit=value

        '''

        # mqtt_auth = {'username':cayenne_conf['username'], 'password':cayenne_conf['password']}

        for key, value in parsed_payload['Data'].iteritems():
            if key == 'rel_hum':
                print("Publishing Temperature")
                hum_payload = key + ',p=' + str(value)
                hum_topic = cayenne_topic + "1"
                #publish.single(hum_topic, payload=hum_payload, qos=cayenne_conf['qos'], retain=False, hostname=cayenne_conf['broker_address'], port=general_conf['broker_port'], client_id="", keepalive=general_conf['broker_keep_alive'], auth=mqtt_auth)
                client.mqttPublish(hum_topic, hum_payload)
                print("Published Temperature")

            if key == 'temp':
                print("Publishing Humidity")
                temp_payload = key + ',t=' + str(value)
                temp_topic = cayenne_topic + "2"
                #publish.single(temp_topic, payload=temp_payload, qos=cayenne_conf['qos'], retain=False, hostname=cayenne_conf['broker_address'], port=general_conf['broker_port'], client_id="",keepalive=general_conf['broker_keep_alive'], auth=mqtt_auth)
                client.mqttPublish(temp_topic, temp_payload)
                print("Published Humidity")

        print("Publishing completed")

    except KeyboardInterrupt:
        print("Keyboard interrupt")

    except:
        print("There was an error while publishing the data.")