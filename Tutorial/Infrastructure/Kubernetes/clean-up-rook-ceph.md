# Clean-up Rook-Ceph

## Date

2023-03-20-Monday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

Rook-Ceph 1.9


## [Clean-Up](https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/)

### Delete the block and file artifacts

```Bash
# kubectl delete -f ../wordpress.yaml
# kubectl delete -f ../mysql.yaml
kubectl delete -n rook-ceph cephblockpool replicapool
kubectl delete storageclass rook-ceph-block
kubectl delete -f csi/cephfs/kube-registry.yaml
kubectl delete storageclass csi-cephfs
```

### Delete the `CephCluster` CR

```Bash
kubectl -n rook-ceph delete cephcluster rook-ceph
```

### Delete the Operator and related Resources

```Bash
kubectl delete -f operator.yaml
kubectl delete -f common.yaml
kubectl delete -f psp.yaml
kubectl delete -f crds.yaml
```

### Delete each disk on worker nodes

```Bash
DISK="/dev/sdX"

# Zap the disk to a fresh, usable state (zap-all is important, b/c MBR has to be clean)
sgdisk --zap-all $DISK

# Wipe a large portion of the beginning of the disk to remove more LVM metadata that may be present
dd if=/dev/zero of="$DISK" bs=1M count=100 oflag=direct,dsync

# SSDs may be better cleaned with blkdiscard instead of dd
blkdiscard $DISK

# Inform the OS of partition table changes
partprobe $DISK
```

---

### Reference
- Clean-up Rook-Ceph, https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/, 2023-01-25-Wed.
