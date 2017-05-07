# this module subscribes to topic payloads sent by gateway publisher

import paho.mqtt.client as mqtt
import

# callback functions for subscriber
def on_connect(mqttc, userdata, rc):
    print('connected...rc=' + str(rc))
    mqttc.subscribe(topic='device/#', qos=0)

def on_disconnect(mqttc, userdata, rc):
    print('disconnected...rc=' + str(rc))

def on_message(mqttc, userdata, msg):
    print('message received...')
    print('topic: ' + msg.topic + ', qos: ' + 
          str(msg.qos) + ', message: ' + str(msg.payload))
    save_to_db(msg)

def on_subscribe(mqttc, userdata, mid, granted_qos):
    print('subscribed (qos=' + str(granted_qos) + ')')

def on_unsubscribe(mqttc, userdata, mid, granted_qos):
    print('unsubscribed (qos=' + str(granted_qos) + ')')


# create client instance
mqtt_client = mqtt.Client()

# assign callbacks
mqtt_client.on_connect = on_connect
mqtt_client.on_disconnect = on_disconnect
mqtt_client.on_message = on_message
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_unsubscribe = on_unsubscribe

# connect and loop forever
mqttc.connect(host='localhost', port=1883)
mqttc.loop_forever()