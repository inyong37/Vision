# Pod is stucked in terminating state.

## Date

2023-03-15-Wednesday.

## Environment

Ubuntu 22.04.2 LTS

Kubernetes 1.24.10

## Problem

```Bash
root@node87:~/rook/deploy/examples# k get pods -A
NAMESPACE     NAME                             READY   STATUS        RESTARTS   AGE
default       csicephfs-demo-pod               0/1     Terminating   1          8d
kube-system   coredns-57575c5f89-88qsl         1/1     Running       3          9d
kube-system   coredns-57575c5f89-nxrlw         1/1     Running       3          9d
kube-system   etcd-node87                      1/1     Running       3          9d
kube-system   kube-apiserver-node87            1/1     Running       3          9d
kube-system   kube-controller-manager-node87   1/1     Running       3          9d
kube-system   kube-proxy-4krrs                 1/1     Running       3          9d
kube-system   kube-proxy-78xr4                 1/1     Running       1          9d
kube-system   kube-proxy-94xkj                 1/1     Running       1          9d
kube-system   kube-proxy-9jmmd                 1/1     Running       1          9d
kube-system   kube-scheduler-node87            1/1     Running       3          9d
kube-system   weave-net-28tf2                  2/2     Running       2          9d
kube-system   weave-net-28w6r                  2/2     Running       8          9d
kube-system   weave-net-c4jww                  2/2     Running       2          9d
kube-system   weave-net-knjqf                  2/2     Running       2          9d
```

## [Solution](https://stackoverflow.com/questions/35453792/pods-stuck-in-terminating-status)

```Bash
root@node87:~/rook/deploy/examples# k delete pod csicephfs-demo-pod --grace-period=0 --force
warning: Immediate deletion does not wait for confirmation that the running resource has been terminated. The resource may continue to run on the cluster indefinitely.
pod "csicephfs-demo-pod" force deleted
```

### :tada: Verify

```Bash
root@node87:~/rook/deploy/examples# k get pods -A
NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE
kube-system   coredns-57575c5f89-88qsl         1/1     Running   3          9d
kube-system   coredns-57575c5f89-nxrlw         1/1     Running   3          9d
kube-system   etcd-node87                      1/1     Running   3          9d
kube-system   kube-apiserver-node87            1/1     Running   3          9d
kube-system   kube-controller-manager-node87   1/1     Running   3          9d
kube-system   kube-proxy-4krrs                 1/1     Running   3          9d
kube-system   kube-proxy-78xr4                 1/1     Running   1          9d
kube-system   kube-proxy-94xkj                 1/1     Running   1          9d
kube-system   kube-proxy-9jmmd                 1/1     Running   1          9d
kube-system   kube-scheduler-node87            1/1     Running   3          9d
kube-system   weave-net-28tf2                  2/2     Running   2          9d
kube-system   weave-net-28w6r                  2/2     Running   8          9d
kube-system   weave-net-c4jww                  2/2     Running   2          9d
kube-system   weave-net-knjqf                  2/2     Running   2          9d
```

---

### Reference
- Pods stuck in Terminating status Stackoverflow, https://stackoverflow.com/questions/35453792/pods-stuck-in-terminating-status, 2023-03-15-Wed.
