#!/bin/bash
export DEBIAN_FRONTEND=noninteractive
sudo apt update && sudo apt upgrade && sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

echo "Installing Docker’s official GPG key"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

echo "Setting up Docker stable repository"
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

echo "Installing Docker engine"
sudo apt-get update
sudo apt-get install -y docker-ce

echo "Restarting Docker engine"
systemctl restart docker

echo "Confirming Docker is running"
sudo docker run hello-world

echo "Installing docker-compose"
sudo curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

echo "Run container IoT cloud services"
docker-compose -f /var/www/cloud_gateway/docker/docker-compose.yml up -d