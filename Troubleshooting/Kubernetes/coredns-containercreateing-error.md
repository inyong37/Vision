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

### Reference
- Coredns Error Blog KR, https://velog.io/@dame_sol/%EC%9D%B4%EB%AF%B8%EC%A7%80%EB%A5%BC-%EB%AA%BB%EA%B0%80%EC%A0%B8%EC%98%A8%EB%8B%A4, 2023-03-16-Thu.
- Coredns Error, https://www.bytefusion.de/2021/01/08/openshift-okd-causes-image-layer-not-known-problems/, 2023-03-16-Thu.
