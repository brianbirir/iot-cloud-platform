## What is this repository for? ###

Implementation of an MQTT broker and MQTT subscriber to receive data from a sensor gateway that publishes the data.

## How do I get set up? ###

### Quick Install
* Download this repo via `git clone` to your current folder
* Run installer.sh i.e. `./installer.sh`. This will install MQTT broker, InfluxDB and configure bith services. It will also install and configure the subscriber as a service to run on an Ubuntu VM.

### Manual Install
#### Mosquitto
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
* Setup password by editing /etc/mosquitto/passwd. Add username and password to the file

* Encrypt password file i.e. `mosquitto_passwd -U passwd`


mosquitto_passwd -U passwordfile
#### InfluxDB

## Change Log ###

## Author ###

* Brian Birir
