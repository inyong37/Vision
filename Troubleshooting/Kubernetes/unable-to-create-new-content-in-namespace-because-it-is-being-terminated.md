# unable to create new content in namespace rook-ceph because it is being terminated

## Date

2023-02-28-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

I tried to re-make rook-ceph, an error occured:

```Bash
root@node85:~/rook/deploy/examples# k create -f operator.yaml
Error from server (Forbidden): error when creating "operator.yaml": configmaps "rook-ceph-operator-config" is forbidden: unable to create new content in namespace rook-ceph because it is being terminated
Error from server (Forbidden): error when creating "operator.yaml": deployments.apps "rook-ceph-operator" is forbidden: unable to create new content in namespace rook-ceph because it is being terminated
```

```Bash
root@node85:~/rook/deploy/examples# k get namespaces
NAME              STATUS        AGE
cdi               Active        14d
default           Active        14d
kube-node-lease   Active        14d
kube-public       Active        14d
kube-system       Active        14d
kubevirt          Active        14d
rook-ceph         Terminating   14d
```

## [Solution](https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/#troubleshooting)

```Bash
root@node85:~/rook/deploy/examples# kubectl -n rook-ceph get cephcluster
NAME        DATADIRHOSTPATH   MONCOUNT   AGE   PHASE      MESSAGE                    HEALTH        EXTERNAL
rook-ceph   /var/lib/rook     3          14d   Deleting   Deleting the CephCluster   HEALTH_WARN
root@node85:~/rook/deploy/examples# for CRD in $(kubectl get crd -n rook-ceph | awk '/ceph.rook.io/ {print $1}'); do
    kubectl get -n rook-ceph "$CRD" -o name | \
    xargs -I {} kubectl patch -n rook-ceph {} --type merge -p '{"metadata":{"finalizers": []}}'
done
cephblockpool.ceph.rook.io/replicapool patched
cephcluster.ceph.rook.io/rook-ceph patched
cephfilesystem.ceph.rook.io/myfs patched
```

```Bash
root@node85:~/rook/deploy/examples# kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -n rook-ceph
NAME                                DATA   AGE
configmap/rook-ceph-mon-endpoints   4      14d
NAME                   TYPE                 DATA   AGE
secret/rook-ceph-mon   kubernetes.io/rook   4      14d
Warning: kubevirt.io/v1 VirtualMachineInstancePresets is now deprecated and will be removed in v2.
root@node85:~/rook/deploy/examples# kubectl -n rook-ceph patch configmap rook-ceph-mon-endpoints --type merge -p '{"metadata":{"finalizers": []}}'
kubectl -n rook-ceph patch secrets rook-ceph-mon --type merge -p '{"metadata":{"finalizers": []}}'
configmap/rook-ceph-mon-endpoints patched
secret/rook-ceph-mon patched
root@node85:~/rook/deploy/examples# kubectl api-resources --verbs=list --namespaced -o name   | xargs -n 1 kubectl get --show-kind --ignore-not-found -n rook-ceph
Warning: kubevirt.io/v1 VirtualMachineInstancePresets is now deprecated and will be removed in v2.
```

---

### Reference
- Remove namespace IBM, https://www.ibm.com/docs/en/cloud-private/3.2.0?topic=console-namespace-is-stuck-in-terminating-state, 2023-02-28-Tue.
- Remove Rook-Ceph, https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/#troubleshooting, 2023-02-28-Tue.
