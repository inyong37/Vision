# Install [Rook](https://rook.io/) [Ceph](https://ceph.com/en/) on Kubernetes

## Environment

Ubuntu 18.04.6 LTS -> Ubuntu 20.04.5 LTS -> Ubuntu 22.04.1 LTS

Kubernetes 1.26.0 (Policy deprecated in 1.25) -> Kubernetes 1.24.0 -> Kubernetes 1.24.10

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

## 1. [Install Rook-Ceph](https://rook.io/docs/rook/v1.9/quickstart.html)

```Bash
$ git clone --single-branch --branch v1.9.2 https://github.com/rook/rook.git
$ cd rook/deploy/examples
$ kubectl apply -f crds.yaml -f common.yaml -f operator.yaml
$ kubectl apply -f cluster.yaml
```

## 2. Deploy File System

```Bash
kubectl apply -f rook/deploy/examples/filesystem.yaml
```

## 3. Deploy Storage Class

```Bash
kubectl apply -f rook/deploy/examples/csi/cephfs/storageclass.yaml
```

### [Issue](https://github.com/helm/helm/issues/11287)

> <img width="1168" alt="Screenshot 2023-01-30 at 2 16 07 PM" src="https://user-images.githubusercontent.com/20737479/215393142-f37257ee-b10f-4266-88e3-bd145155dcd6.png">

With Kubernetes 1.24.0:

> <img width="622" alt="Screenshot 2023-01-31 at 11 07 12 AM" src="https://user-images.githubusercontent.com/20737479/215641540-5980ac86-1197-46b0-9fb9-59911b4ff131.png">

Installing rook-ceph with Krew works, but the pods are not properly deployed.

### [Cleanup](https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/)

Delete the Block and File artifacts:

```Bash
# kubectl delete -f ../wordpress.yaml
# kubectl delete -f ../mysql.yaml
kubectl delete -n rook-ceph cephblockpool replicapool
kubectl delete storageclass rook-ceph-block
kubectl delete -f csi/cephfs/kube-registry.yaml
kubectl delete storageclass csi-cephfs
```

Delete the `CephCluster` CR:

```Bash
kubectl -n rook-ceph delete cephcluster rook-ceph
```

Delete the Operator and related Resources:

```Bash
kubectl delete -f operator.yaml
kubectl delete -f common.yaml
kubectl delete -f psp.yaml
kubectl delete -f crds.yaml
```

## Option B. [Install using Krew](https://github.com/rook/kubectl-rook-ceph)

```Bash
kubectl krew install rook-ceph
```

---

### Reference
- Rook, https://rook.io/, 2023-01-20-Fri.
- Ceph, https://ceph.com/en/, 2023-03-02-Thu.
- Rook GitHub, https://github.com/rook/rook, 2023-01-20-Fri.
- Rook Prerequisites, https://rook.io/docs/rook/v1.10/Getting-Started/Prerequisites/prerequisites/, 2023-01-20-Fri.
- 쿠버네티스 가상스토리지(Ceph) 설치, https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html, 2023-01-20-Fri.
- Ceph Quickstart, https://rook.io/docs/rook/v1.9/quickstart.html, 2023-01-25-Wed.
- Cleanup, https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/, 2023-01-25-Wed.
- kubectl-rook-ceph, https://github.com/rook/kubectl-rook-ceph, 2023-01-30-Mon.
