#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-03-28-Tuesday.
# Description: This shell script is to set flat-manager client for committing and pushing apps to flatpak repository.
# Command: "sh debian-flat-manager-client.sh" with user authority.

echo -e "\e[0;34m========== SETTING FLAT-MANAGER CLIENT ON DEBIAN ==========\e[0m"

# VARIABLES
echo -e "\e[0;32m---------- variables ----------\e[0m"
echo $HOME

# INSTALLING "RUST"
echo -e "\e[0;32m---------- rust ----------"
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"

# INSTALLING PACKAGES
echo -e "\e[0;32m---------- packages ----------\e[0m"
sudo apt install -y 
  flatpak flatpak-builder cargo libpq-dev postgresql postgresql-contrib pkg-config libssl-dev \
  python3-aiohttp python3-pip \
  git libcurl4-openssl-dev libsoup2.4-dev autoconf dracut libtool libglib2.0-dev \
  libgpgme-dev bison liblzma-dev e2fslibs-dev libfuse-dev libsystemd-dev tree gtk-doc-tools \
  gir1.2-ostree-1.0 libostree-dev
pip3 install tenacity pyparsing

# INSTALLING OSTREE
echo -e "\e[0;32m---------- ostree ----------\e[0m"
cd $HOME
git clone https://github.com/ostreedev/ostree.git
cd ostree
git submodule update --init
env NOCONFIGURE=1 ./autogen.sh
./configure --prefix=/usr --with-dracut --with-curl --with-builtin-grub2-mkconfig
make -j
sudo make install -j

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

# BUILDING REPOSITORY
ostree --repo=repo init --mode=archive-z2
ostree --repo=beta-repo init --mode=archive-z2
mkdir build-repo

echo -e "\e[0;34m========== FINISHED ==========\e[0m"
