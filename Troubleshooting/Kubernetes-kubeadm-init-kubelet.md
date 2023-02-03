# kubelet isn't running or healthy when kubeadm init

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.0

## Problem

When I tried to kubeadm init on master server, the error with `kubelet isn't running or healthy` appeared.

Before this, I used:

1. minikube with Kubernetes 1.26.0 on Ubuntu 22.04.1 LTS 
2. minikube with Kubernetes 1.24.0 on Ubuntu 22.04.1 LTS
3. Kubernetes 1.26.0 on Ubuntu 18.04.6 LTS (VM)
4. Kuberentes 1.24.0 on Ubuntu 20.04.5 LTS (VM)

Since 1.26.0 supports swap, there was no error. Also VMs didn't set swap, so there was no error.

## [Solution](https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy)

Disable swap:

```Bash
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab
```

Reset kubeadm:

```Bash
kubeadm reset
```

Re-initialize kubeadm

```Bash
kubeadm init ...
```

---

### Reference
- kubeadm init shows kubelet isn't running or healthy, https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy, 2023-02-03-Fri.
