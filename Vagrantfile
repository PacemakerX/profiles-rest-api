# -*- mode: ruby -*-
# vi: set ft=ruby :

# This file is a Vagrantfile, which is used to configure a virtual machine (VM) using Vagrant.
# The "2" in Vagrant.configure specifies the configuration version. 
# Do not change it unless you know what you're doing.

Vagrant.configure("2") do |config|
  # Specify the base box for the VM. A "box" is a pre-configured VM image.
  # Here, we are using an Ubuntu 18.04 (Bionic Beaver) box.
  config.vm.box = "ubuntu/bionic64"

  # Specify the version of the box to use. The "~>" means "compatible with this version."
  config.vm.box_version = "~> 20200304.0.0"

  # Forward port 8000 from the guest (VM) to the host (your local machine).
  # This allows you to access services running on port 8000 in the VM from your local machine.
  config.vm.network "forwarded_port", guest: 8000, host: 8000

  # Provisioning is the process of setting up the VM after it is created.
  # Here, we use a shell script to configure the VM.
  config.vm.provision "shell", inline: <<-SHELL
    # Disable automatic updates to avoid conflicts during provisioning.
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer

    # Update the package list to ensure we have the latest information about available packages.
    sudo apt-get update

    # Install Python 3 virtual environment tools and the zip utility.
    sudo apt-get install -y python3-venv zip

    # Create a .bash_aliases file in the vagrant user's home directory if it doesn't exist.
    touch /home/vagrant/.bash_aliases

    # Add an alias for Python to point to Python 3, but only if it hasn't been added already.
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      # Add a marker to indicate the alias has been added.
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases

      # Add the alias to make the 'python' command point to 'python3'.
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end