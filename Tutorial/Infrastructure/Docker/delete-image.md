# Delete an Image

## Date

2023-04-13-Thursday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

## Delete an Image

```Bash
sudo docker images rm {image_id}
```

Before deleting an image, make sure that related containers are removed.

---

1. List images: `docker images`

```Bash
(base) inyong@desktop:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
<none>                        <none>    8715103a39da   25 seconds ago   5.95GB
flat-manager                  0.1       a9ff3b483c58   25 hours ago     329MB
ubuntu                        22.04     08d22c0ceb15   5 weeks ago      77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago     246MB
ubuntu                        latest    cdb68b455a14   5 months ago     77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago     1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago     322MB
tibero                        latest    1a6ada668b7c   14 months ago    4.01GB
hello-world                   latest    feb5d9fea6a5   18 months ago    13.3kB
progrium/stress               latest    db646a8f4087   8 years ago      282MB
```

2. Remove an image: `docker image rm {image_id}

```Bash
(base) inyong@desktop:~$ sudo docker image rm 8715103a39da
Deleted: sha256:8715103a39da07f16f47915572d1452a35a5f965393acc9e63ea5d5e4058de8a
Deleted: sha256:7363a407772c4fe3db90068f8eb9ed9a42474ebec2adc7a136b97a364d38ec8b
```

:tada: Verify:

```Bash
(base) inyong@desktop:~$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
flat-manager                  0.1       a9ff3b483c58   25 hours ago     329MB
ubuntu                        22.04     08d22c0ceb15   5 weeks ago      77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago     246MB
ubuntu                        latest    cdb68b455a14   5 months ago     77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago     1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago     322MB
tibero                        latest    1a6ada668b7c   14 months ago    4.01GB
hello-world                   latest    feb5d9fea6a5   18 months ago    13.3kB
progrium/stress               latest    db646a8f4087   8 years ago      282MB
```

---

### Giving Repository Name as an Argument

Check images:

```Bash
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
flat-manager                  0.1       a9ff3b483c58   25 hours ago    329MB
ubuntu                        22.04     08d22c0ceb15   5 weeks ago     77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago    246MB
ubuntu                        latest    cdb68b455a14   5 months ago    77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago    1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago    322MB
tibero                        latest    1a6ada668b7c   14 months ago   4.01GB
hello-world                   latest    feb5d9fea6a5   18 months ago   13.3kB
progrium/stress               latest    db646a8f4087   8 years ago     282MB
```

Try to delete an image with its repository name:

```Bash
(base) inyong@desktop:~$ sudo docker image rm flat-manager
Error response from daemon: No such image: flat-manager:latest
```

Didn't work.

Re-try to delete an image with its ID:

```Bash
(base) inyong@desktop:~$ sudo docker image rm a9ff3b483c58
Untagged: flat-manager:0.1
Deleted: sha256:a9ff3b483c58aae563d2de35d45347bf103aadd090be2c6784bfe532ed4da95d
```

It worked.

:tada: Check images:

```
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
ubuntu                        22.04     08d22c0ceb15   5 weeks ago     77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago    246MB
ubuntu                        latest    cdb68b455a14   5 months ago    77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago    1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago    322MB
tibero                        latest    1a6ada668b7c   14 months ago   4.01GB
hello-world                   latest    feb5d9fea6a5   18 months ago   13.3kB
progrium/stress               latest    db646a8f4087   8 years ago     282MB
```

---

### Repository Name Worked... Hmmm...

```Bash
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
ubuntu                        22.04     08d22c0ceb15   5 weeks ago     77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago    246MB
ubuntu                        latest    cdb68b455a14   5 months ago    77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago    1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago    322MB
tibero                        latest    1a6ada668b7c   14 months ago   4.01GB
hello-world                   latest    feb5d9fea6a5   18 months ago   13.3kB
progrium/stress               latest    db646a8f4087   8 years ago     282MB
(base) inyong@desktop:~$ sudo docker image rm tibero
Untagged: tibero:latest
Deleted: sha256:1a6ada668b7ca5cb7dcc17bd7e85e2883c74ddb2bbaaa6de27f45fb067a2d49f
Deleted: sha256:7abb935e5fb5ac8ef1d277695b7bf1d75e32ee793b1639cc7863b3e63e7d1f6f
Deleted: sha256:2c6dce37f6d10239f6b92f630edf84410ef2d1513f62b273cd4ae16b2ecb58ea
Deleted: sha256:1f04d3bb0a774679683e487499e157682af1ba13a4cdb775041b879e344a82d4
Deleted: sha256:9f54eef412758095c8079ac465d494a2872e02e90bf1fb5f12a1641c0d1bb78b
(base) inyong@desktop:~$ sudo docker images
REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
ubuntu                        22.04     08d22c0ceb15   5 weeks ago     77.8MB
infra/ubuntu-aptget-test      v0.0.1    2b81ec1d5dfd   5 months ago    246MB
ubuntu                        latest    cdb68b455a14   5 months ago    77.8MB
gcr.io/k8s-minikube/kicbase   v0.0.35   7fb60d0ea30e   6 months ago    1.12GB
urpylka/aptly                 latest    6a730f747e5e   7 months ago    322MB
hello-world                   latest    feb5d9fea6a5   18 months ago   13.3kB
progrium/stress               latest    db646a8f4087   8 years ago     282MB
```
