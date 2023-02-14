# Install [Rook](https://rook.io/) Ceph on Kubernetes

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

## A. [Rook Ceph 1.9 Quickstart](https://rook.io/docs/rook/v1.9/quickstart.html)

```Bash
$ git clone --single-branch --branch v1.9.2 https://github.com/rook/rook.git
$ cd rook/deploy/examples
$ kubectl apply -f crds.yaml -f common.yaml -f operator.yaml
$ kubectl apply -f cluster.yaml
```

### [Issue](https://github.com/helm/helm/issues/11287)

> <img width="1168" alt="Screenshot 2023-01-30 at 2 16 07 PM" src="https://user-images.githubusercontent.com/20737479/215393142-f37257ee-b10f-4266-88e3-bd145155dcd6.png">

With Kubernetes 1.24.0:

> <img width="622" alt="Screenshot 2023-01-31 at 11 07 12 AM" src="https://user-images.githubusercontent.com/20737479/215641540-5980ac86-1197-46b0-9fb9-59911b4ff131.png">

Installing rook-ceph with Krew works, but the pods are not properly deployed.

## [Cleanup](https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/)

Delete the Block and File artifacts:

```Bash
$ # kubectl delete -f ../wordpress.yaml
$ # kubectl delete -f ../mysql.yaml
$ kubectl delete -n rook-ceph cephblockpool replicapool
$ kubectl delete storageclass rook-ceph-block
$ kubectl delete -f csi/cephfs/kube-registry.yaml
$ kubectl delete storageclass csi-cephfs
```

Delete the `CephCluster` CR:

```Bash
$ kubectl -n rook-ceph delete cephcluster rook-ceph
```

Delete the Operator and related Resources:

```Bash
$ kubectl delete -f operator.yaml
$ kubectl delete -f common.yaml
$ kubectl delete -f psp.yaml
$ kubectl delete -f crds.yaml
```

## B. [Install using Krew](https://github.com/rook/kubectl-rook-ceph)

```Bash
$ kubectl krew install rook-ceph
```

## :tada:

```Bash
rook-ceph     csi-cephfsplugin-6nqvl                             3/3     Running     0             8m31s
rook-ceph     csi-cephfsplugin-fqg49                             3/3     Running     0             8m31s
rook-ceph     csi-cephfsplugin-provisioner-5c6c4c7785-6bmzn      6/6     Running     0             8m31s
rook-ceph     csi-cephfsplugin-provisioner-5c6c4c7785-mqwh9      6/6     Running     0             8m31s
rook-ceph     csi-cephfsplugin-xdmnn                             3/3     Running     0             8m31s
rook-ceph     csi-rbdplugin-6pvtj                                3/3     Running     0             8m31s
rook-ceph     csi-rbdplugin-provisioner-7c756d9bd7-8v7cf         6/6     Running     0             8m31s
rook-ceph     csi-rbdplugin-provisioner-7c756d9bd7-m7zwt         6/6     Running     0             8m31s
rook-ceph     csi-rbdplugin-rjsp8                                3/3     Running     0             8m31s
rook-ceph     csi-rbdplugin-wpwbk                                3/3     Running     0             8m31s
rook-ceph     rook-ceph-crashcollector-node86-6f69c98877-785cl   1/1     Running     0             3m41s
rook-ceph     rook-ceph-crashcollector-node87-865f998898-59zjm   1/1     Running     0             3m49s
rook-ceph     rook-ceph-crashcollector-node88-65669f77f5-vd48r   1/1     Running     0             3m15s
rook-ceph     rook-ceph-mgr-a-6b6f9444f-qw2bg                    2/2     Running     0             3m49s
rook-ceph     rook-ceph-mgr-b-69768df8f7-lvk6r                   2/2     Running     0             3m48s
rook-ceph     rook-ceph-mon-a-77545f988f-qnphr                   1/1     Running     0             9m45s
rook-ceph     rook-ceph-mon-b-7c5c48bb4d-kvqpn                   1/1     Running     0             8m48s
rook-ceph     rook-ceph-mon-c-7699d5c9f5-7ckcb                   1/1     Running     0             6m11s
rook-ceph     rook-ceph-operator-8485948986-2v6k6                1/1     Running     0             12m
rook-ceph     rook-ceph-osd-0-7cc7d95975-99d96                   1/1     Running     0             3m15s
rook-ceph     rook-ceph-osd-prepare-node86-g4crh                 0/1     Completed   0             2m55s
rook-ceph     rook-ceph-osd-prepare-node87-zgxvx                 0/1     Completed   0             2m52s
rook-ceph     rook-ceph-osd-prepare-node88-dv8j5                 0/1     Completed   0             2m48s
```

---

### Reference
- Rook, https://rook.io/, 2023-01-20-Fri.
- Rook GitHub, https://github.com/rook/rook, 2023-01-20-Fri.
- Rook Prerequisites, https://rook.io/docs/rook/v1.10/Getting-Started/Prerequisites/prerequisites/, 2023-01-20-Fri.
- 쿠버네티스 가상스토리지(Ceph) 설치, https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html, 2023-01-20-Fri.
- Ceph Quickstart, https://rook.io/docs/rook/v1.9/quickstart.html, 2023-01-25-Wed.
- Cleanup, https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/, 2023-01-25-Wed.
- kubectl-rook-ceph, https://github.com/rook/kubectl-rook-ceph, 2023-01-30-Mon.
