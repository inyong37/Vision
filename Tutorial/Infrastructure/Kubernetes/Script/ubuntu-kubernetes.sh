#!/usr/bin/bash

# Author: In Yong Hwang (inyong1020@gmail.com)
# Date: 2023-06-15-Thursday.
# Description: This shell script is to set Kubernetes on Ubuntu Machine.
# Command: "sh ubuntu-kubernetes.sh" with root authority.

echo "========== SETTING KUBERNETES ON UBUNTU 22.04 LTS =========="

# SET SWAP OFF
echo "========== SWAP OFF =========="
swapoff -a
sed -i '/swap/s/^/#/' /etc/fstab

# DISABLE FIREWALL
systemctl stop firewalld
systemctl disable firewalld

# SET NETWORK
echo "========== SET NETWORK =========="
mkdir -p /etc/modules-load.d

cat <<EOF | tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF

modprobe overlay
modprobe br_netfilter

mkdir -p /etc/sysctl.d

cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-iptables  = 1
net.bridge.bridge-nf-call-ip6tables = 1
net.ipv4.ip_forward                 = 1
EOF

sysctl --system

# INSTALL CONTAINER RUNTIME INTERFACE
echo "========== INSTALL CRI-O 1.24 =========="
export OS_VERSION=xUbuntu_22.04
export CRIO_VERSION=1.24
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS_VERSION/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/libcontainers-archive-keyring.gpg
curl -fsSL https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$CRIO_VERSION/$OS_VERSION/Release.key | sudo gpg --dearmor -o /usr/share/keyrings/libcontainers-crio-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/libcontainers-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable/$OS_VERSION/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable.list
echo "deb [signed-by=/usr/share/keyrings/libcontainers-crio-archive-keyring.gpg] https://download.opensuse.org/repositories/devel:/kubic:/libcontainers:/stable:/cri-o:/$CRIO_VERSION/$OS_VERSION/ /" | sudo tee /etc/apt/sources.list.d/devel:kubic:libcontainers:stable:cri-o:$CRIO_VERSION.list
apt update && apt install -y cri-o cri-o-runc
systemctl daemon-reload
systemctl enable crio
systemctl start crio

# INSTALL KUBERNETES
echo "========== INSTALL KUBERNETS =========="
apt update && apt install -y apt-transport-https ca-certificates curl
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt update && apt install -y kubeadm=1.24.10-00 kubectl=1.24.10-00 kubelet=1.24.10-00
apt-mark hold kubelet kubeadm kubectl

# FINISHED
echo "========== FINISHED ==========="
echo "kubeadm init --pod-network-cidr <ip_address>/16 --apiserver-advertise-address=<master_node_ip_address>"
echo "kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml"
