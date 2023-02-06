# kubectl connection refused

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

<img width="719" alt="Screenshot 2023-02-03 at 4 30 04 PM" src="https://user-images.githubusercontent.com/20737479/216538804-2ce575b5-a577-483b-ba46-070a63acb7c4.png">

## [Solution #1](https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/5)

<img width="746" alt="Screenshot 2023-02-03 at 4 30 19 PM" src="https://user-images.githubusercontent.com/20737479/216538838-67433791-feaa-407d-8cb2-1cf7d3c27495.png">

After few minutes, suddenly it works...

Master01: 

> <img width="355" alt="Screenshot 2023-02-03 at 4 36 08 PM" src="https://user-images.githubusercontent.com/20737479/216539886-ba7117fa-9805-4d61-99c5-dfa0eb74ac86.png">

Node01:

> <img width="1252" alt="Screenshot 2023-02-03 at 4 36 22 PM" src="https://user-images.githubusercontent.com/20737479/216539932-c397c080-a51f-4a6a-aa13-a4db7df02ab4.png">

Node02:

> <img width="1256" alt="Screenshot 2023-02-03 at 4 36 32 PM" src="https://user-images.githubusercontent.com/20737479/216539955-fe024a51-ffcf-4cae-9f08-be2b74772ce6.png">

## [Solution #2](https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/24)

Disable firewall

```Bash
ufw status verbose
ufw disable
systemctl restart kubelet
```

---

### Reference
- The connection to the server <host>:6443 was refused - did you specify the right host or port?, https://discuss.kubernetes.io/t/the-connection-to-the-server-host-6443-was-refused-did-you-specify-the-right-host-or-port/552/5, 2023-02-03-Fri.
