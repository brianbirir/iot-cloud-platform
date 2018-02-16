# This echoes the data received by the Ruleblox MQTT server to Cayenne server in mydevices.com

import paho.mqtt.client as mqtt
import time
# import sensor
import dummy
import json

# create instance of the client class
client_sensor = mqtt.Client()


# get configuration
def get_configs():
    with open("./config.json") as config_file:
        config = json.load(config_file)
    return config


# get temperature and humidity values
cTemp = dummy.dummy_temp()
cHumidity = dummy.dummy_humidity()

# connection_configuration
general_conf = get_configs()['general']

# get thingspeak configuration
cayenne_conf = get_configs()['env']['cayenne']

'''
cayenne server topic format: 
    
v1/username/things/clientID/data/channel
'''
cayenne_topic = 'v1/'+ cayenne_conf['username'] + '/things/' + cayenne_conf['client_id'] + '/data/'


# subscribe to topic
def subscribe_to_topic(topic,qos):
    client_sensor.subscribe(topic, qos)
    print ("Subscribed to MQTT topic: " + str(topic))
    print ""

# publish to topic
def publish_to_topic(topic, msg, qos):
    client_sensor.publish(topic, msg, qos, False)
    print ("Published: " + str(msg) + " " + "on MQTT Topic: " + str(topic))
    print ""


# collect payload data as JSON and publish
def pub_payload(payload):

    parsed_payload = json.loads(payload)

    '''
    cayenne payload should be in the form of:

    type,unit=value

    '''

    for key, value in parsed_payload.iteritems():
        if key == 'rel_hum':
            hum_payload = key + ',p=' + str(value)
            publish_to_topic(cayenne_topic+"4", hum_payload, cayenne_conf['qos'])

        if key == 'temp':
            temp_payload = key + ',t=' + str(value)
            publish_to_topic(cayenne_topic+"5", temp_payload, cayenne_conf['qos'])



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=",rc)
        #Flag to indicate success
        client_sensor.connected_flag=True
    elif rc == 5:
        print("User authentication connection error =",rc)
        client_sensor.bad_connection_flag=True
    else:
        print("Bad connection Returned code=",rc)
        client_sensor.bad_connection_flag=True


# Callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("message received  "  ,str(msg.payload.decode("utf-8")))


# Callback for on_disconnect
def on_disconnect():
    m = "Disconnected flags"+"result code "+str(rc)+"client_id  "
    print m
    client_sensor.connected_flag = False


# Callback for Logging
def on_log(client, userdata, level, buf):
    print("log: ",buf)


# connect to broker and send data
def connect_broker(payload):

    # flags
    mqtt.Client.connected_flag = False
    mqtt.Client.bad_connection_flag = False
    mqtt.Client.retry_count = 0

    # assign callback functions to client
    client_sensor.on_connect = on_connect
    client_sensor.on_message = on_message
    client_sensor.on_log = on_log

    run_main = False
    run_flag = True

    while run_flag:
        # establish connection
        while not client_sensor.connected_flag and client_sensor.retry_count < 3:
            count = 0
            run_main = False
            try:
                print("connecting ", cayenne_conf['broker_address'])

                # set username and password to connecto to MQTT broker
                client_sensor.username_pw_set(cayenne_conf['username'], cayenne_conf['password'])

                # CONNECT
                client_sensor.connect(cayenne_conf['broker_address'], general_conf['broker_port'], general_conf['broker_keep_alive'])
                break # break from while loop
            
            except:
                print "connection attempt failed will retry"
                client_sensor.retry_count += 1
                if client_sensor.retry_count > 3:
                    run_flag = False
        # run loop
        if not run_main:
            client_sensor.loop_start()
            while True:
                if client_sensor.connected_flag: # wait for connack
                    client_sensor.retry_count = 0 # reset counter
                    run_main = True
                    break
                if count > 6 or client_sensor.bad_connection_flag: # don't wait forever
                    client_sensor.loop_stop() # stop loop
                    client_sensor.retry_count += 1
                    if client_sensor.retry_count > 3:
                        run_flag = False
                    break # break from while loop

                time.sleep(1)
                count += 1

        if run_main:
            try:
                # Do main loop
                print "in main loop" # publish and subscribe here
                pub_payload(payload)
                time.sleep(10)
            # Added try block to catch keyboard interrupt  to break loop so we
            # don't leave loop thread running.

            except KeyboardInterrupt:
                print "Keyboard Interrupt so ending"
                run_flag = False

    # disconnect & end loop
    client_sensor.disconnect()
    client_sensor.loop_stop()
