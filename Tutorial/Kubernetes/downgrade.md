# Downgrade/remove Kubernetes

## Date

2023-02-02-Thursday.

2023-02-07-Tuesday.

## Environment

Ubuntu 20.04.5 LTS -> Ubuntu 22.04.1 LTS

Kubernetes 1.26.1 -> 1.24.00 -> 1.24.10

## Contents

### 1. Reset on each machines

```Bash
kubeadm reset
rm -rf $HOME/.kube /etc/cni/net.d /opt/cni /etc/kubernetes
``` 

```Bash
apt install ipvsadm
ipvsadm --clear
```

### 2. [Uninstall kubeadm, kubectl, and kubelet](https://stackoverflow.com/questions/44698283/how-to-completely-uninstall-kubernetes)

```Bash
apt remove kubeadm kubectl kubelet
apt autoremove
```

### 3. [Install kubeadm, kubectl, and kubelet with specific version](https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes)

Check available versions:

```Bash
curl -s https://packages.cloud.google.com/apt/dists/kubernetes-xenial/main/binary-amd64/Packages | grep Version | awk '{print $2}'
```

Install specific version:

```Bash
apt install kubeadm=1.24.10-00 kubectl=1.24.10-00 kubelet=1.24.10-00
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


### 4. Deploy pod network

A. Calico:

```Bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

B. Flannel:

```Bash
kubectl edit cm coredns -n kube-system
```

Edit as below:

```Bash
...
# loop
...
```

```Bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

Finally, join from worker nodes:

```Bash
kubeadm join {master_ip} -- token {token} --discovery-token-ca-cert-hash {sha256}
```

---

### Reference
- How to install specific version of Kubernetes?, https://stackoverflow.com/questions/49721708/how-to-install-specific-version-of-kubernetes, 2023-02-02-Thu.
- How to completely uninstall kubernetes, https://stackoverflow.com/questions/44698283/how-to-completely-uninstall-kubernetes, 2023-02-02-Thu.
- Ubuntu 22.04에 쿠버네티스 설치하기 (Install Kubernetes), https://andrewpage.tistory.com/234, 2023-02-07-Tue.
- How to Install Kubernetes on Ubuntu 22.04 / Ubuntu 20.04, https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-kubernetes-on-ubuntu-22-04.html, 2023-02-07-Tue.
- cri-dockerd GitHub, https://github.com/Mirantis/cri-dockerd, 2023-02-07-Tue.
- How to Install Containerd on Ubuntu 22.04 / Ubuntu 20.04, https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-containerd-on-ubuntu-22-04.html, 2023-02-07-Tue.
- How to Install CRI-O on Ubuntu 22.04 / Ubuntu 20.04, https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-cri-o-on-ubuntu-22-04.html, 2023-02-07-Tue.
