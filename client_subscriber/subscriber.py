# this module subscribes to topic payloads sent by gateway MQTT client publisher
import paho.mqtt.client as mqtt
from influx_db import sensor_handler
from cayenne_publisher.publish import publish_cayenne

# MQTT Settings
MQTT_Broker = 'localhost'
MQTT_Port = 1883
MQTT_Keep_Alive = 60
MQTT_Topic = 'pyblox/#'
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

    # post to InfluxDB Client
    sensor_handler(msg.topic,msg.payload)

    # send data to cayenne server
    publish_cayenne(msg.payload)


def on_subscribe(mqtt_client, userdata, mid, granted_qos):
    print('subscribed (qos=' + str(granted_qos) + ')')


def on_log(client, userdata, level, buf):
    print("log: ",buf)


def connect_to_broker():
    # initiate mqtt client
    mqtt_c  = mqtt.Client()

    # register event handlers
    mqtt_c.on_message = on_message
    mqtt_c.on_connect = on_connect
    mqtt_c.on_subscribe = on_subscribe
    mqtt_c.on_log = on_log

    # connect client with authentication
    mqtt_c.username_pw_set(MQTT_username, MQTT_password)
    mqtt_c.connect(MQTT_Broker, MQTT_Port, MQTT_Keep_Alive)

    # loop forever
    mqtt_c.loop_forever()
