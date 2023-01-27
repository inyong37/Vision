# Install and Setup CentOS 7 Linux

## Download

CentOS Linux ~ 7

CentOS Stream 8 ~

Rocky Linux 8 ~

## Install

## Setup

### [ssh](https://www.wikihow.com/Enable-Ssh-in-Centos-7)

:key: Usually already setup.

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
$ sudo systemctl status sshd .
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

### [docker](https://docs.docker.com/engine/install/centos/)

Set up the repository:

```Bash
$ sudo yum install -y yum-utils
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

To install the latest version, run:

```Bash
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Start:

```Bash
$ sudo systemctl start docker
```

---

### Reference
- How to Enable SSH in CentOS 7, https://www.wikihow.com/Enable-Ssh-in-Centos-7, 2023-01-26-Thu.
- How To Install Git on CentOS 7, https://www.digitalocean.com/community/tutorials/how-to-install-git-on-centos-7, 2023-01-26-Thu.
- docker, https://docs.docker.com/engine/install/centos/, 2023-01-26-Thu.