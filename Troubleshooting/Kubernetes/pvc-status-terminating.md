# Fix pvc status is stucked in terminating

## Date

2023-03-13-Monday.

## Environment

Ubuntu 22.04.2 LTS

Kubernetes 1.24.10

## Problem

I tried to delete pvc which is not working properly.

```Bash
root@node87:~# k get pv,pvc
NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                  STORAGECLASS   REASON   AGE
persistentvolume/pvc-e2d6b552-6939-42ac-adb2-95a1537f7d7c   1Gi        RWO            Delete           Bound    default/cephfs-pvc     rook-cephfs             6d17h
persistentvolume/task-pv-volume                             15Gi       RWO            Retain           Bound    default/disk-windows   hostpath                6d18h

NAME                                 STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/cephfs-pvc     Bound    pvc-e2d6b552-6939-42ac-adb2-95a1537f7d7c   1Gi        RWO            rook-cephfs    6d17h
persistentvolumeclaim/disk-windows   Bound    task-pv-volume                             15Gi       RWO            hostpath       6d18h
root@node87:~# k delete pvc cephfs-pvc
persistentvolumeclaim "cephfs-pvc" deleted
```

However, after deleting command, the pvc status is stucked in 'terminating'.

```Bash
root@node87:~# k get pv,pvc
NAME                                                        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                  STORAGECLASS   REASON   AGE
persistentvolume/pvc-e2d6b552-6939-42ac-adb2-95a1537f7d7c   1Gi        RWO            Delete           Bound    default/cephfs-pvc     rook-cephfs             6d17h
persistentvolume/task-pv-volume                             15Gi       RWO            Retain           Bound    default/disk-windows   hostpath                6d18h

NAME                                 STATUS        VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
persistentvolumeclaim/cephfs-pvc     Terminating   pvc-e2d6b552-6939-42ac-adb2-95a1537f7d7c   1Gi        RWO            rook-cephfs    6d17h
persistentvolumeclaim/disk-windows   Bound         task-pv-volume                             15Gi       RWO            hostpath       6d18h
```

## [Solution](https://veducate.co.uk/kubernetes-pvc-terminating/)

```Bash
kubectl patch pvc {PVC_NAME} -p '{"metadata":{"finalizers":null}}'
```

### :tada: Verify

```Bash
root@node87:~# kubectl patch pvc cephfs-pvc -p '{"metadata":{"finalizers":null}}'
persistentvolumeclaim/cephfs-pvc patched
root@node87:~# k get pvc
NAME           STATUS   VOLUME           CAPACITY   ACCESS MODES   STORAGECLASS   AGE
disk-windows   Bound    task-pv-volume   15Gi       RWO            hostpath       6d18h
```

---

### Reference
- How To Fix A PVC Stuck in Terminating Status in Kubernetes: Troubleshooting Guide, https://veducate.co.uk/kubernetes-pvc-terminating/, 2023-03-13-Mon.
