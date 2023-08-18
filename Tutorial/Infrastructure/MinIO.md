# [MinIO](https://min.io/)

MinIO is high-performance Kubernetes-native object storage that is compatible with the S3 API. 

## Date

2023-05-08-Monday.

2023-08-17-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Setup MinIO

### 1. [Install MinIO Server](https://dl.min.io/server/minio/release/)

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230816201730.0.0_amd64.deb -O minio.deb
# wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230504214430.0.0_amd64.deb -O minio.deb
sudo dpkg -i minio.deb
```

Alternative:

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
```

### 2. [Install the MinIO Client](https://dl.min.io/client/mc/release/)

```Bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
sudo mv mc /usr/local/bin/mc
```

### 3. Alias

```Bash
mc alias set {alias_name} http://{ip_address}:9000 {id} {password}
# mc alias set myminio http://192.168.0.2:9000 minioadmin minioadmin
```

Option for local alias:

```
mc alias set {local_minio} http://127.0.0.1:9000 {user} {password}
mc admin info {local_minio}
```

### 4. Configure User and Password

```Bash
export MINIO_ROOT_USER={user}
export MINIO_ROOT_PASSWORD={password}
```

### 5. Launch the MinIO Server

Make a Directory for MinIO

```Bash
mkdir ~/{minio_workspace}
```

```Bash
minio server ~/{minio_workspace} --console-address :9090
```

### :tada: Connect to the MinIO Server via a Browser

`http://127.0.0.1:9090` or `{ip_address}:9090`

---

[List Alias](https://min.io/docs/minio/linux/reference/minio-mc/mc-alias-list.html): `mc alias list`

## Setting Expiration

Prerequisite: Alias

### Set a Rule

```Bash
mc ilm rule add --expire-days {days} {alias_name}/{bucket_name}
# mc ilm rule add --expire-days 10 myminio/test-bucket
```

---

## [Upgrade a MinIO Deployment](https://min.io/docs/minio/linux/operations/install-deploy-manage/upgrade-minio-deployment.html)

MinIO uses an update-then-restart methodology for upgrading a deployment to a newer release:

1. Update the MinIO binary on all hosts with the newer release
2. Restart the deployment using `mc admin service restart`

This procedure does not require taking downtime and is non-disruptive to ongoing operations.

MinIO's upgrade-then-restart procedure does not require taking downtime or scheduling a maintenance period. MinIO restarts are fast, such that restarting all server processes in parallel typically completes in a few seconds. MinIO operations are atomic and strictly consistent, such that applications using MinIO or S3 SDKs can rely on the built-in transparent retry without further client-side logic. This ensures upgrades are non-disruptive to ongoing operations.

"Rolling" or serial "one-at-a-time" upgrade methods do not provide any advantage over the recommended "parallel" procedure, and can introduce unnecessary complexity to the upgrade procedure. For virtualized environments which require rolling updates, you should amend the recommend procedure as follows:

1. Update the MinIO Binary in the virtual machine or container one at a time.
2. Restart the MinIO deployment using `mc admin service restart`.
3. Update the virtual machine/container configuration to use the matching newer MinIO image.
4. Perform the rolling restart of each machine/container with the updated image.

### A. Update `systemctl`-Managed MinIO Deployments

1. Update the MinIO Binary on Each Node - DEB (Debian/Ubuntu):

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230816201730.0.0_amd64.deb -O minio.deb
sudo dpkg -i minio.deb
```

2. Restart the Deployment:

```Bash
mc admin service restart {alias}
```

3. Validate the Update:

```Bash
mc admin info {alias}
```

4. Update MinIO Client

```Bash
mc update
```

### B. Update Non-System Managed MinIO Deployments

The following command updates a MinIO deployment with the specified alias to the latest stable release:

```Bash
mc admin update {alias}
```

You should upgrade your `mc` binary to match or closely follow the MinIO server release. You can use the `mc update` command to update the binary to the latest stable release:

```Bash
mc update
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
- MinIO Client Release, https://dl.min.io/client/mc/release/, 2023-08-17-Thu.
- MinIO Server Release, https://dl.min.io/server/minio/release/, 2023-08-17-Thu.
- Upgrade, https://min.io/docs/minio/linux/operations/install-deploy-manage/upgrade-minio-deployment.html, 2023-08-18-Fri.
- List aliases, https://min.io/docs/minio/linux/reference/minio-mc/mc-alias-list.html, 2023-08-18-Fri.
