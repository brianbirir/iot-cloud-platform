import helpers.logger as app_logger
from config import Config
from db import Database
from helpers.parser import convert_from_byte_literal

# load MQTT broker configurations
topic = Config.BROKER_TOPIC
qos = Config.BROKER_QOS


# callback functions for subscriber
def on_connect(mqtt_client, userdata, flags, rc):
    return_code = {
        0: "Connection successful",
        1: "Connection refused – incorrect protocol version",
        2: "Connection refused – invalid client identifier",
        3: "Connection refused – server unavailable",
        4: "Connection refused – bad username or password",
        5: "Connection refused – not authorised"
    }
    if rc == 0:
        app_logger.info("Broker connection was successful")
        mqtt_client.subscribe(topic, int(qos))
    else:
        app_logger.error(return_code.get(rc, "Unable to identify return code error!"))


def on_disconnect(mqtt_client, userdata, rc):
    app_logger.info('disconnected...rc=' + str(rc))


def on_message(mqtt_client, userdata, msg):
    app_logger.info("MQTT Data Received...")
    app_logger.info("MQTT Topic: " + str(msg.topic))
    app_logger.info("Data: " + str(msg.payload))
    database_instance = Database(sensor_topic=msg.topic,
                                 sensor_data=convert_from_byte_literal(msg.payload))
    database_instance.save()
    app_logger.info("Data saved to Influx database!")


def on_subscribe(mqtt_client, userdata, mid, granted_qos):
    app_logger.info('subscribed (qos=' + str(granted_qos) + ')')


def on_log(client, userdata, level, buf):
    app_logger.info(buf)
