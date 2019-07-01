#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

echo "Installing InfluxDB"
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/lsb-release
echo "deb https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update && sudo apt-get install influxdb
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb

echo "Installing EMQ X Broker"
curl -fsSL https://repos.emqx.io/gpg.pub | sudo apt-key add -
sudo apt-key fingerprint 3E640D53
sudo add-apt-repository --yes \
    "deb [arch=amd64] https://repos.emqx.io/emqx-ce/deb/ubuntu/ \
    $(lsb_release -cs) \
    stable"
sudo apt update
sudo apt install -y emqx
echo "Starting EMQ X Broker"
sudo systemctl start emqx