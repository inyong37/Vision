# Install Kubernetes on Ubuntu

## Date

2023-02-02-Thursday.

2023-02-03-Friday.

2023-06-15-Thursday.

## Environment

* Ubuntu 22.04 LTS/22.04.1 LTS/22.04.2 LTS
  * Kubernetes 1.24.10
  * CRI-O 1.24
  * WeaveNet 2.8.1

## Content

:key: All commands are executed on root authority.

### 0. [Set Swap Off](https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy):

```Bash
swapoff -a
sed -i '/ swap / s/^/#/' /etc/fstab
```

:key: Make sure the last line of `/etc/fstab` is commented out.

### 0. [Disable Firewall](https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-kubernetes-on-ubuntu-22-04.html)

0-0-A. Disable all

```Bash
systemctl stop firewalld
systemctl disable firewalld
```

0-0-B-a. Allow ports on Master Node

```Bash
apt install ufw -y
ufw allow 6443/tcp
ufw allow 2379/tcp
ufw allow 2380/tcp
ufw allow 10250/tcp
ufw allow 10257/tcp
ufw allow 10259/tcp
ufw reload
```

0-0-B-b. Allow ports on Worker Node

```Bash
ufw allow 10250/tcp
ufw allow 30000:32767/tcp
ufw reload
```

### 0. Set Network

Make k8s modules configuration:

```Bash
mkdir -p /etc/modules-load.d
```

```Bash
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
```

```Bash
cat <<EOF | tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF
```

Apply:

```Bash
sysctl --system
```

### 1. [Install Container Runtime Interface - CRI-O](https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-cri-o-on-ubuntu-22-04.html)

:key: Kubernetes 1.24, the Docker will no longer be supported as a runtime due to the removal of Dockershim. Or Docker Engine (For Kubernetes v1.24 and newer, you need to install cri-docker). CRI-O has built-in CNI (can be used with Kubernetes).

:key: Set OS version and CRIO version to use. I will use Kubernetes 1.24.10, therefore, I will set `CRIO_VERSION` as 1.24:

```Bash
export OS_VERSION=xUbuntu_22.04
export CRIO_VERSION=1.24
```

```Bash
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS_VERSION/Release.key | gpg --dearmor -o /usr/share/keyrings/libcontainers-archive-keyring.gpg
```

```Bash
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$CRIO_VERSION/$OS_VERSION/Release.key | gpg --dearmor -o /usr/share/keyrings/libcontainers-crio-archive-keyring.gpg
```

```Bash
echo "deb [signed-by=/usr/share/keyrings/libcontainers-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS_VERSION/ /" | tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
```

```Bash
echo "deb [signed-by=/usr/share/keyrings/libcontainers-crio-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$CRIO_VERSION/$OS_VERSION/ /" | tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$CRIO_VERSION.list
```

```Bash
apt update && apt install -y cri-o cri-o-runc
```

```Bash
systemctl daemon-reload
```

```Bash
systemctl enable crio
```

```Bash
systemctl start crio
```

```Bash
systemctl status crio
```

Verify:

```Bash
apt install -y cri-tools
crictl --runtime-endpoint unix:///var/run/crio/crio.sock version
crictl info
```

### 2. Install Kubernetes

```Bash
apt update && apt install -y apt-transport-https ca-certificates curl
```

Download the Google Cloud public signing key:

```Bash
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
```

Add the Kubernetes apt repository:

```Bash
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
```

<!--
```Bash
curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

```Bash
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
```
-->

:key: FYI: Check available versions:

```Bash
curl -s https://packages.cloud.google.com/apt/dists/kubernetes-xenial/main/binary-amd64/Packages | grep Version | awk '{print $2}'
```

3-1-A. Install specific version:

```Bash
apt update && apt install -y kubeadm=1.24.10-00 kubectl=1.24.10-00 kubelet=1.24.10-00
```

3-1-B. Install latest version:

```Bash
apt update && apt intall -y kubeadm kubectl kubelet
```

Fix the versions:

```Bash
apt-mark hold kubelet kubeadm kubectl
```

### :control_knobs: Initialize on Master Node

```Bash
kubeadm init --pod-network-cidr <ip_address>/16 --apiserver-advertise-address=<master_node_ip_address>
```

### :control_knobs: Set Variable Path on Master Node

```Bash
export KUBECONFIG=/etc/kubernetes/admin.conf
```

### :control_knobs: Deploy Network Policy on Master Node - Weave Net

```Bash
kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

### :robot: Join on Worker Nodes

```Bash
kubeadm join {master_ip} -- token {token} --discovery-token-ca-cert-hash {sha256}
```

### :tada: Finally, Verify on Master Node

Nodes:

```Bash
root@master01:~# kubectl get nodes
NAME       STATUS                     ROLES           AGE    VERSION
master01   Ready                      control-plane   2d2h   v1.24.10
node01     Ready,SchedulingDisabled   <none>          2d1h   v1.24.10
node02     Ready                      <none>          2d1h   v1.24.10
```

Pods:

```Bash
root@master01:~# kubectl get pods -A -o wide
NAMESPACE     NAME                               READY   STATUS    RESTARTS   AGE    IP                NODE       NOMINATED NODE   READINESS GATES
kube-system   coredns-57575c5f89-dhr9r           1/1     Running   0          2d2h   10.85.0.3         master01   <none>           <none>
kube-system   coredns-57575c5f89-vtbnl           1/1     Running   0          2d2h   10.85.0.2         master01   <none>           <none>
kube-system   etcd-master01                      1/1     Running   0          2d2h   192.168.1.238     master01   <none>           <none>
kube-system   kube-apiserver-master01            1/1     Running   0          2d2h   192.168.1.238     master01   <none>           <none>
kube-system   kube-controller-manager-master01   1/1     Running   0          2d2h   192.168.1.238     master01   <none>           <none>
kube-system   kube-proxy-86bwq                   1/1     Running   0          2d2h   192.168.1.238     master01   <none>           <none>
kube-system   kube-proxy-8zpzw                   1/1     Running   0          2d1h   192.168.103.107   node02     <none>           <none>
kube-system   kube-proxy-wm9fv                   1/1     Running   0          2d1h   192.168.1.237     node01     <none>           <none>
kube-system   kube-scheduler-master01            1/1     Running   0          2d2h   192.168.1.238     master01   <none>           <none>
kube-system   weave-net-kqzlv                    2/2     Running   0          42m    192.168.1.238     master01   <none>           <none>
kube-system   weave-net-lddm7                    2/2     Running   0          42m    192.168.103.107   node02     <none>           <none>
kube-system   weave-net-ttfp4                    2/2     Running   0          42m    192.168.1.237     node01     <none>           <none>
```

---

### Reference
- How to Install CRI-O on Ubuntu 22.04 / Ubuntu 20.04, https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-cri-o-on-ubuntu-22-04.html, 2023-02-07-Tue.
- How to Install Kubernetes on Ubuntu 22.04 / Ubuntu 20.04, https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/install-kubernetes-on-ubuntu-22-04.html, 2023-02-09-Thu.
- kubeadm init shows kubelet isn't running or healthy, https://stackoverflow.com/questions/52119985/kubeadm-init-shows-kubelet-isnt-running-or-healthy, 2023-02-03-Fri.
- Integrating Kubernetes via the Addon, https://www.weave.works/docs/net/latest/kubernetes/kube-addon/, 2023-02-09-Thu.
- Install and Set Up kubectl on Linux, https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-using-native-package-management, 2023-06-15-Thu.
