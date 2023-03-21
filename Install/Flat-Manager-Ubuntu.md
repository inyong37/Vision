# [Install Flatpak Repository](https://github.com/flatpak/flat-manager)

## Date

2023-03-20-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Install flat-manager

```Bash
apt-get install gcc g++ libudev-dev pkg-config file make cmake
apt-get install perl yasm
apt-get install openssl libudev-dev file curl jq
apt-get install build-essential libssl-dev git libclang-dev
apt-get install intltool
apt-get install libglib2.0-dev
```

### Install cargo

```Bash
apt install cargo
```

### [Install postgresql](https://www.postgresql.org/download/linux/ubuntu/)

```Bash
apt install wget ca-certificates
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
apt-get update
apt-get -y install postgresql
```

### Install ostree

```Bash
apt install ostree
```

### Clone flat-manager

```Bash
git clone https://github.com/flatpak/flat-manager.git
```

### Build

```Bash
cd {workspace}/flat-manager
cargo build
```

---

### Reference
- flat-manager GitHub, https://github.com/flatpak/flat-manager, 2023-03-20-Mon.
- postgresql Download, https://www.postgresql.org/download/linux/ubuntu/, 2023-03-20-Mon.
- failed to run custom build command, https://github.com/openethereum/openethereum/issues/415, 2023-03-21-Tue.
