# kubectl Connection Refused

## Environment

Ubuntu 18.04.6 LTS

Kubernetes 1.26.0

## Date

#1 2023-01-20-Friday

#2 2023-01-25-Wednesday

## Problem

`kubectl get pods` and `kubectl get nodes` don't work as below:

#1

<img width="1320" alt="Screenshot 2023-01-20 at 10 54 47 AM" src="https://user-images.githubusercontent.com/20737479/213601250-190428d6-636b-43e9-92b7-d98bffd974cf.png">

#2

<img width="1322" alt="Screenshot 2023-01-25 at 2 01 44 PM" src="https://user-images.githubusercontent.com/20737479/214484112-23d80b09-74f1-4a56-8a6d-33adebaabb52.png">

## [Solution](https://k21academy.com/docker-kubernetes/the-connection-to-the-server-localhost8080-was-refused/)

### A. Set the `$KUBECONFIG` to `admin.conf`

```Bash
$ export KUBECONFIG=/etc/kubernetes/admin.conf
```

### B. Copy/move the `admin.conf` to `$HOME` and set the `$KUBECONFIG`

```Bash
$ cp /etc/kubernetes/admin.conf $HOME/
$ chown $(id -u):$(id -g) $HOME/admin.conf
$ export KUBECONFIG=$HOME/admin.conf
```

## Fixed

#1

<img width="1011" alt="Screenshot 2023-01-20 at 10 59 53 AM" src="https://user-images.githubusercontent.com/20737479/213601883-3ea6f166-f912-4804-bacf-51cbc9e41c73.png">

#2

<img width="291" alt="Screenshot 2023-01-25 at 2 05 04 PM" src="https://user-images.githubusercontent.com/20737479/214484259-3b29df62-43eb-4d97-be7b-f07a4ca1461e.png">

---

### Reference

- The connection to the server localhost:8080 was refused – did you specify the right host or port?, https://k21academy.com/docker-kubernetes/the-connection-to-the-server-localhost8080-was-refused/, 2023-01-20-Fri.
