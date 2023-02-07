# Kubectl Connection Refused

## Date

#1 2023-01-20-Friday.

#2 2023-01-25-Wednesday.

#3 2023-02-03-Friday.

#4 2023-02-07-Tuesday.

## Environment

Ubuntu 18.04.6 LTS -> Ubuntu 22.04.1 LTS

Kubernetes 1.26.0 -> Kubernetes 1.24.10

## Problem

`kubectl get pods` and `kubectl get nodes` don't work as below:

#1

<img width="1320" alt="Screenshot 2023-01-20 at 10 54 47 AM" src="https://user-images.githubusercontent.com/20737479/213601250-190428d6-636b-43e9-92b7-d98bffd974cf.png">

#2

<img width="1322" alt="Screenshot 2023-01-25 at 2 01 44 PM" src="https://user-images.githubusercontent.com/20737479/214484112-23d80b09-74f1-4a56-8a6d-33adebaabb52.png">

#3 

<img width="719" alt="Screenshot 2023-02-03 at 4 30 04 PM" src="https://user-images.githubusercontent.com/20737479/216538804-2ce575b5-a577-483b-ba46-070a63acb7c4.png">

#4 

<img width="1160" alt="Screenshot 2023-02-07 at 10 50 34 AM" src="https://user-images.githubusercontent.com/20737479/217127446-3a368526-c813-4e95-8115-b6c6e77f7cb7.png">

## [Solution #1](https://k21academy.com/docker-kubernetes/the-connection-to-the-server-localhost8080-was-refused/)

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


## [Solution #3](https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/5)

Disable swap

<img width="746" alt="Screenshot 2023-02-03 at 4 30 19 PM" src="https://user-images.githubusercontent.com/20737479/216538838-67433791-feaa-407d-8cb2-1cf7d3c27495.png">

After few minutes, suddenly it works...

Master01: 

> <img width="355" alt="Screenshot 2023-02-03 at 4 36 08 PM" src="https://user-images.githubusercontent.com/20737479/216539886-ba7117fa-9805-4d61-99c5-dfa0eb74ac86.png">

Node01:

> <img width="1252" alt="Screenshot 2023-02-03 at 4 36 22 PM" src="https://user-images.githubusercontent.com/20737479/216539932-c397c080-a51f-4a6a-aa13-a4db7df02ab4.png">

Node02:

> <img width="1256" alt="Screenshot 2023-02-03 at 4 36 32 PM" src="https://user-images.githubusercontent.com/20737479/216539955-fe024a51-ffcf-4cae-9f08-be2b74772ce6.png">

## [Solution #3](https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/24)

Disable firewall

```Bash
ufw status verbose
ufw disable
systemctl restart kubelet
```

---

### Reference
- The connection to the server localhost:8080 was refused – did you specify the right host or port?, https://k21academy.com/docker-kubernetes/the-connection-to-the-server-localhost8080-was-refused/, 2023-01-20-Fri.
- The connection to the server <host>:6443 was refused - did you specify the right host or port?, https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/5, 2023-02-03-Fri.
