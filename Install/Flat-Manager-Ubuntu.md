# [Install Flatpak Repository]

## Date

2023-03-20-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Install flat-manager

### Install cargo

```Bash
sudo apt install cargo
```

### [Install postgresql](https://www.postgresql.org/download/linux/ubuntu/)

```Bash
sudo apt install wget ca-certificates
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql
```

### Install ostree

```Bash
apt install ostree
```

---

### Reference
- flat-manager GitHub, https://github.com/flatpak/flat-manager, 2023-03-20-Mon.
- postgresql Download, https://www.postgresql.org/download/linux/ubuntu/, 2023-03-20-Mon.
- 
