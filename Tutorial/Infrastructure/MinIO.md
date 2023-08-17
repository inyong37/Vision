# [MinIO](https://min.io/)

MinIO is high-performance Kubernetes-native object storage that is compatible with the S3 API. 

## Date

2023-05-08-Monday.

2023-08-17-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Setup MinIO

### 1. Install MinIO

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230816201730.0.0_amd64.deb -O minio.deb
# wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230504214430.0.0_amd64.deb -O minio.deb
sudo dpkg -i minio.deb
```

Or

A. Download MinIO Client for Linux AMD64

```Bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
```

B. Download MinIO Server for Linux AMD64

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
```

### 2. Configure User and Password

```Bash
export MINIO_ROOT_USER={user}
export MINIO_ROOT_PASSWORD={password}
```

### 3. Launch the MinIO Server

Make a Directory for MinIO

```Bash
mkdir ~/{minio_workspace}
```

```Bash
minio server ~/{minio_workspace} --console-address :9090
```

### :tada: Connect to the MinIO Server via a Browser

`http://127.0.0.1:9090` or `{ip_address}:9090`

### (Optional) Install the MinIO Client

```Bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/mc
mc alias set local http://127.0.0.1:9000 {user} {password}
mc admin info local
```

---

## Setting Expiration

### Prerequisite

Alias:

```Bash
mc alias set {alias_name} http://{ip_address}:9000 {id} {password}
# mc alias set myminio http://192.168.0.2:9000 minioadmin minioadmin
```

### Set a Rule

```Bash
mc ilm rule add --expire-days {days} {alias_name}/{bucket_name}
# mc ilm rule add --expire-days 10 myminio/test-bucket
```

---

## Topologies

### Single-Node Single-Drive (SNSD or "Standalone")

Local development and evaluation with no/limited reliability

### Single-Node Multi-Drive (SNMD or “Standalone Multi-Drive”)

Workloads with lower performance, scale, and capacity requirements

Drive-level reliability with configurable tolerance for loss of up to 1/2 all drives

Evaluation of multi-drive topologies and failover behavior.

### Multi-Node Multi-Drive (MNMD or “Distributed”)

Enterprise-grade high-performance object storage

Multi Node/Drive level reliability with configurable tolerance for loss of up to 1/2 all nodes/drives

Primary storage for AI/ML, Distributed Query, Analytics, and other Data Lake components

Scalable for Petabyte+ workloads - both storage capacity and performance

---

## Object Retention Modes

MinIO implements the following S3 Object Locking Modes:

### GOVERNANCE Mode

Prevents any operation that would mutate or modify the object or its locking settings by non-privileged users.

Users with the `s3:BypassGovernanceRetention` permission on the bucket or object can modify the object or its locking settings.

MinIO lifts the lock automatically after the configured retention rule duration has passed.

### COMPLIANCE Mode

Prevents any operation that would mutate or modify the object or its locking settings.

No MinIO user can modify the object or its settings, including the MinIO root user.

MinIO lifts the lock automatically after the configured retention rule duration has passed.

---

## Hardware Checklist

### CPU

Sufficient CPU cores to achieve performance goals for hashing (for example, for healing) and encryption

MinIO recommends Dual Intel® Xeon® Scalable Gold CPUs (minimum 16 cores per socket) or any CPU with AVX512 instructions

### RAM

Sufficient RAM to achieve performance goals based on the number of drives and anticipated concurrent requests (see the formula and reference table).

MinIO recommends a minimum of 128GB of memory per node for best performance.

### Node

Minimum of four nodes dedicated to object storage.

For containers or Kubernetes in virtualized environments, MinIO requires four distinct physical nodes. Colocating multiple high-performance softwares on the same nodes can result in resource contention and reduced overall performance.

### Drive

SATA/SAS drives for balanced capacity-to-performance, NVMe SSDs for high-performance.

MinIO recommends a minimum of 8 drives per server.

Use the same type of drive (NVMe, SSD, or HDD) with the same capacity across all nodes in the deployment.

### Network

25GbE Network as a baseline, 100GbE Network for high performance

---

MinIO for
- [Kubernetes](https://min.io/product/kubernetes)
- [Amazon Elastic Kubernetes Service](https://min.io/product/multicloud-elastic-kubernetes-service)
- [Microsoft Azure Kubernetes Service](https://min.io/product/multicloud-azure-kubernetes-service)
- [Google Kubernetes Engine](https://min.io/product/multicloud-google-kubernetes-service)
- [VMware Tanzur](https://min.io/product/private-cloud-vmware-tanzu)
- [Red Hat OpenShift Container Platform](https://min.io/product/private-cloud-red-hat-openshift)
- [SUSE Rancher](https://min.io/product/multicloud-suse-rancher)

---

### Reference
- MinIO, https://min.io/, 2023-05-26-Fri.
- MinIO Kubernetes, https://min.io/product/kubernetes, 2023-05-26-Fri.
- MinIO for Amazon Elastic Kubernetes Service, https://min.io/product/multicloud-elastic-kubernetes-service, 2023-05-26-Fri.
- MinIO for Microsoft Azure Kubernetes Service, https://min.io/product/multicloud-azure-kubernetes-service, 2023-05-26-Fri.
- MinIO for Google Kubernetes Engine, https://min.io/product/multicloud-google-kubernetes-service, 2023-05-26-Fri.
- MinIO for VMware Tanzu, https://min.io/product/private-cloud-vmware-tanzu, 2023-05-26-Fri.
- MinIO for Red Hat OpenShift Container Platform, https://min.io/product/private-cloud-red-hat-openshift, 2023-05-26-Fri.
- MinIO for SUSE Rancher, https://min.io/product/multicloud-suse-rancher, 2023-05-26-Fri.
- MinIO, https://min.io/docs/minio/linux/index.html, 2023-05-08-Mon.
- MinIO Install and Deploy, https://min.io/docs/minio/linux/operations/installation.html, 2023-05-23-Tue.
- MinIO Deploy SNSD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-single-drive.html, 2023-05-23-Tue.
- MinIO Deploy SNMD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-multi-drive.html, 2023-05-23-Tue.
- MinIO Deploy MNMD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-multi-node-multi-drive.html, 2023-05-23-Tue.
- MinIO Hardware Checklist, https://min.io/docs/minio/linux/operations/checklists/hardware.html#minio-hardware-checklisthttps://min.io/docs/minio/linux/operations/checklists/hardware.html, 2023-05-23-Tue.
- MinIO automatic delete Stackoverflow, https://stackoverflow.com/questions/69031738/minio-is-it-possible-to-set-automatic-deletion-from-bucket-of-the-object-after-t, 2023-06-13-Tue.
- MinIO alias set, https://min.io/docs/minio/linux/reference/minio-mc/mc-alias-set.html, 2023-06-13-Tue.
- MinIO ilm rule add, https://min.io/docs/minio/linux/reference/deprecated/mc-ilm-add.html#command-mc.ilm.add, 2023-06-13-Tue.
- MinIO Object Management, https://min.io/docs/minio/linux/administration/object-management/object-lifecycle-management.html, 2023-06-13-Tue.
