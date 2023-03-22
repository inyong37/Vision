# Install and Setup CentOS 7 Linux

## Download

CentOS Linux ~ 7

CentOS Stream 8 ~

Rocky Linux 8 ~

## Install

## Setup

using root: `$ su`

### [Set-up static IP address](https://www.manualfactory.net/10004)

```Bash
vi /etc/sysconfig/network-scripts/ifcfg-{ethernet_number} # {ethernet_number} might seem 'eno1'
```

Edit configuration as:

```YAML
TYPE=Ethernet
PROXY_METHOD=none
BROWSER_ONLY=no
BOOTPROTO=none
DEFROUTE=yes
IPV4_FAILURE_FATAL=no
IPV6INIT=yes
IPV6_AUTOCONF=yes
IPV6_DEFROUTE=yes
IPV6_FAILURE_FATAL=no
IPV6_ADDR_GEN_MODE=stable-privacy
NAME=eno1
UUID=e0f27782-11c0-4858-abb8-c8a4f6066f8d
DEVICE=eno1
ONBOOT=yes
IPADDR=192.168.10.77
PREFIX=24
GATEWAY=192.168.10.1
DNS1=8.8.8.8
DNS2=8.8.4.4
IPV6_PRIVACY=no
```

Restart network service:

```Bash
systemctl restart network
```

### [ssh](https://www.wikihow.com/Enable-Ssh-in-Centos-7)

:key: Usually ssh server service is already set-up.

FYI:

```Bash
$ sudo yum -y install openssh-server openssh-clients
```

> <img width="699" alt="Screenshot 2023-01-26 at 3 51 01 PM" src="https://user-images.githubusercontent.com/20737479/214774473-edd8d171-14e1-4559-8c80-50dfd2f65fe6.png">

Start:

```Bash
$ sudo systemctl start sshd
```

Check:

```Bash
$ sudo systemctl status sshd
```

> <img width="628" alt="Screenshot 2023-01-26 at 3 51 50 PM" src="https://user-images.githubusercontent.com/20737479/214774577-0c968390-c7af-4cc6-bcd5-b38147beae53.png">

### [git](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-centos-7)

Install:

```Bash
$ sudo yum install git
```

Verify:
```Bash
$ git --version
```

---

### Reference
- How to Enable SSH in CentOS 7, https://www.wikihow.com/Enable-Ssh-in-Centos-7, 2023-01-26-Thu.
- How To Install Git on CentOS 7, https://www.digitalocean.com/community/tutorials/how-to-install-git-on-centos-7, 2023-01-26-Thu.
- Set-up Static IP Blog KR, https://www.manualfactory.net/10004, 2023-03-22-Wed.
