# broker class

import paho.mqtt.client as mqtt
import utils.logger as logger
from definitions import load_config
from src.influxmodel import Influxmodel

class Broker:

    def __init__(self):
        self._broker = load_config()['mqtt_broker']['url']
        self._port = load_config()['mqtt_broker']['port']
        self._keep_alive = load_config()['mqtt_broker']['keep_alive']
        self._topic = load_config()['mqtt_broker']['topic']
        self._qos = load_config()['mqtt_broker']['qos']
        self._username = load_config()['mqtt_broker']['username']
        self._password = load_config()['mqtt_broker']['password']

        self._influxclient = Influxmodel()

    # callback functions for subscriber
    def on_connect(self,mqtt_client, userdata, rc):

        logger.info_logger('connected...rc=' + str(rc))
        mqtt_client.subscribe(self._topic, self._qos)

    def on_disconnect(self,mqtt_client, userdata, rc):

        logger.info_logger('disconnected...rc=' + str(rc))

    # on message collect payload and save to Influx DB database
    def on_message(self,mqtt_client, userdata, msg):

        logger.info_logger("MQTT Data Received...")
        logger.info_logger("MQTT Topic: " + str(msg.topic))
        logger.info_logger("Data: " + str(msg.payload))

        # post to InfluxDB Client
        self._influxclient.save(msg.topic,msg.payload)
        logger.info_logger("Data saved to Influx database!")

    def on_subscribe(self,mqtt_client, userdata, mid, granted_qos):

        logger.info_logger('subscribed (qos=' + str(granted_qos) + ')')

    def on_log(self,client, userdata, level, buf):
        logger.info_logger(buf)

    def connect_to_broker(self):
        # initiate mqtt client
        mqtt_c = mqtt.Client()

        # register event handlers
        mqtt_c.on_message = self.on_message
        mqtt_c.on_connect = self.on_connect
        mqtt_c.on_subscribe = self.on_subscribe
        mqtt_c.on_disconnect = self.on_disconnect
        mqtt_c.on_log = self.on_log

        # connect client with authentication
        mqtt_c.username_pw_set(self._username, self._password)
        mqtt_c.connect(self._broker, self._port, self._keep_alive)

        # loop forever
        mqtt_c.loop_forever()