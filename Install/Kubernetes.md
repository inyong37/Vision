# Kubernetes Cluster with Vagrant

## A. Ubuntu 20.04.4 LTS

### 1. Forwarding IPv4 and letting iptables see bridged traffic

```Bash
$ cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
overlay
br_netfilter
EOF
```

```Bash
$ sudo modprobe overlay
$ sudo modprobe br_netfilter
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
$ sudo sysctl --system

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

### 2. Install Vagrant

```bash
$ wget -O- https://apt.releases.hashicorp.com/gpg | gpg --dearmor | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg
$ echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
$ sudo apt update && sudo apt install vagrant
```

```Bash
$ vagrant up
```

### 3. Install Virtualbox-6.1

https://www.virtualbox.org/wiki/Download_Old_Builds_6_1

### 4. Install Container Runtime - Docker

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
$ sudo systemctl enable docker
```

---

### Reference
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-18-Wed.
- Download VirtualBox (Old Builds): VirtualBox 6.1, https://www.virtualbox.org/wiki/Download_Old_Builds_6_1, 2023-01-18-Wed.
- Container Runtimes, https://kubernetes.io/docs/setup/production-environment/container-runtimes/, 2023-01-17-Tue.
- Install Docker Engine on Ubuntu, https://docs.docker.com/engine/install/ubuntu/, 2023-01-17-Tue.
- Runtime Container, https://kubernetes.io/id/docs/setup/production-environment/container-runtimes/, 2023-01-17-Tue.
