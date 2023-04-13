# Delete an Image

## Date

2023-04-13-Thursday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

## Delete an Image

Check images:

```Bash
(base) inyong@desktop:~$ sudo docker images
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

Remove an image:

```Bash
(base) inyong@desktop:~$ sudo docker image rm 8715103a39da
Deleted: sha256:8715103a39da07f16f47915572d1452a35a5f965393acc9e63ea5d5e4058de8a
Deleted: sha256:7363a407772c4fe3db90068f8eb9ed9a42474ebec2adc7a136b97a364d38ec8b
```

---

### Try

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
