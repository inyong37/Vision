# Setup a Load Balancer for Multiple Master Nodes

## Date

2023-03-16-Thursday.

## Environment

Ubuntu 22.04.2 LTS

## Setup

All commands are executed on the root authority.

### Install `HAproxy`

```Bash
apt update && apt install -y haproxy
```

### Backup default configuration

```Bash
cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg-org
```

### Edit configuration

```Bash
vim /etc/haproxy/haproxy.cfg
```

as below:

```cfg
frontend kubernetes-master-lb
bind 0.0.0.0:6443
option tcplog
mode tcp
default_backend kubernetes-master-nodes
backend kubernetes-master-nodes
mode tcp
balance roundrobin
option tcp-check
option tcplog
server {k8s-master1} {10.1.10.101}:6443 check
server {k8s-master2} {10.1.10.102}:6443 check
server {k8s-master3} {10.1.10.103}:6443 check
```

Put hostnames of master nodes and ip addresses in `{}`s.

### Apply it

```Bash
systemctl restart haproxy
```

```Bash
systemctl enable haproxy
```

## Setup on all nodes

### Add hosts on all nodes

```Bash
vim /etc/hosts
```

as below:

```yaml
{10.1.10.100} {k8s-lb}
{10.1.10.101} {k8s-master1}
{10.1.10.102} {k8s-master2}
{10.1.10.103} {k8s-master3}
{10.1.10.104} {k8s-worker1}
{10.1.10.105} {k8s-worker2}
{10.1.10.106} {k8s-worker3}
```

Edit ip addresses and hostnames of load balancer, master nodes and worker nodes.

### Verify it

```Bash
ping k8s-worker4
```

---

### Reference
- Setup Kubernetes Cluster Blog KR, https://tech.cloudmt.co.kr/2022/06/27/k8s-highly-available-clusters/, 2023-03-16-Thu.
