# coredns status is on `ContainerCreating` with an error

## Date

2023-03-16-Thursday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

Re-building Kubernetes Cluster, errors occured:

```Bash
NAMESPACE     NAME                              READY   STATUS              RESTARTS      AGE   IP                NODE      NOMINATED NODE   READINESS GATES
kube-system   coredns-57575c5f89-mh8ld          0/1     ContainerCreating   0             5s    <none>            node238   <none>           <none>
kube-system   coredns-57575c5f89-sstwj          0/1     ContainerCreating   0             88s   <none>            node238   <none>           <none>
```

```Bash
  Warning  FailedCreatePodSandBox  5s    kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-85swg_kube-system_0a70418c-f266-4bdb-b999-a93810f6a32c_0(7f125f3470e4cf3d61fd4bd8992fd01ef3591e15d1d3e1a7da3c4f7f792d8c33): error adding pod kube-system_coredns-57575c5f89-85swg to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/7f125f3470e4cf3d61fd4bd8992fd01ef3591e15d1d3e1a7da3c4f7f792d8c33": dial tcp 127.0.0.1:6784: connect: connection refused
```

## [Solution](https://velog.io/@dame_sol/%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A5%BC-%EB%AA%BB%EA%B0%80%EC%A0%B8%EC%98%A8%EB%8B%A4)

### Delete images

```Bash
crictl images
```

```Bash
crictl rmi fce326961ae2d 0849bf5f3ef4e 4b0f3887b66e7 d6ccf30c8566e b1ef1dbb09ca5 6270bb605e12e
```

### Restart services

```Bash
systemctl stop kubelet
systemctl stop crio
rm -rf /var/lib/containers/
systemctl start crio
systemctl start kubelet
```

## Verify - Rebuilt Kubernetes cluster; doesn't work.

```Bash
root@node238:~# k get nodes -o wide
NAME      STATUS   ROLES           AGE     VERSION    INTERNAL-IP       EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
node107   Ready    control-plane   65s     v1.24.10   192.168.103.107   <none>        Ubuntu 22.04.1 LTS   5.15.0-60-generic   cri-o://1.24.4
node237   Ready    <none>          2m17s   v1.24.10   192.168.1.237     <none>        Ubuntu 22.04.1 LTS   5.15.0-60-generic   cri-o://1.24.4
node238   Ready    control-plane   5m53s   v1.24.10   192.168.1.238     <none>        Ubuntu 22.04.1 LTS   5.15.0-60-generic   cri-o://1.24.4
node85    Ready    <none>          2m13s   v1.24.10   192.168.10.85     <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node86    Ready    <none>          2m12s   v1.24.10   192.168.10.86     <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node87    Ready    control-plane   2m9s    v1.24.10   192.168.10.87     <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
node88    Ready    <none>          2m11s   v1.24.10   192.168.10.88     <none>        Ubuntu 22.04.2 LTS   5.15.0-67-generic   cri-o://1.24.4
root@node238:~# k get pods -A -o wide
NAMESPACE     NAME                              READY   STATUS              RESTARTS        AGE     IP                NODE      NOMINATED NODE   READINESS GATES
kube-system   coredns-57575c5f89-27ggv          0/1     ContainerCreating   0               5m42s   <none>            node238   <none>           <none>
kube-system   coredns-57575c5f89-vkfxm          0/1     ContainerCreating   0               5m42s   <none>            node238   <none>           <none>
kube-system   etcd-node107                      1/1     Running             0               61s     192.168.103.107   node107   <none>           <none>
kube-system   etcd-node238                      1/1     Running             10              5m56s   192.168.1.238     node238   <none>           <none>
kube-system   etcd-node87                       1/1     Running             8               2m15s   192.168.10.87     node87    <none>           <none>
kube-system   kube-apiserver-node107            1/1     Running             8               57s     192.168.103.107   node107   <none>           <none>
kube-system   kube-apiserver-node238            1/1     Running             8               5m56s   192.168.1.238     node238   <none>           <none>
kube-system   kube-apiserver-node87             1/1     Running             14 (2m4s ago)   2m15s   192.168.10.87     node87    <none>           <none>
kube-system   kube-controller-manager-node238   1/1     Running             9 (2m4s ago)    5m56s   192.168.1.238     node238   <none>           <none>
kube-system   kube-controller-manager-node87    1/1     Running             12              54s     192.168.10.87     node87    <none>           <none>
kube-system   kube-proxy-96lc6                  1/1     Running             0               2m19s   192.168.10.86     node86    <none>           <none>
kube-system   kube-proxy-dl9md                  1/1     Running             0               2m18s   192.168.10.88     node88    <none>           <none>
kube-system   kube-proxy-gkv4d                  1/1     Running             0               2m20s   192.168.10.85     node85    <none>           <none>
kube-system   kube-proxy-hmgbw                  1/1     Running             0               72s     192.168.103.107   node107   <none>           <none>
kube-system   kube-proxy-pm9jl                  1/1     Running             0               2m16s   192.168.10.87     node87    <none>           <none>
kube-system   kube-proxy-q7vxp                  1/1     Running             0               2m24s   192.168.1.237     node237   <none>           <none>
kube-system   kube-proxy-rmtgc                  1/1     Running             0               5m42s   192.168.1.238     node238   <none>           <none>
kube-system   kube-scheduler-node107            1/1     Running             8               64s     192.168.103.107   node107   <none>           <none>
kube-system   kube-scheduler-node238            1/1     Running             9 (2m4s ago)    5m55s   192.168.1.238     node238   <none>           <none>
kube-system   kube-scheduler-node87             1/1     Running             12              2m14s   192.168.10.87     node87    <none>           <none>
root@node238:~# k describe pod coredns-57575c5f89-27ggv
Error from server (NotFound): pods "coredns-57575c5f89-27ggv" not found
root@node238:~# k describe pod coredns-57575c5f89-27ggv -n kube-system
Name:                 coredns-57575c5f89-27ggv
Namespace:            kube-system
Priority:             2000000000
Priority Class Name:  system-cluster-critical
Node:                 node238/192.168.1.238
Start Time:           Thu, 16 Mar 2023 08:13:31 +0000
Labels:               k8s-app=kube-dns
                      pod-template-hash=57575c5f89
Annotations:          <none>
Status:               Pending
IP:
IPs:                  <none>
Controlled By:        ReplicaSet/coredns-57575c5f89
Containers:
  coredns:
    Container ID:
    Image:         registry.k8s.io/coredns/coredns:v1.8.6
    Image ID:
    Ports:         53/UDP, 53/TCP, 9153/TCP
    Host Ports:    0/UDP, 0/TCP, 0/TCP
    Args:
      -conf
      /etc/coredns/Corefile
    State:          Waiting
      Reason:       ContainerCreating
    Ready:          False
    Restart Count:  0
    Limits:
      memory:  170Mi
    Requests:
      cpu:        100m
      memory:     70Mi
    Liveness:     http-get http://:8080/health delay=60s timeout=5s period=10s #success=1 #failure=5
    Readiness:    http-get http://:8181/ready delay=0s timeout=1s period=10s #success=1 #failure=3
    Environment:  <none>
    Mounts:
      /etc/coredns from config-volume (ro)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-zkg4n (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  config-volume:
    Type:      ConfigMap (a volume populated by a ConfigMap)
    Name:      coredns
    Optional:  false
  kube-api-access-zkg4n:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              kubernetes.io/os=linux
Tolerations:                 CriticalAddonsOnly op=Exists
                             node-role.kubernetes.io/control-plane:NoSchedule
                             node-role.kubernetes.io/master:NoSchedule
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason                  Age                  From               Message
  ----     ------                  ----                 ----               -------
  Normal   Scheduled               5m57s                default-scheduler  Successfully assigned kube-system/coredns-57575c5f89-27ggv to node238
  Warning  FailedCreatePodSandBox  5m57s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(3623d5ad5b9173c9586b64a4034206566cee6769bbe077f64123cedfee5e500c): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/3623d5ad5b9173c9586b64a4034206566cee6769bbe077f64123cedfee5e500c": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  5m45s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(8dcb2805f24dab5923b34bddf04cead6bdd7cac92818bd079b7d7e88d4e48c62): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/8dcb2805f24dab5923b34bddf04cead6bdd7cac92818bd079b7d7e88d4e48c62": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  5m32s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(fcbace7988cd8606c7089b4dc416c5a68d3ea73c80c4b4ee053dc39d5bcd995c): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/fcbace7988cd8606c7089b4dc416c5a68d3ea73c80c4b4ee053dc39d5bcd995c": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  5m19s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(c648458a21c4873af93f21f46104222ca1ee1ede40ffbaa987f9188ebe3283f6): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/c648458a21c4873af93f21f46104222ca1ee1ede40ffbaa987f9188ebe3283f6": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  5m4s                 kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(a4352bb464c95e358a8186730a81a9ba74c6e424f4ff6d984b87646bde90920d): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/a4352bb464c95e358a8186730a81a9ba74c6e424f4ff6d984b87646bde90920d": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  4m53s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(e4068502577a072626ad17f73cf05cb896b0d7bd4b88cf49abbb7691b9196ef4): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/e4068502577a072626ad17f73cf05cb896b0d7bd4b88cf49abbb7691b9196ef4": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  4m40s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(c6e422185a885c220ce6e3549af9ce77a99d80914f615d795240da89184ee578): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/c6e422185a885c220ce6e3549af9ce77a99d80914f615d795240da89184ee578": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  4m29s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(054f09d13efe6a4f39e9bde30b87fa880aa4313c03a86d760fe138847f85fd36): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/054f09d13efe6a4f39e9bde30b87fa880aa4313c03a86d760fe138847f85fd36": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  4m14s                kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(15155722ddab6483c7b393b8f71021e0bc4e191d527b45854eaa5a356674b461): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/15155722ddab6483c7b393b8f71021e0bc4e191d527b45854eaa5a356674b461": dial tcp 127.0.0.1:6784: connect: connection refused
  Warning  FailedCreatePodSandBox  35s (x17 over 4m3s)  kubelet            (combined from similar events): Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(0b968e26505bd990f57092aea53d1900bf7098598ab0d3ad86bb41ef46e02e19): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/0b968e26505bd990f57092aea53d1900bf7098598ab0d3ad86bb41ef46e02e19": dial tcp 127.0.0.1:6784: connect: connection refused
```

### Reference
- Coredns Error Blog KR, https://velog.io/@dame_sol/%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A5%BC-%EB%AA%BB%EA%B0%80%EC%A0%B8%EC%98%A8%EB%8B%A4, 2023-03-16-Thu.
- Coredns Error, https://www.bytefusion.de/2021/01/08/openshift-okd-causes-image-layer-not-known-problems/, 2023-03-16-Thu.
