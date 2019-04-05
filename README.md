# IOT Subscriber

Implementation of an MQTT subscriber client to receive data from a sensor gateway that publishes the data from sensors. The receives message is parsed and stored in an instance of InfluxDB, a time series database.

## What to setup?

- Python 3.6
- Python libraries:
    - `paho-mqtt` client
    - `pymysql` - MySQL Python client library
    - InfluxDB Python client library
- MQTT - Mosquitto MQTT Broker
- InfluxDB time series database [https://portal.influxdata.com/downloads/](https://portal.influxdata.com/downloads/)

## System Architecture
![System Architexture](design.png)