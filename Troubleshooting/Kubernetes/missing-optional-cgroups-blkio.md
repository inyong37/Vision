# missing optional cgroups: blkio when kubeadm init

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.0

## Problem

<img width="797" alt="Screenshot 2023-02-03 at 3 55 04 PM" src="https://user-images.githubusercontent.com/20737479/216532583-a4e24df9-8d8c-4e35-9fee-16bfbb1c418a.png">

## [Solution](https://unix.stackexchange.com/questions/707338/kubeadm-init-missing-optional-cgroups)

Upgrade Kubernetes version (more than Kubernetes 1.24.0

1. Reset:

```Bash
kubeadm reset
```

2. Remove:

```Bash
apt remove kubeadm kubectl kubelet
apt autoremove
```

3. Install updated version:

```Bash
apt install -y kubeadm=1.24.10-00 kubectl=1.24.10-00 kubelet=1.24.10-00
```

4. Fix the version:

```Bash
apt-mark hold kubeadm kubectl kubelet
```

5. Init:

```
kubeadm init --pod-network-cidr ${IP}/16 --apiserver-advertise-address=${IP}
```

> <img width="801" alt="Screenshot 2023-02-03 at 3 59 15 PM" src="https://user-images.githubusercontent.com/20737479/216533311-d57762eb-2f4f-47dd-be04-bf2819e5d6b1.png">

---

### Reference
- kubeadm init missing optional cgroups, https://unix.stackexchange.com/questions/707338/kubeadm-init-missing-optional-cgroups, 2023-02-03-Fri.
