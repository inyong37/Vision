# missing optional cgroups: blkio when kubeadm init

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.0

## Problem

<img width="797" alt="Screenshot 2023-02-03 at 3 55 04 PM" src="https://user-images.githubusercontent.com/20737479/216532583-a4e24df9-8d8c-4e35-9fee-16bfbb1c418a.png">

## [Solution](https://unix.stackexchange.com/questions/707338/kubeadm-init-missing-optional-cgroups)

Upgrade Kubernetes version (more than Kubernetes 1.24.0)

---

### Reference
- kubeadm init missing optional cgroups, https://unix.stackexchange.com/questions/707338/kubeadm-init-missing-optional-cgroups, 2023-02-03-Fri.
