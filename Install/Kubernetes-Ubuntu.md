# Install Kubernetes on Ubuntu

## Date

2023-02-02-Thursday.

## Environment

Ubuntu 20.04.5 LTS

## Content

:key: All commands are executed on root authority.

### 1. [Network](https://github.com/inyong37/Vision/blob/master/Install/Kubernetes-Vagrant-Ubuntu.md)

Make k8s modules configuration:

```Bash
vim /etc/modules-load.d/k8s.conf
```

as below:

```conf
overlay
br_netfilter
```

Apply:

```Bash
modprobe overlay
modprobe br_netfilter
```

Make k8s system configuration:

```Bash
vim /etc/sysctl.d/k8s.conf
```

as below:

```conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
```

Apply:

```Bash
sysctl --system
```

### 2. [Container Runtime Interface - containerd](https://github.com/inyong37/Vision/blob/master/Troubleshooting/Install-containerd.md)

```Bash
apt update && apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg2
```


```Bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
```

```Bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Remove old containerd:

```Bash
apt remove -y containerd
```

Install containerd:

```Bash
apt install -y containerd.io
```

```Bash
systemctl restart containerd
```

### 3. [kubeadm, kubectl, kubelet](https://github.com/inyong37/Vision/blob/master/Install/Kubernetes-Vagrant-Ubuntu.md) in [specific version](https://github.com/inyong37/Vision/blob/master/Tutorial/Kubernetes-Downgrade.md)

```Bash
apt update && apt install -y apt-transport-https ca-certificates curl
```

```Bash
curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

```Bash
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
```

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

```Bash
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

Finally, join from worker nodes:

```Bash
kubeadm join {master_ip} -- token {token} --discovery-token-ca-cert-hash {sha256}
```

---

### Reference
- Install Kubernetes Cluster using Vagrant on Ubuntu, https://github.com/inyong37/Vision/blob/master/Install/Kubernetes-Vagrant-Ubuntu.md, 2023-02-02-Thu.
- Using containerd for CRI in Kubernetes, https://github.com/inyong37/Vision/blob/master/Troubleshooting/Install-containerd.md, 2023-02-02-Thu.
- Downgrade Kubernetes, https://github.com/inyong37/Vision/blob/master/Tutorial/Kubernetes-Downgrade.md, 2023-02-02-Thu.
- Kubernetes Nodes' status are NotReady, https://github.com/inyong37/Vision/blob/master/Troubleshooting/Kubernetes-not-ready.md, 2023-02-02-Thu.
