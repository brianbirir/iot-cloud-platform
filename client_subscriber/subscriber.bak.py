# this module subscribes to topic payloads sent by gateway MQTT client publisher

import paho.mqtt.client as mqtt
from influx_db import sensor_handler
#from mysql_db import sensor_handler

# MQTT Settings
MQTT_Broker = 'localhost'
MQTT_Port = '1883'
Keep_Alive_Interval = 60
MQTT_Topic = 'PyBlox/#'
MQTT_qos = 0
MQTT_username = 'ruleblox'
MQTT_password = 'ruleblox@2017#!'


# callback functions for subscriber
def on_connect(mqtt_client, userdata, rc):
    print('connected...rc=' + str(rc))
    mqtt_client.subscribe(MQTT_Topic, MQTT_qos)


def on_disconnect(mqtt_client, userdata, rc):
    print('disconnected...rc=' + str(rc))


# on message collect payload and save to Influx DB database
def on_message(mqtt_client, userdata, msg):
    print "MQTT Data Received..."
    print "MQTT Topic: " + str(msg.topic)
    print "Data: " + str(msg.payload)
    # sensor_handler(msg.topic,msg.payload)


def on_subscribe(mqtt_client, userdata, mid, granted_qos):
    print('subscribed (qos=' + str(granted_qos) + ')')


def on_unsubscribe(mqtt_client, userdata, mid, granted_qos):
    print('unsubscribed (qos=' + str(granted_qos) + ')')


def on_log(client, userdata, level, buf):
    print("log: ",buf)


def connect_to_broker():
    # connect to broker and loop forever

    # create client instance
    mqtt_client = mqtt.Client(clean_session=True)
    # assign callbacks

    mqtt_client.on_connect = on_connect
    # mqtt_client.on_disconnect = on_disconnect
    mqtt_client.on_message = on_message
    # mqtt_client.on_subscribe = on_subscribe
    # mqtt_client.on_unsubscribe = on_unsubscribe
    mqtt_client._on_log = on_log

    # set username and password to connect to MQTT broker
    mqtt_client.username_pw_set(MQTT_username, MQTT_password)
    mqtt_client.connect(MQTT_Broker, MQTT_Port)
    #mqtt_client.on_message = on_message
    mqtt_client.loop_forever()
