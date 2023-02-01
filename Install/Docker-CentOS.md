# [Install Docker Engine on CentOS](https://docs.docker.com/engine/install/centos/)

## Environment 

CentOS 7

## Requirement

CentOS 7

CentOS 8 (stream)

CentOS 9 (stream)

## Install using the repository

### 1. Set up the repository

```Bash
$ sudo yum install -y yum-utils
```

```Bash
$ sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

### 2. Install Docker Engine

Check available versions:

```Bash
$ sudo yum list docker-ce --showduplicates | sort -r
```

A. Specify `$DOCKER_VERSION`

```Bash
$ DOCKER_VERSION=docker-ce-18.09.1
$ sudo yum install docker-ce-<DOCKER_VERSION> docker-ce-cli-<DOCKER_VERSION> containerd.io docker-compose-plugin
```

B. To install the latest version, run:

```Bash
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

### 3. Start

```Bash
$ sudo systemctl start docker
```

### 4. Verify

```Bash
$ sudo docker run hello-world
```

---

### Reference

- Install Docker Engine on CentOS, https://docs.docker.com/engine/install/centos/, 2023-01-26-Thu.
