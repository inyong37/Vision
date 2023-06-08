# Setup Docker on Fedora

## Date

2023-04-19-Wednesday.

## Environment

Fedora 37

## [Setup Docker on Fedora](https://docs.docker.com/engine/install/fedora/)

### 0. Uninstall Old Versions

```Bash
sudo dnf remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-selinux \
                  docker-engine-selinux \
                  docker-engine
```

### 1. Setup the Repository

```Bash
sudo dnf -y install dnf-plugins-core
```

```Bash
sudo dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo
```

### 2-A. Install the Latest Version of Docker Engine

```Bash
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### 2-B. Install Specific Version of Docker Engine

Check the versions:

```Bash
dnf list docker-ce  --showduplicates | sort -r
```

Set the specific version:

```Bash
VERSION_STRING=3:23.0.4-1.fc37
```

Install:

```Bash
sudo dnf -y install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io docker-buildx-plugin docker-compose-plugin
```

### 3. Start Docker

```Bash
sudo systemctl start docker
```

---

### Reference
- Install Docker Fedora, https://docs.docker.com/engine/install/fedora/, 2023-04-19-Wed.
