"""MQTT client that subscribes to topic"""
import paho.mqtt.client as mqtt
from ..config import Config
from .subscriber import (on_connect,
                         on_message,
                         on_disconnect,
                         on_subscribe,
                         on_log)
import cloud_gateway.helpers.logger as app_logger


# load MQTT broker configurations
broker_url = Config.BROKER_URL
port = Config.BROKER_PORT
keep_alive = Config.BROKER_KEEP_ALIVE
username = Config.BROKER_USERNAME
password = Config.BROKER_PASSWORD


def connect_to_broker():
    """Connects to MQTT broker
    """
    # initiate mqtt client
    mqtt_c = mqtt.Client()

    # register event handlers
    mqtt_c.on_connect = on_connect
    mqtt_c.on_message = on_message
    mqtt_c.on_subscribe = on_subscribe
    mqtt_c.on_disconnect = on_disconnect
    mqtt_c.on_log = on_log

    # connect client with authentication
    try:
        mqtt_c.username_pw_set(username, password)
        app_logger.info("Username and password have been set.")
    except Exception as e:
        app_logger.error(str(e))
    try:
        mqtt_c.connect(broker_url, int(port), int(keep_alive))
        app_logger.info("Initiation of connection to broker.")
    except Exception as e:
        app_logger.error(str(e))

    # loop forever
    mqtt_c.loop_forever()
