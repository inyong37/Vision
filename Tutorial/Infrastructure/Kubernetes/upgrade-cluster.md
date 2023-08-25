# [Upgrade a Cluster](https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/)

## Date

2023-08-25-Friday.

## Environment

* Ubuntu 22.04.2 LTS
  * kubeadm 1.27.3-00
  * kubelet 1.27.3-00
  * kubectl 1.27.3-00
 
## [Upgrade Control Planes](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

1. `apt-mark unhold kubeadm && apt-get update && apt-get install -y kubeadm='1.27.4-00' && apt-mark hold kubeadm`
2. `kubeadm version`
3. `kubeadm upgrade plan`
4. `kubeadm upgrade apply v1.27.4`
5. `apt-mark unhold kubelet kubectl && apt-get update && apt-get install -y kubelet='1.27.4-00' kubectl='1.27.4-00' && apt-mark hold kubelet kubectl`
6. `systemctl daemon-reload`
7. `systemctl restart kubelet`

## [Upgrade Workers on Linux](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/)

1. `apt-mark unhold kubeadm && apt-get update && apt-get install -y kubeadm='1.27.4-00' && apt-mark hold kubeadm`
2. `kubeadm upgrade node`
3. `apt-mark unhold kubelet kubectl && apt-get update && apt-get install -y kubelet='1.27.4-00' kubectl='1.27.4-00' && apt-mark hold kubelet kubectl`
4. `systemctl daemon-reload`
5. `systemctl restart kubelet`

---

### Reference
- Upgrade A Cluster, https://kubernetes.io/docs/tasks/administer-cluster/cluster-upgrade/, 2023-08-25-Fri.
- Upgrading kubeadm cluster, https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/, 2023-08-25-Fri.
- Upgrading Linux nodes, https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/upgrading-linux-nodes/, 2023-08-25-Fri.
