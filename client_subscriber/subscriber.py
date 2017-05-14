# this module subscribes to topic payloads sent by gateway MQTT client publisher

import paho.mqtt.client as mqtt
import influx_db

# MQTT Settings
MQTT_Broker = 'localhost'
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = 'Room/Si7021/#'
MQTT_qos = 0
MQTT_username = 'ruleblox'
MQTT_password = 'ruleblox@2017#!'

# callback functions for subscriber
def on_connect(mqtt_client, userdata, rc):
    print('connected...rc=' + str(rc))
    mqtt_client.subscribe(MQTT_Topic, MQTT_qos)

def on_disconnect(mqtt_client, userdata, rc):
    print('disconnected...rc=' + str(rc))

def on_message(mqtt_client, userdata, msg):
	print "MQTT Data Received..."
	print "MQTT Topic: " + str(msg.topic)
	print "Data: " + str(msg.payload)
	#sensor_Data_Handler(msg.topic, msg.payload)

def on_subscribe(mqtt_client, userdata, mid, granted_qos):
    print('subscribed (qos=' + str(granted_qos) + ')')

def on_unsubscribe(mqtt_client, userdata, mid, granted_qos):
    print('unsubscribed (qos=' + str(granted_qos) + ')')


# create client instance
mqtt_client = mqtt.Client()

# assign callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.on_message = on_message
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_unsubscribe = on_unsubscribe


def connect_to_broker():
    # connect to broker and loop forever
    # set username and password to connecto to MQTT broker
    mqtt_client.username_pw_set(MQTT_username, MQTT_password)
    mqtt_client.connect(MQTT_Broker, MQTT_Port)
    mqtt_client.loop_forever()
