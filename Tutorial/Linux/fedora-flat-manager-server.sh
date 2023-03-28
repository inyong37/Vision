#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-03-28-Tuesday.

echo -e "\e[0;34m========== SETTING FLAT-MANAGER SERVER ON FEDORA(>=37) ==========\e[0m"

# VARIABLES
echo -e "\e[0;32m---------- variables ----------\e[0m"
echo $HOME

# INSTALLING "RUST"
echo -e "\e[0;32m---------- rust ----------"
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"

# INSTALLING PACKAGES MANAGER "DNF"
echo -e "\e[0;32m---------- package manager ----------\e[0m"
sudo yum install -y dnf

# INSTALLING PACKAGES
echo -e "\e[0;32m---------- packages ----------\e[0m"
sudo dnf install -y cargo postgresql-devel ostree-devel ostree git

# CLONING A GIT REPOSITORY "FLAT MANAGER"
echo -e "\e[0;32m---------- flat-manager ----------\e[0m"
cd $HOME
git clone https://github.com/flatpak/flat-manager.git

# BUILDING "FLAT MANAGER"
cd flat-manager
cargo build

# SETUP CONFIGURATION WITH DEFAULT ENVIRONMENT
cp example.env .env
cp example-config.json config.json

# BUILDING DATABASE "POSTGRESQL"
echo -e "\e[0;32m---------- database ----------\e[0m"
sudo dnf install postgresql-server postgresql-contrib
sudo systemctl enable postgresql
sudo opostgresql-setup --initdb --unit postgresql
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
echo -e "\e[0;32m---------- tunneling ----------\e[0m"
cd $HOME
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
cd /usr/local/bin
sudo chmod 755 ngrok

# START NGROK
ngrok http 8080

echo -e "\e[0;34m========== FINISHED ==========\e[0m"
