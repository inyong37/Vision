# :whale: Install Docker Engine on CentOS

## Date

2023-01-26-Thursday.

## Environment 

CentOS 7

## OS Requirements

CentOS 7 / CentOS 8 (stream) / CentOS 9 (stream)

## [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)

### 1. Set up the repository

```Bash
sudo yum install -y yum-utils
```

```Bash
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

### 2. Install Docker Engine

Check available versions:

```Bash
sudo yum list docker-ce --showduplicates | sort -r
```

2-A. Specify docker engine version

```Bash
DOCKER_VERSION=18.09.1
```

Install specified version of docker engine:

```Bash
sudo yum install -y docker-ce-<DOCKER_VERSION> docker-ce-cli-<DOCKER_VERSION> containerd.io docker-compose-plugin
```

2-B. Install the latest version of docker engine

```Bash
sudo yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### 3. Start

```Bash
sudo systemctl enable docker
sudo systemctl start docker
```

### :tada: Verify

```Bash
sudo docker run hello-world
```

---

### Reference

- Install Docker Engine on CentOS, https://docs.docker.com/engine/install/centos/, 2023-01-26-Thu.
