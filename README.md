# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* MQTT Broker/Server - Mosquitto
* Version

### How do I get set up? ###
* Install Mosquitto on Ubuntu Server
```
sudo apt-get install mosquitto mosquitto-clients
```
* Run ` sudo netstat -ntulp` to confirm that Mosquitto is running. It should be running on port `1883`. Or run the following test:

* Log in to your server a second time, so you have two terminals side-by-side. In the new terminal, use mosquitto_sub to subscribe to the test topic:
```
    mosquitto_sub -h localhost -t test
```

* -h is used to specify the hostname of the MQTT server, and -t is the topic name. You'll see no output after hitting ENTER because mosquitto_sub is waiting for messages to arrive. Switch back to your other terminal and publish a message:

```
    mosquitto_pub -h localhost -t test -m "hello world"
```


### Contribution guidelines ###


### Change Log ###

### Author ###

* Brian Birir
