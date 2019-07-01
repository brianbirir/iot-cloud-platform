Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.network :forwarded_port, guest: 1883, host: 5555, id: "mqtt"
  config.vm.network :forwarded_port, guest: 8888, host: 7000, id: "influxdb"
  config.vm.network :forwarded_port, guest: 18083, host: 18083, id: "EMQXdashboard"
  config.vm.synced_folder ".", "/var/www/cloud_gateway"
  config.vm.network "private_network", type: "dhcp"
end
