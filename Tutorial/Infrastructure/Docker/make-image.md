# Make a Docker Image from a Container

## Date

2023-04-13-Thursday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS Image

## 1. Save & Load

Export는 container를 동작하는데 필요한 모든 파일(root의 파일 시스템 전체)이 압축된다. 

Save는 layer 구조, history를 포함한 형태로 압축이 된다.

Check docker images:

```Bash
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
flatpak-repository         0.0.1     ecb5a13275a6   58 minutes ago   5.95GB
```

### Save

```Bash
sudo docker save -o {file-name}.tar {image-name}:{tag}
# sudo docker save -o ubuntu-flatpak-repository-save.tar flatpak-repository:0.0.1
```

### Load

```Bash
sudo docker load -i {file-name}.tar
# sudo docker load -i ubuntu-flatpak-repository-save.tar
```

Output:

```Bash
(base) inyong@desktop:~$ sudo docker load -i ubuntu-flatpak-repository-save.tar
7363a407772c: Loading layer [==================================================>]  6.019GB/6.019GB
Loaded image: flatpak-repository:0.0.1
```


---

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

Method 1:

```Bash
cat {file-name}.tar | docker import - {repository-name}:{tag}
# cat ubuntu-flatpak-repository-export.tar | docker import - flatpak-repository:0.0.1
```

:tada: Verify:

```Bash
(base) inyong@desktop:~$ cat ubuntu-flatpak-repository-export.tar | docker import - flatpak-repository:0.0.1
sha256:ecb5a13275a6fe92da5edf83eacf89b0610bfac988d6e825c6587798c6bbb183
(base) inyong@desktop:~$ docker images
REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
flatpak-repository         0.0.1     ecb5a13275a6   34 seconds ago   5.95GB
ubuntu                     22.04     08d22c0ceb15   5 weeks ago      77.8MB
infra/ubuntu-aptget-test   v0.0.1    2b81ec1d5dfd   5 months ago     246MB
urpylka/aptly              latest    6a730f747e5e   7 months ago     322MB
progrium/stress            latest    db646a8f4087   8 years ago      282MB
```

Method 2:

```Bash
sudo docker import {file-name or url} - {image-name}:{tag}
# sudo docker import ubuntu-flatpak-repository-export.tar
```

:tada: Verify

```Bash
-rw-rw-r--  1 inyong inyong 5.7G Apr 13 14:17  ubuntu-flatpak-repository-export.tar
-rw-------  1 root   root   5.7G Apr 13 16:13  ubuntu-flatpak-repository-save.tar
-rw-rw-r--  1 inyong inyong 6018519040 Apr 13 14:17  ubuntu-flatpak-repository-export.tar
-rw-------  1 root   root   6018527232 Apr 13 16:13  ubuntu-flatpak-repository-save.tar
```

---

## Deploy a Container

```Bash
docker run --name={container_name} -it {image_name}:{tag} /bin/bash
# docker run --name=repo -it flatpak-repository:0.0.1 /bin/bash
```

Run command는 exit하면 stop이 되기 때문에 다른 방식으로 나오거나 나온 뒤 start로 다시 키고 접속해야 한다.

---

### Reference
- Docker Image, https://tjddnjs.tistory.com/102, 2023-04-13-Thu.
