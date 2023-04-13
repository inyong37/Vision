# Make a Docker Image from a Container

## Date

2023-04-13-Thursday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS Image

## 1. Save & Load

Check docker images:

```Bash
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
flat-manager                  0.1       a9ff3b483c58   24 hours ago    329MB
```

### Save

```Bash
sudo docker save -o {file-name}.tar {image-name}:{tag}
# sudo docker save -o ubuntu-flatpak-repository-save.tar flat-manager
```

### Load

```Bash
sudo docker load -i {file-name}.tar
# sudo docker load -i ubuntu-flatpak-repository-save.tar
```

## 2. Export & Import

Check docker containers:

```Bash
(base) inyong@desktop:~$ sudo docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED       STATUS       PORTS     NAMES
1b0ca2b05e14   ubuntu:22.04   "/bin/bash"   4 hours ago   Up 4 hours             u1
```

### Export

```Bash
sudo docker export {container-name or container-id} > {file-name}.tar
# sudo docker export u1 > ubuntu-flatpak-repository-export.tar
```

### Import

```Bash
sudo docker import {file-name or url} - {image-name}:{tag}
# sudo docker import ubuntu-flatpak-repository-export.tar
```

:tada: Verify

```Bash
-rw-rw-r--  1 inyong inyong 6018519040 Apr 13 14:17  ubuntu-flatpak-repository-export.tar
-rw-------  1 root   root    345286656 Apr 13 14:15  ubuntu-flatpak-repository-save.tar
```

Export는 container를 동작하는데 필요한 모든 파일(root의 파일 시스템 전체)이 압축된다. 

Save는 layer 구조, history를 포함한 형태로 압축이 왼다.

---

### Reference
- Docker Image, https://tjddnjs.tistory.com/102, 2023-04-13-Thu.
