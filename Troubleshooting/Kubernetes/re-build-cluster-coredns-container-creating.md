# coredns pods' states are in `ContainerCreating` after re-building Kubernetes cluster

## Date

2023-03-20-Monday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

WeaveNet 2.8.1

## Problem

While re-building Kubernetes cluster, the coredns pods are stucked in `ContainerCreating` status:

```Bash
root@node238:~# k get pods -A -o wide
NAMESPACE     NAME                              READY   STATUS              RESTARTS         AGE     IP                NODE      NOMINATED NODE   READINESS GATES
kube-system   coredns-57575c5f89-27ggv          0/1     ContainerCreating   0                3d17h   <none>            node238   <none>           <none>
kube-system   coredns-57575c5f89-vkfxm          0/1     ContainerCreating   0                3d17h   <none>            node238   <none>           <none>
```

with

```Bash
Events:
  Type     Reason                  Age                       From     Message
  ----     ------                  ----                      ----     -------
  Warning  FailedCreatePodSandBox  4m50s (x7499 over 3d17h)  kubelet  (combined from similar events): Failed to create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_coredns-57575c5f89-27ggv_kube-system_18e19958-8373-484e-ab22-54be3249d543_0(fc31be6cabf6307322dca030b2dfdb4cac3115a5b3a2ce0957014ea839e1d27d): error adding pod kube-system_coredns-57575c5f89-27ggv to CNI network "weave": plugin type="weave-net" name="weave" failed (add): unable to allocate IP address: Post "http://127.0.0.1:6784/ip/fc31be6cabf6307322dca030b2dfdb4cac3115a5b3a2ce0957014ea839e1d27d": dial tcp 127.0.0.1:6784: connect: connection refused
```

## [Solution](https://clarkshim.tistory.com/262)

Deploy CNI pod

```Bash
root@node238:~# kubectl apply -f https://github.com/weaveworks/weave/releases/download/v2.8.1/weave-daemonset-k8s.yaml
serviceaccount/weave-net created
clusterrole.rbac.authorization.k8s.io/weave-net created
clusterrolebinding.rbac.authorization.k8s.io/weave-net created
role.rbac.authorization.k8s.io/weave-net created
rolebinding.rbac.authorization.k8s.io/weave-net created
daemonset.apps/weave-net created
```

### :tada: Verify

```Bash
root@node238:~# k get pods -A -o wide
NAMESPACE     NAME                              READY   STATUS            RESTARTS         AGE     IP                NODE      NOMINATED NODE   READINESS GATES
kube-system   coredns-57575c5f89-27ggv          1/1     Running           0                3d17h   10.40.0.1         node238   <none>           <none>
kube-system   coredns-57575c5f89-vkfxm          1/1     Running           0                3d17h   10.40.0.2         node238   <none>           <none>
```

---

### Reference
- Coredns Error Blog KR, https://clarkshim.tistory.com/262, 2023-03-20-Mon.
