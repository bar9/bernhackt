Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.1.99"
  config.vm.hostname = "newkids.block"
  config.vm.synced_folder ".", "/vagrant", type: "nfs"
  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python-dev
      sudo apt-get install -y python-pip
      sudo pip3 install --upgrade pip
      pip install git+https://github.com/bar9/browsepy.git
      browsepy 0.0.0.0 80 --directory /vagrant/demo_data
      #browsepy 0.0.0.0 80 --directory /vagrant/demo_data --plugin=blockchain_verification
SHELL
end