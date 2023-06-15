# Join to Another Kubernetes Cluster as a Worker Node

## Date

2023-03-15-Wednesday

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Delete a node from Old Kubernetes Cluster

### 1. Delete the Node on Master Node

```Bash
root@node238:~# kubectl drain node237
root@node238:~# kubectl delete node node237
```

### 2. Reset the Worker Node itself

```Bash
root@node237:~# kubeadm reset --cri-socket=/var/run/crio/crio.sock
```

## Join to the new Kubernetes Cluster

### Get Join Command in Master Node

```Bash
kubeadm token create --print-join-command
```

### 1. Join

```
root@node237:~# kubeadm join {server_ip} --token {token} --discovery-token-ca-cert-hash sha256:{hash}
[preflight] Running pre-flight checks
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[kubelet-start] Writing kubelet environment file with flags to file "/var/lib/kubelet/kubeadm-flags.env"
[kubelet-start] Starting the kubelet
[kubelet-start] Waiting for the kubelet to perform the TLS Bootstrap...

This node has joined the cluster:
* Certificate signing request was sent to apiserver and a response was received.
* The Kubelet was informed of the new secure connection details.

Run 'kubectl get nodes' on the control-plane to see this node join the cluster.
```

### :tada: Verify

```Bash
root@node87:~# k get nodes -o wide
NAME      STATUS   ROLES           AGE     VERSION    INTERNAL-IP     EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
node237   Ready    <none>          6m25s   v1.24.10   192.168.1.237   <none>        Ubuntu 22.04.1 LTS   5.15.0-60-generic   cri-o://1.24.4
node85    Ready    <none>          9d      v1.24.10   192.168.10.85   <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node86    Ready    <none>          9d      v1.24.10   192.168.10.86   <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node87    Ready    control-plane   9d      v1.24.10   192.168.10.87   <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node88    Ready    <none>          9d      v1.24.10   192.168.10.88   <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
```

---

### Reference
- Join Node Blog KR, https://sinsomi.tistory.com/entry/k8s-node-%EC%B6%94%EA%B0%80-master-node-worker-node-join, 2023-03-15-Wed.
- Join Command Kubernetes, https://stackoverflow.com/questions/51126164/how-do-i-find-the-join-command-for-kubeadm-on-the-master, 2023-06-15-Thu.
