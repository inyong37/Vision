# Set static IP address without GUI on Ubuntu 22.04 LTS Server

## Date

2023-02-13-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Problem/situaion

Try to set up static IP address on Ubuntu 22.04 LTS Server without GUI

## Solution

Before:

```YAML
cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    eno1:
      dhcp4: true
  version: 2
```

After:

```YAML
cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    eno1:
      dhcp4: no
      addresses:
        - 192.168.0.2/24 # Your Static IP Address
      routes:
        - to: default
          via: 192.168.0.1 # Your AP's IP Address
      nameservers:
        addresses
          - 168.126.63.1 # KT DNS Server
          - 8.8.8.8 # Google DNS Server
          - 8.8.4.4 # Google 2nd DNS Server 
  renderer: networkd
  version: 2
```

:key: FYI:

```Bash
root@node85:~# netplan apply

** (generate:16132): WARNING **: 01:56:56.355: `gateway4` has been deprecated, use default routes instead.
See the 'Default routes' section of the documentation for more details.
```

Change `Gateway4` to `routes: -to: ... via: ...`.

---

### Reference
- How to Configure Static IP Address on Ubuntu Server 22.04 - Ubuntu Server 22.04, https://devtutorial.io/how-to-configure-static-ip-address-on-ubuntu-server-22-04-ubuntu-server-22-04-p3098.html, 2023-02-13-Mon.
- How to Set Static IP Address on Ubuntu Server 22.04, https://www.linuxtechi.com/static-ip-address-on-ubuntu-server/, 2023-02-13-Mon.
- How to Set Static IP Address and Configure Network in Linux, https://www.tecmint.com/set-add-static-ip-address-in-linux/, 2023-02-13-Mon.
- How to Configure Static IP Address on Ubuntu 22.04 LTS and 22.10, https://www.makeuseof.com/configure-static-ip-address-settings-ubuntu-22-04/, 2023-02-13-Mon.
- Ubuntu 18.04 Netplan을 사용한 Static IP 설정, https://blog.hkwon.me/ubuntu-18-04-netplan/, 2023-02-13-Mon.
- netplan generate: `gateway4` has been deprecated, use default routes instead, https://unix.stackexchange.com/questions/681220/netplan-generate-gateway4-has-been-deprecated-use-default-routes-instead, 2023-02-13-Mon.
