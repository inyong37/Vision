# Using containerd for CRI in Kubernetes

## Date

2023-02-02-Thursday

## Environment

Ubuntu 22.04 LTS

## Problem

I am trying to organize new Kubernetes cluster with 3 Ubuntu 22.04 LTS PCs. After setting network, I installed continerd with `apt install containerd.io` as below steps.

:key: [Setup containerd for CRI](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd)

:key: [Install containerd](https://github.com/containerd/containerd/blob/main/docs/getting-started.md): The containerd.io package contains runc too, but does not contain CNI plugins.

:key: [Install containerd on Ubuntu via installing Docker](https://docs.docker.com/engine/install/ubuntu/)

However, I got an error when I commanded `kubeadm init -- ...`

<img width="2236" alt="Screenshot 2023-02-02 at 11 04 22 AM" src="https://user-images.githubusercontent.com/20737479/216213128-c0d711f3-864f-4f07-83c8-b7f15561e8f4.png">

## Solution

---

### Reference
- 
