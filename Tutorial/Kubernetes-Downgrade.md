# Downgrade Kubernetes

## Date

2023-02-02-Thursday.

## Environment

Ubuntu 20.04.5 LTS

Kubernetes 1.26.1 -> 1.24.00

## Contents

### 1. Reset on each machines

```Bash
kubeadm reset
```

### 2. [Uninstall kubeadm, kubectl, and kubelet](https://stackoverflow.com/questions/44698283/how-to-completely-uninstall-kubernetes)

```Bash
apt remove -y kubeadm kubectl kubelet
```

### 3. [Install kubeadm, kubectl, and kubelet with specific version](https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes)

Check available versions:

```Bash
curl -s https://packages.cloud.google.com/apt/dists/kubernetes-xenial/main/binary-amd64/Packages | grep Version | awk '{print $2}'
```

Install specific version:

```Bash
apt install -y kubeadm=1.24.0-00 kubectl=1.24.0-00 kubelet=1.24.0-00
```

Fix the versions:

```Bash
apt-mark hold kubelet kubeadm kubectl
```

Initialize:

```Bash
kubeadm init --pod-network-cidr <ip_address>/16 --apiserver-advertise-address=<master_node_ip_address>
```

Set admin.conf path:

```Bash
export KUBECONFIG=/etc/kubernetes/admin.conf
```

Deploy pod network:

```Bash
kubectl edit cm coredns -n kube-system
```

Edit as below:

```Bash
...
# loop
...
```

---

### Reference
- How to install specific version of Kubernetes?, https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes, 2023-02-02-Thu.
- How to completely uninstall kubernetes, https://stackoverflow.com/questions/44698283/how-to-completely-uninstall-kubernetes, 2023-02-02-Thu.
