#!/usr/bin/bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-04-12-Wednesday.
# Description: This shell script is to set flat-manager for flatpak repository.
# To use this script,
# 1. "apt-get update && apt-get install -y wget"
# 2. "wget https://raw.githubusercontent.com/inyong37/Vision/master/Tutorial/Flatpak/ubuntu-flat-manager.sh"
# Command: "sh ubuntu-image-container-flat-manager.sh" with root authority (in docker image/container).

echo -e "\e[0;34m========== SETTING FLAT-MANAGER ON UBUNTU 22.04 IMAGE CONTAINER ==========\e[0m"

# VARIABLES
echo -e "\e[0;32m---------- variables ----------\e[0m"
echo $HOME

# INSTALLING PACKAGES
echo -e "\e[0;32m---------- packages ----------\e[0m"
apt-get install -y curl git python3-aiohttp python3-pip autoconf gtk-doc-tools libglib2.0-dev libgpgme-dev libtool bison liblzma-dev e2fslibs-dev libcurl4-openssl-dev libsoup2.4-dev libfuse-dev libssl-dev systemd libpq-dev sudo # iptables
pip3 install tenacity

# INSTALLING "RUST"
echo -e "\e[0;32m---------- rust ----------"
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"

# INSTALLING FLATPAK AND OSTREE
echo -e "\e[0;32m---------- flatpak ----------\e[0m"
apt-get install -y flatpak flatpak-builder gnome-software-plugin-flatpak ostree libostree-dev
# (TODO) Need to install SDK for build application
# flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
# flatpak install -y flathub org.freedesktop.Platform//22.08 org.freedesktop.Sdk//22.08

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
apt-get install -y postgresql postgresql-contrib
# CREATE "REPO" DATABASE WITH CURRENT USER
# Note: There might be changing errors errors, 
# but the createuser and createdb commands are executed.
service postgresql start
sudo -u postgres createuser $(whoami)
sudo -u postgres createdb --owner=$(whoami) repo
service postgresql restart

# BUILDING REPOSITORY
echo -e "\e[0;32m---------- repository ----------\e[0m"
ostree --repo=repo init --mode=archive-z2
ostree --repo=beta-repo init --mode=archive-z2
mkdir build-repo

# ISSUING TOKEN FOR REPOSITORY 
export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name testtoken)

# RUN THE REPOSITORY (TODO) IN NEW TMUX WINDOW
cargo run --bin flat-manager

# ENABLE THE PORT - NOT WORK IN CONTAINER
# iptables -A INPUT -p tcp --dport 8080 -j ACCEPT

echo -e "\e[0;34m========== FINISHED ==========\e[0m"
