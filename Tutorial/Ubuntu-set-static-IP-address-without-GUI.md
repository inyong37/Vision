# Set static IP address without GUI on Ubuntu 22.04 LTS Server

## Date

2023-02-13-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Problem/situaion

Try to set up static IP address on Ubuntu 22.04 LTS Server without GUI

## [Solution](https://devtutorial.io/how-to-configure-static-ip-address-on-ubuntu-server-22-04-ubuntu-server-22-04-p3098.html)

Before:

```Bash
cat /etc/netplan/00-installer-config.yaml
# This is the network config written by 'subiquity'
network:
  ethernets:
    eno1:
      dhcp4: true
  version: 2
```

After:

```Bash
```

---

### Reference
- https://devtutorial.io/how-to-configure-static-ip-address-on-ubuntu-server-22-04-ubuntu-server-22-04-p3098.html
