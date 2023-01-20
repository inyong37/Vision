# Install [Rook](https://rook.io/) Ceph on Kubernetes (1.26.0) and Ubuntu (18.04.6 LTS)

## [Requirement](https://rook.io/docs/rook/v1.10/Getting-Started/Prerequisites/prerequisites/)

Rook can be installed on any existing Kubernetes cluster as long as it meets the minimum version and Rook is granted the required privileges (see below for more information).

- Kubernetes v1.19 or higher is supported for the Ceph operator.
- Architectures supported are amd64 / x86_64 and arm64.
- Ceph Prerequisites: In order to configure the Ceph storage cluster, at least one of these local storage types is required:
  - Raw devices (no partitions or formatted filesystems)
  - Raw partitions (no formatted filesystem)
  - LVM Logical Volumes (no formatted filesystem)
  - Persistent Volumes available from a storage class in block mode

### LVM package

Ceph OSDs have a dependency on LVM in the following scenarios:
- OSDs are created on raw devices or partitions
- If encryption is enabled (encryptedDevice: "true" in the cluster CR)
- A metadata device is specified

LVM is not required for OSDs in these scenarios:
- Creating OSDs on PVCs using the storageClassDeviceSets

```bash
$ apt-get install -y lvm2
```

If you will be creating volumes from a Ceph shared file system (CephFS), the recommended minimum kernel version is 4.17. If you have a kernel version less than 4.17, the requested PVC sizes will not be enforced. Storage quotas will only be enforced on newer kernels.

---

### Reference
- Rook, https://rook.io/, 2023-01-20-Fri.
- Rook GitHub, https://github.com/rook/rook, 2023-01-20-Fri.
- Rook Prerequisites, https://rook.io/docs/rook/v1.10/Getting-Started/Prerequisites/prerequisites/, 2023-01-20-Fri.
- 쿠버네티스 가상스토리지(Ceph) 설치, https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html, 2023-01-20-Fri.

