# [Install Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

## Environment

Ubuntu 22.04 LTS

## Requirement

64-bit version

Ubuntu 22.10 Kinetic

Ubuntu 22.04 LTS Jammy

Ubuntu 20.04 LTS Focal

Ubuntu 18.04 LTS Bionic

## Install using the repository

### 1. Set up the repository

```Bash
$ sudo apt-get update
```

```Bash
$ sudo apt-get install -y ca-certificates curl gnupg lsb-release
```

```Bash
$ sudo mkdir -p /etc/apt/keyrings
```

```Bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

```Bash
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

### 2. Install Docker Engine

```Bash
$ sudo apt-get update
```

Check available version:

```Bash
$ sudo apt-cache madison docker-ce | awk '{ print $3 }'
```

Specify `$DOCKER_VERSION_STRING`

```Bash
$ DOCKER_VERSION=5:20.10.13~3-0~ubuntu-jammy
$ sudo apt-get install docker-ce=$DOCKER_VERSION docker-ce-cli=$VDOCKER_VERSION containerd.io docker-compose-plugin
```

---

### Reference

- Install Docker Engine on Ubuntu, https://docs.docker.com/engine/install/ubuntu/, 2023-02-01-Wed.
