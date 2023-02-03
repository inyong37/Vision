# Install Kubernetes on Ubuntu (Experimental)

## Date

2023-02-02-Thursday.

2023-02-03-Friday.

## Environment

Ubuntu 20.04.5 LTS

Ubuntu 22.04.1 LTS

## Content

:key: All commands are executed on root authority.

### 1. [Network](https://github.com/inyong37/Vision/blob/master/Install/Kubernetes-Vagrant-Ubuntu.md)

Make k8s modules configuration:

```Bash
mkdir -p /etc/modules-load.d
cat <<EOF | tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

Apply:

```Bash
modprobe overlay
modprobe br_netfilter
```

Make k8s system configuration:

```Bash
mkdir -p /etc/sysctl.d
cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF 
```

Apply:

```Bash
sysctl --system
```

### 2. [Container Runtime Interface - containerd](https://github.com/inyong37/Vision/blob/master/Troubleshooting/Install-containerd.md)

Option A - Install bare-containerd:

```Bash
apt update && apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg2
```

```Bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
```

```Bash
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

:key: Remove old containerd on Ubuntu 20:

```Bash
apt remove containerd -y
```

:key: Remove old containerd on Ubuntu 22:

```Bash
apt remove containerd.io -y
```

Install containerd:

```Bash
apt install containerd.io -y
```

```Bash
systemctl restart containerd
```

:construction: There is an issue about cgroup. Therefore, I tried to solve this with installing Docker engine instead of bare-containerd. However, it did not work. Still same issue occured.

<img width="486" alt="Screenshot 2023-02-03 at 3 41 26 PM" src="https://user-images.githubusercontent.com/20737479/216530206-10c8dce0-505e-43c8-a5b5-79ed7f0d66cc.png">

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

:key: [If you want to use old version, then you have to disable swap](https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy):

```Bash
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab
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
# export KUBECONFIG=/etc/kubernetes/kubelet.conf # sometimes, kubelet exists.
```

Option A - Deploy CoreDNS pod network:

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

Option B - Deploy Weave pod network (only a command):

```Bash
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
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
- kubeadm init shows kubelet isn't running or healthy, https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy, 2023-02-03-Fri.
