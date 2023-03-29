#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-03-29-Wednesday.
# Description: This shell script is to set flatpak for developing applications.
# Command: "sh debian-flatpak.sh" with user authority.
# Note: User has to keep in mind to enter password for sudo commands.

echo -e "\e[0;34m========== SETTING FLATPAK ON DEBIAN ==========\e[0m"

# VARIABLES
echo -e "\e[0;32m---------- variables ----------\e[0m"
echo $HOME

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

echo -e "\e[0;34m========== FINISHED ==========\e[0m"