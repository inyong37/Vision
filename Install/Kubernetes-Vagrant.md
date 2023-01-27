# Kubernetes Cluster with Vagrant

## A. Ubuntu 20.04.4 LTS

:key: All commands are executed on sudo.

### 1. Install Vagrant

```bash
$ wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
$ echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
$ sudo apt update && sudo apt install vagrant
```

### 2. Install Virtualbox-6.1

a. Download VirtualBox with GUI:

https://www.virtualbox.org/wiki/Download_Old_Builds_6_1

b. Download VirtualBox with CUI:

```Bash
$ wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
$ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
$ sudo add-apt-repository "deb http://download.virtualbox.org/virtualbox/debian focal contrib"
$ apt update && apt install virtualbox-6.1
```

Start vagrant with virtualbox:

```Bash
$ vagrant up --provider virtualbox
```

ssh:

```Bash
$ vagrant ssh {vm_name} # kubemaster, kubenode01, kubenode01
```

### 3. Forwarding IPv4 and letting iptables see bridged traffic

```Bash
$ cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

```Bash
$ modprobe overlay
$ modprobe br_netfilter
```

sysctl params required by setup, params persist across reboots: 

```Bash
$ cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF 
```

Apply sysctl params without reboot:

```Bash
$ sysctl --system

```

Verify that the br_netfilter, overlay modules are loaded by running below instructions:

```Bash
$ lsmod | grep br_netfilter
$ lsmod | grep overlay
```

Verify that the net.bridge.bridge-nf-call-iptables, net.bridge.bridge-nf-call-ip6tables, net.ipv4.ip_forward system variables are set to 1 in your sysctl config by running below instruction:

```Bash
$ sysctl net.bridge.bridge-nf-call-iptables net.bridge.bridge-nf-call-ip6tables net.ipv4.ip_forward
```

### 4. Install Container Runtime - Docker

:key: [If you want to use KubeVirt, then you have to install containerd or CRI for Container Runtime.](Kubernetes-KubeVirt.md)

```Bash
$ apt-get update && apt-get install -y \
  apt-transport-https ca-certificates curl software-properties-common gnupg2
```

```Bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
```

```Bash
$ add-apt-repository \
  "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) \
  stable"
```

```Bash
$ apt-get update && apt-get install -y \
  containerd.io=1.2.13-2 \
  docker-ce=5:19.03.11~3-0~ubuntu-$(lsb_release -cs) \
  docker-ce-cli=5:19.03.11~3-0~ubuntu-$(lsb_release -cs)
```

```Bash
$ cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF
```

```Bash
$ mkdir -p /etc/systemd/system/docker.service.d
```

```Bash
$ systemctl daemon-reload
$ systemctl restart docker
```

```Bash
$ systemctl enable docker
```

### 5. Install kubeadm/kubelet/kubectl

:key: In releases older than Debian 12 and Ubuntu 22.04, /etc/apt/keyrings does not exist by default. You can create this directory if you need to, making it world-readable but writeable only by admins.

Update the apt package index and install packages needed to use the Kubernetes apt repository:

```Bash
$ apt-get update
$ apt-get install -y apt-transport-https ca-certificates curl
```

Download the Google Cloud public signing key:

```Bash
$ curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

Add the Kubernetes apt repository:

```Bash
$ echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
```

Update apt package index, install kubelet, kubeadm and kubectl, and pin their version:

```Bash
$ apt-get update
$ apt-get install -y kubelet kubeadm kubectl
$ apt-mark hold kubelet kubeadm kubectl
```

### 6-1. Control Pane - master node

```bash
$ kubeadm init --pod-network-cidr <ip_address>/16 --apiserver-advertise-address=<master_node_ip_address>
```

To start using your cluster, you need to run the following as a regular user:

```bash
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

:key: Alternatively, if you are the root user, you can run:

```bash
$ export KUBECONFIG=/etc/kubernetes/admin.conf
```

[Install Weave Net](https://www.weave.works/docs/net/latest/kubernetes/kube-addon/)

```Bash
$ kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
```

### 6-2. Worker node

You can join any number of worker nodes by running the following on each as root:

```Bash
$ kubeadm join --token <token> <control-plane-host>:<control-plane-port> --discovery-token-ca-cert-hash sha256:<hash>
```

### 6-3. Check it on master node

```Bash
$ kubectl get nodes
```
<img width="383" alt="Screenshot 2023-01-18 at 1 54 19 PM" src="https://user-images.githubusercontent.com/20737479/213087369-fff2a1f1-0130-44ba-b7e6-a95fd3d454fb.png">

## :construction: B. macOS with Apple Silicon

### 1. Install Vagrant

```zsh
$ brew install hashicorp/tap/hashicorp-vagrant
```

### 2. Install VMware Fusion

https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-22H2

```zsh
$ ln -s /Applications/VMWare\ Fusion\ Tech\ Preview.app /Applications/VMWare\ Fusion.app
```

```zsh
sudo /opt/vagrant-vmware-desktop/bin/vagrant-vmware-utility api -debug
```

Verify running:

```zsh
$ sudo lsof -i -P | grep LISTEN | grep 'vagrant-v'
```

Or start to run:

```zsh
$ sudo launchctl load -w /Library/LaunchDaemons/com.vagrant.vagrant-vmware-utility.plist
```

```zsh
$ vagrant plugin install vagrant-vmware-desktop
```

---

### Reference
- Certified Kubernetes Administrator (CKA) with Practice Test, https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/, 2023-01-18-Wed.
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-18-Wed.
- Download VirtualBox (Old Builds): VirtualBox 6.1, https://www.virtualbox.org/wiki/Download_Old_Builds_6_1, 2023-01-18-Wed.
- Container Runtimes, https://kubernetes.io/docs/setup/production-environment/container-runtimes/, 2023-01-17-Tue.
- Install Docker Engine on Ubuntu, https://docs.docker.com/engine/install/ubuntu/, 2023-01-17-Tue.
- Runtime Container, https://kubernetes.io/id/docs/setup/production-environment/container-runtimes/, 2023-01-17-Tue.
- Installing kubeadm, https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/, 2023-01-18-Wed.
- Setting up Vagrant 2.3.0 for Virtual Machine Management in Mac ( Apple M1 Pro), https://medium.com/geekculture/setting-up-vagrant-2-3-0-for-virtual-machine-management-in-mac-apple-m1-pro-9dc4ec9036db, 2023-01-16-Mon.
- VMware Fusion Public Tech Preview 22H2, https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-22H2, 2023-01-16-Mon.
- Integrating Kubernetes via the Addon, https://www.weave.works/docs/net/latest/kubernetes/kube-addon/, 2023-01-18-Wed.
- How to Install VirtualBox 6.1 on Ubuntu 20.04, https://tecadmin.net/install-virtualbox-on-ubuntu-20-04/, 2023-01-19-Thu.
- Vagrant Blog KR, https://blog.juho.kim/posts/2021-10-01_Vagrant/, 2023-01-27-Fri.
