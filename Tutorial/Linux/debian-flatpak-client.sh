#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-03-28-Tuesday.

echo "========== SETTING FLATPAK CLIENT ON DEBIAN =========="

# VARIABLES
echo "CHECKING VARIABLES"
echo $HOME

# INSTALLING "RUST"
curl https://sh.rustup.rs -sSf | sh -s -- -y

# INSTALLING PACKAGES MANAGER "DNF"
sudo yum install -y dnf

# INSTALLING PACKAGES
sudo dnf install -y cargo postgresql-devel ostree-devel ostree git

# CLONING A GIT REPOSITORY
cd $HOME
git clone https://github.com/flatpak/flat-manager.git

# BUILDING "FLAT MANAGER"
cd flat-manager
cargo build

# SETUP CONFIGURATION WITH DEFAULT ENVIRONMENT
cp example.env .env
cp example-config.json config.json

# BUILDING DATABASE "POSTGRESQL"
sudo dnf install -y postgresql-server postgresql-contrib
sudo systemctl enable postgresql
sudo postgresql-setup --initdb --unit postgresql
sudo systemctl start postgresql

# CREATE "REPO" DATABASE WITH CURRENT USER
sudo -u postgres createuser $(whoami)
sudo -u postgres createdb --owner=$(whoami) repo

# BUILDING REPOSITORY
ostree --repo=repo init --mode=archive-z2
ostree --repo=beta-repo init --mode=archive-z2
mkdir build-repo

# ENABLE THE PORT
iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo setenforce 0

# INSTALL NGROK FOR TUNNELING
cd $HOME
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
cd /usr/local/bin
sudo chmod 755 ngrok

# START NGROK
ngrok http 8080

echo "========== FINISHED =========="
