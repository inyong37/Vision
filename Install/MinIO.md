# Setup MinIO

## Date

2023-05-08-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Setup MinIO

### 1. Install MinIO

```Bash
wget https://dl.min.io/server/minio/release/linux-amd64/archive/minio_20230504214430.0.0_amd64.deb -O minio.deb
sudo dpkg -i minio.deb
```

### 2. Configure User and Password

```Bash
export MINIO_ROOT_USER={user}
export MINIO_ROOT_PASSWORD={password}
```

### 3. Launch the MinIO Server

```Bash
mkdir ~/minio
minio server ~/minio --console-address :9090
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

### Reference
- MinIO, https://min.io/docs/minio/linux/index.html, 2023-05-08-Mon.
- MinIO Install and Deploy, https://min.io/docs/minio/linux/operations/installation.html, 2023-05-23-Tue.
- MinIO Deploy SNSD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-single-drive.html, 2023-05-23-Tue.
- MinIO Deploy SNMD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-single-node-multi-drive.html, 2023-05-23-Tue.
- MinIO Deploy MNMD, https://min.io/docs/minio/linux/operations/install-deploy-manage/deploy-minio-multi-node-multi-drive.html, 2023-05-23-Tue.
- MinIO Hardware Checklist, https://min.io/docs/minio/linux/operations/checklists/hardware.html#minio-hardware-checklisthttps://min.io/docs/minio/linux/operations/checklists/hardware.html, 2023-05-23-Tue.
