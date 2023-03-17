# Minikube Start Error

## Environment

Ubuntu 22.04.1 LTS

## Problem

minikube doesn't work properly with minikube start command.

```Bash
* minikube v1.28.0 on Ubuntu 22.04
* Unable to pick a default driver. Here is what was considered, in preference order:
  - docker: Not healthy: "docker version --format {{.Server.Os}}-{{.Server.Version}}" exit status 1: Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/version": dial unix /var/run/docker.sock: connect: permission denied
  - docker: Suggestion: Add your user to the 'docker' group: 'sudo usermod -aG docker $USER && newgrp docker' <https://docs.docker.com/engine/install/linux-postinstall/>
```

## Solution

The output of error told the solution as above.

```Bash
$ sudo usermod -aG docker $USER && newgrp docker
```

---

### Reference
- Docker Engine post-installation steps, https://docs.docker.com/engine/install/linux-postinstall/, 2022-10-19-Wed.
