Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.provision "shell", path: "provision.sh"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.network :forwarded_port, guest: 3881, host: 3881, id: "mqtt"
  config.vm.network :forwarded_port, guest: 5000, host: 5000, id: "flask"
  config.vm.network :forwarded_port, guest: 8086, host: 8086, id: "influxdb"
  config.vm.network :forwarded_port, guest: 18083, host: 18083, id: "EMQXdashboard"
  config.vm.synced_folder ".", "/var/www/cloud_gateway", owner: "vagrant", group: "www-data"
  config.vm.network "private_network", type: "dhcp"
end
