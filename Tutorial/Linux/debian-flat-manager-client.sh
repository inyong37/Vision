#!/usr/bin/ bash

# Author: In Yong Hwang (inyong1020 [at] gmail {dot} com)
# Date: 2023-03-28-Tuesday.

echo "========== SETTING FLAT-MANAGER CLIENT ON DEBIAN =========="

# VARIABLES
echo $HOME

# INSTALLING "RUST"
curl https://sh.rustup.rs -sSf | sh -s -- -y

# INSTALLING PACKAGES
sudo apt install -y cargo postgresql-devel ostree-devel ostree git
sudo apt install -y git libcurl4-openssl-dev libsoup2.4-dev autoconf dracut libtool libglib2.0-dev libgpgme-dev bison liblzma-dev e2fslibs-dev libfuse-dev libsystemd-dev tree tmux gtk-doc-tools

# INSTALLING OSTREE
cd $HOME
git clone https://github.com/ostreedev/ostree.git
cd ostree
git submodule update --init
env NOCONFIGURE=1 ./autogen.sh
./configure --prefix=/usr --with-dracut --with-curl --with-builtin-grub2-mkconfig
make -j
sudo make install -j

# CLONING A GIT REPOSITORY
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

echo "========== FINISHED =========="
