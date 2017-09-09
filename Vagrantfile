Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network", ip: "192.168.1.99"
  config.vm.hostname = "newkids.block"
  config.vm.synced_folder ".", "/vagrant", type: "nfs"
  config.vm.provision "shell", inline: <<-SHELL
      sudo apt-get update
      sudo apt-get install -y python-dev
      sudo apt-get install -y python-pip
      sudo apt-get install -y openssl
      sudo apt-get install -y libssl-dev
      sudo apt-get install geth
      sudo pip install --upgrade git+https://github.com/bar9/browsepy.git
      sudo pip install --upgrade pip
      sudo pip install --upgrade browsepy
      sudo pip install --upgrade pyopenssl
      sudo pip install --upgrade requests[security]
      sudo pip install --upgrade eth-testrpc
      sudo pip install --upgrade web3

      browsepy 0.0.0.0 80 --directory /vagrant/demo_data
      #browsepy 0.0.0.0 80 --directory /vagrant/demo_data --plugin=blockchain_verification
SHELL
end