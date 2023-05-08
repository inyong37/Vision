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

### Reference
- MinIO, https://min.io/docs/minio/linux/index.html, 2023-05-08-Mon.
