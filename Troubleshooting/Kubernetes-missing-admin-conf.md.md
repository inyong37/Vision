# Missing admin.conf file on Kubernetes Node

## Date

2023-02-03-Friday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.0

## Problem

<img width="712" alt="Screenshot 2023-02-03 at 2 00 00 PM" src="https://user-images.githubusercontent.com/20737479/216516305-b3c05762-8fc7-4dbe-9894-881df3ee884f.png">


## [Solution](https://stackoverflow.com/questions/66213199/config-not-found-etc-kubernetes-admin-conf-after-setting-up-kubeadm-worker)

<img width="422" alt="Screenshot 2023-02-03 at 1 59 41 PM" src="https://user-images.githubusercontent.com/20737479/216516279-0e90a35f-ceb4-4507-8d09-23c81cc25040.png">

Check $HOME and /etc/kubernetes/ directories:

```Bash
ls ~
ls /etc/kubernetes/
```

Copy/move kubelet.conf to destination and named `admin.conf`:

```Bash
cp /etc/kubernetes/kubelet.conf ~/admin.conf
```

Set $KUBECONFIG:

```Bash
export KUBECONFIG=~/admin.conf
```

Verify:

```Bash
kubectl
```

---

### Reference
- Config not found: /etc/kubernetes/admin.conf -- After setting up kubeadm worker node, https://stackoverflow.com/questions/66213199/config-not-found-etc-kubernetes-admin-conf-after-setting-up-kubeadm-worker, 2023-02-03-Fri.
