# broker subscriber
import paho.mqtt.client as mqtt
from src.lib.logger import info_logger
from definitions import load_config
from src.storage import InfluxStore


# parameters
broker = load_config()['mqtt_broker']['url']
port = load_config()['mqtt_broker']['port']
keep_alive = load_config()['mqtt_broker']['keep_alive']
topic = load_config()['mqtt_broker']['topic']
qos = load_config()['mqtt_broker']['qos']
username = load_config()['mqtt_broker']['username']
password = load_config()['mqtt_broker']['password']

influx_c = InfluxStore()


# callback functions for subscriber
def on_connect(mqtt_client, userdata, flags, rc):

    returnCode = {
        0: "Connection successful",
        1: "Connection refused – incorrect protocol version",
        2: "Connection refused – invalid client identifier",
        3: "Connection refused – server unavailable",
        4: "Connection refused – bad username or password",
        5: "Connection refused – not authorised"
    }

    info_logger(returnCode.get(rc,"unable to identify return code error!"))

    if rc == 0:

        mqtt_client.subscribe(topic, qos)


def on_disconnect(mqtt_client, userdata, rc):

    info_logger('disconnected...rc=' + str(rc))


# on message collect payload and save to Influx DB database
def on_message(mqtt_client, userdata, msg):

    info_logger("MQTT Data Received...")
    info_logger("MQTT Topic: " + str(msg.topic))
    info_logger("Data: " + str(msg.payload))

    # post to InfluxDB Client
    influx_c.save(msg.topic,msg.payload)

    info_logger("Data saved to Influx database!")


def on_subscribe(mqtt_client, userdata, mid, granted_qos):

    info_logger('subscribed (qos=' + str(granted_qos) + ')')


def on_log(client, userdata, level, buf):

    info_logger(buf)


def connect_to_broker():

    # initiate mqtt client
    mqtt_c = mqtt.Client()

    # register event handlers
    mqtt_c.on_message = on_message
    mqtt_c.on_connect = on_connect
    mqtt_c.on_subscribe = on_subscribe
    mqtt_c.on_disconnect = on_disconnect
    mqtt_c.on_log = on_log

    # connect client with authentication
    mqtt_c.username_pw_set(username, password)
    mqtt_c.connect(broker, port, keep_alive)

    # loop forever
    mqtt_c.loop_forever()
