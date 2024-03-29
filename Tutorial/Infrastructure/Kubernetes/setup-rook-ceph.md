# Install [Rook](https://rook.io/) [Ceph](https://ceph.com/en/) on Kubernetes

## Environment

Ubuntu 18.04.6 LTS -> Ubuntu 20.04.5 LTS -> Ubuntu 22.04.1 LTS

Kubernetes 1.26.0 (Policy deprecated in 1.25) -> Kubernetes 1.24.0 -> Kubernetes 1.24.10

## [Install Ceph](https://docs.ceph.com/en/latest/install/)

### Cephadm

Cephadm installs and manages a Ceph cluster that uses containers and systemd and is tightly integrated with the CLI and dashboard GUI.

- cephadm supports only Octopus and newer releases.
- cephadm is fully integrated with the orchestration API and fully supports the CLI and dashboard features that are used to manage cluster deployment.
- cephadm requires container support (in the form of Podman or Docker) and Python 3.

### Rook

Rook deploys and manages Ceph clusters running in Kubernetes, while also enabling management of storage resources and provisioning via Kubernetes APIs. We recommend Rook as the way to run Ceph in Kubernetes or to connect an existing Ceph storage cluster to Kubernetes.

- Rook supports only Nautilus and newer releases of Ceph.
- Rook is the preferred method for running Ceph on Kubernetes, or for connecting a Kubernetes cluster to an existing (external) Ceph cluster.
- Rook supports the orchestrator API. Management features in the CLI and dashboard are fully supported.

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

## 1.B. [Install Rook-Ceph using Krew](https://github.com/rook/kubectl-rook-ceph)

```Bash
kubectl krew install rook-ceph
```

## 2. Deploy File System

```Bash
kubectl apply -f rook/deploy/examples/filesystem.yaml
```

## 3. Deploy Storage Class

```Bash
kubectl apply -f rook/deploy/examples/csi/cephfs/storageclass.yaml
```

---

:tada: Verify

It takes some time to become 'Running' status.

```Bash
NAMESPACE     NAME                                               READY   STATUS      RESTARTS   AGE     IP              NODE     NOMINATED NODE   READINESS GATES
rook-ceph     csi-cephfsplugin-6nmwr                             3/3     Running     0          6m41s   192.168.10.88   node88   <none>           <none>
rook-ceph     csi-cephfsplugin-8lw8f                             3/3     Running     0          6m41s   192.168.10.85   node85   <none>           <none>
rook-ceph     csi-cephfsplugin-99sd8                             3/3     Running     0          6m41s   192.168.10.86   node86   <none>           <none>
rook-ceph     csi-cephfsplugin-provisioner-5c6c4c7785-j4jvr      6/6     Running     0          6m41s   10.40.0.1       node86   <none>           <none>
rook-ceph     csi-cephfsplugin-provisioner-5c6c4c7785-wlhhr      6/6     Running     0          6m40s   10.36.0.3       node88   <none>           <none>
rook-ceph     csi-rbdplugin-8wfwv                                3/3     Running     0          6m41s   192.168.10.85   node85   <none>           <none>
rook-ceph     csi-rbdplugin-bh56h                                3/3     Running     0          6m41s   192.168.10.86   node86   <none>           <none>
rook-ceph     csi-rbdplugin-pnjt5                                3/3     Running     0          6m41s   192.168.10.88   node88   <none>           <none>
rook-ceph     csi-rbdplugin-provisioner-7c756d9bd7-57fbd         6/6     Running     0          6m41s   10.36.0.2       node88   <none>           <none>
rook-ceph     csi-rbdplugin-provisioner-7c756d9bd7-9rp9k         6/6     Running     0          6m41s   10.40.0.3       node86   <none>           <none>
rook-ceph     rook-ceph-crashcollector-node85-7b64ff5b96-94tcs   1/1     Running     0          28s     10.32.0.5       node85   <none>           <none>
rook-ceph     rook-ceph-crashcollector-node86-6f69c98877-vh9fb   1/1     Running     0          43s     10.40.0.8       node86   <none>           <none>
rook-ceph     rook-ceph-crashcollector-node88-68957884d9-xnsgt   1/1     Running     0          27s     10.36.0.8       node88   <none>           <none>
rook-ceph     rook-ceph-mds-k8sfs-a-6b469c4c48-86wcl             1/1     Running     0          29s     10.32.0.4       node85   <none>           <none>
rook-ceph     rook-ceph-mds-k8sfs-b-67b8dbfdc6-s2x7j             1/1     Running     0          28s     10.36.0.5       node88   <none>           <none>
rook-ceph     rook-ceph-mgr-a-56fcf86d-h5h2q                     2/2     Running     0          77s     10.32.0.3       node85   <none>           <none>
rook-ceph     rook-ceph-mgr-b-8cc56bd7b-g52vr                    2/2     Running     0          76s     10.40.0.4       node86   <none>           <none>
rook-ceph     rook-ceph-mon-a-775fb5d7d7-t9cgv                   1/1     Running     0          8m10s   10.40.0.2       node86   <none>           <none>
rook-ceph     rook-ceph-mon-b-85c94c6595-xqt4p                   1/1     Running     0          4m22s   10.36.0.4       node88   <none>           <none>
rook-ceph     rook-ceph-mon-c-76b8868d66-m7hvk                   1/1     Running     0          4m3s    10.32.0.2       node85   <none>           <none>
rook-ceph     rook-ceph-operator-8485948986-5q48b                1/1     Running     0          10m     10.36.0.1       node88   <none>           <none>
rook-ceph     rook-ceph-osd-0-65745bf55d-8s249                   1/1     Running     0          45s     10.32.0.6       node85   <none>           <none>
rook-ceph     rook-ceph-osd-1-66b58b844-lhvkl                    1/1     Running     0          43s     10.40.0.7       node86   <none>           <none>
rook-ceph     rook-ceph-osd-2-cdd648d67-rk26w                    1/1     Running     0          43s     10.36.0.7       node88   <none>           <none>
rook-ceph     rook-ceph-osd-prepare-node85-8g5xr                 0/1     Completed   0          18s     10.32.0.7       node85   <none>           <none>
rook-ceph     rook-ceph-osd-prepare-node86-xmnkj                 0/1     Completed   0          15s     10.40.0.5       node86   <none>           <none>
rook-ceph     rook-ceph-osd-prepare-node88-wlm4v                 0/1     Completed   0          12s     10.36.0.6       node88   <none>           <none>
```

---

### [Issue](https://github.com/helm/helm/issues/11287)

> <img width="1168" alt="Screenshot 2023-01-30 at 2 16 07 PM" src="https://user-images.githubusercontent.com/20737479/215393142-f37257ee-b10f-4266-88e3-bd145155dcd6.png">

With Kubernetes 1.24.0:

> <img width="622" alt="Screenshot 2023-01-31 at 11 07 12 AM" src="https://user-images.githubusercontent.com/20737479/215641540-5980ac86-1197-46b0-9fb9-59911b4ff131.png">

Installing rook-ceph with Krew works, but the pods are not properly deployed.

---

### Reference
- Rook, https://rook.io/, 2023-01-20-Fri.
- Ceph, https://ceph.com/en/, 2023-03-02-Thu.
- Install Ceph, https://docs.ceph.com/en/latest/install/, 2023-03-02-Thu.
- Rook GitHub, https://github.com/rook/rook, 2023-01-20-Fri.
- Rook Prerequisites, https://rook.io/docs/rook/v1.10/Getting-Started/Prerequisites/prerequisites/, 2023-01-20-Fri.
- 쿠버네티스 가상스토리지(Ceph) 설치, https://danawalab.github.io/kubernetes/2020/01/28/kubernetes-rook-ceph.html, 2023-01-20-Fri.
- Ceph Quickstart, https://rook.io/docs/rook/v1.9/quickstart.html, 2023-01-25-Wed.
- kubectl-rook-ceph, https://github.com/rook/kubectl-rook-ceph, 2023-01-30-Mon.
- Install partprobe, https://command-not-found.com/partprobe, 2023-03-03-Fri.
