Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  # config.vm.network :forwarded_port, guest: 8080, host: 5000
  config.vm.network :forwarded_port, guest: 1883, host: 5555
  config.vm.network :forwarded_port, guest: 8888, host: 7000
  config.vm.synced_folder "client_subscriber/", "/var/www/mqtt_broker"
  # dhcp/ public network
  # config.vm.network "public_network"

  config.ssh.username = 'ubuntu'
  config.ssh.password = 'ubuntu'
end
