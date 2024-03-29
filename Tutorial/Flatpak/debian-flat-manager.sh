#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-04-06-Thursday.
# Description: This shell script is to set flat-manager for flatpak repository.
# Command: "sh debian-flat-manager.sh" with user authority.

echo -e "\e[0;34m========== SETTING FLAT-MANAGER ON DEBIAN 11 ==========\e[0m"

# VARIABLES
echo -e "\e[0;32m---------- variables ----------\e[0m"
echo $HOME

# INSTALLING "RUST"
echo -e "\e[0;32m---------- rust ----------"
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"

# INSTALLING PACKAGES
echo -e "\e[0;32m---------- packages ----------\e[0m"
sudo apt install -y git python3-aiohttp python3-pip autoconf gtk-doc-tools libglib2.0-dev libgpgme-dev libtool bison liblzma-dev e2fslibs-dev libcurl4-openssl-dev libsoup2.4-dev libfuse-dev
pip3 install tenacity

# INSTALLING OSTREE
echo -e "\e[0;32m---------- ostree ----------\e[0m"
cd $HOME
git clone https://github.com/flatpak/ppa-ostree.git
cd ppa-ostree
git submodule update --init
env NOCONFIGURE=1 ./autogen.sh
./configure --prefix=/usr --with-dracut --with-curl --with-builtin-grub2-mkconfig
make -j
sudo make install -j

# INSTALLING FLATPAK
echo -e "\e[0;32m---------- flatpak ----------\e[0m"
sudo apt install -y flatpak flatpak-builder gnome-software-plugin-flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
sudo flatpak install -y flathub org.freedesktop.Platform//22.08 org.freedesktop.Sdk//22.08

# CLONING A GIT REPOSITORY "FLAT-MANAGER"
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
sudo apt install -y postgresql postgresql-contrib
sudo systemctl enable postgresql
# CREATE "REPO" DATABASE WITH CURRENT USER
# Note: There might be changing errors errors, 
# but the createuser and createdb commands are executed.
sudo -u postgres createuser $(whoami)
sudo -u postgres createdb --owner=$(whoami) repo
sudo systemctl start postgresql

# BUILDING REPOSITORY
echo -e "\e[0;32m---------- repository ----------\e[0m"
ostree --repo=repo init --mode=archive-z2
ostree --repo=beta-repo init --mode=archive-z2
mkdir build-repo

# ISSUING TOKEN FOR REPOSITORY 
export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name testtoken)

# RUN THE REPOSITORY (TODO) IN NEW TMUX WINDOW
# tmux new && cd $HOME/flat-manager && cargo run --bin flat-manager
echo -e "\e[0;33m run the below command in another window: \e[0m"
echo -e "\e[0;33m cd $HOME/flat-manager && cargo run --bin flat-manager \e[0m"

# ENABLE THE PORT
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
# sudo setenforce 0

# INSTALL NGROK FOR TUNNELING
echo -e "\e[0;32m---------- tunneling ----------\e[0m"
cd $HOME
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
cd /usr/local/bin
sudo chmod 755 ngrok
# ngrok config add-authtoken {NGROK_TOKEN}

# START NGROK IN A TMUX SESSION (TODO) IN NEW TMUX WINDOW
# tmux new && ngrok http 8080
echo -e "\e[0;33m run the below command in another window with ngrok token if you have: \e[0m"
echo -e "\e[0;33m ngrok config add-authtoken {NGROK_TOKEN} \e[0m"
echo -e "\e[0;33m ngrok http 8080 \e[0m"

echo -e "\e[0;34m========== FINISHED ==========\e[0m"
