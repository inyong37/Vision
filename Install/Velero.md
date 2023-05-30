# [Velero](https://velero.io/)

Velero is an open source tool to safely backup and restore, perform disaster recovery, and migrate Kubernetes cluster resources and persistent volumes.

## Date

2023-05-24-Wednesday.

## Environment

- Ubuntu 22.04.2 LTS
  - Kubernetes 1.24.10

## Install Velero on Kubernets

### Download

```Bash
curl -fsSL -o velero-v1.9.0-linux-amd64.tar.gz https://github.com/vmware-tanzu/velero/releases/download/v1.9.0/velero-v1.9.0-linux-amd64.tar.gz
```

```Bash
tar -xvf velero-v1.9.0-linux-amd64.tar.gz
```

```Bash
mv velero-v1.9.0-linux-amd64/velero /bin/
```

Check:

```Bash
velero
```

### Configure Access Key

```Bash
cd ~/velero-v1.9.0-linux-amd64
```

```Bash
cat <<EOF > credentials-velero
[default]
aws_access_key_id={id_from_minio}
aws_secret_access_key={password_from_minio}
EOF
```

### Install

```Bash
velero install \
--provider aws \
--plugins velero/velero-plugin-for-aws:v1.2.1 \
--bucket {bucket_name} \
--secret-file {access_key_file} \
--use-volume-snapshots=false \
--backup-location-config region=minio,s3ForcePathStyle="true",s3Url=http://{ip_address}:9000
```

Output:

```Bash
Velero is installed! ⛵ Use 'kubectl logs deployment/velero -n velero' to view the status.
```

---

## [Quick Start Evaluation Install with MinIO](https://velero.io/docs/v1.11/contributions/minio/)

### Prerequisites

- Access to a Kubernetes cluster, version 1.7 or later. Note: File System Backup support requires Kubernetes version 1.10 or later, or an earlier version with the mount propagation feature enabled. File System Backup support is not required for this example, but may be of interest later. See File System Backup.
- A DNS server on the cluster
- kubectl installed
- Sufficient disk space to store backups in Minio. You will need sufficient disk space available to handle any backups plus at least 1GB additional. Minio will not operate if less than 1GB of free disk space is available.

### Download

```Bash
curl -fsSL -o velero-v1.9.0-linux-amd64.tar.gz https://github.com/vmware-tanzu/velero/releases/download/v1.9.0/velero-v1.9.0-linux-amd64.tar.gz
```

### Unzip

```Bash
tar -xvf velero-v1.9.0-linux-amd64.tar.gz
```

### Setup Binary

```Bash
cp ~/velero-v1.9.0-linux-amd64/velero /bin/
```

### Configure MinIO

`vim ~/velero-v1.9.0-linux-amd64/credentials-velero`

```Bash
[default]
aws_access_key_id = minio
aws_secret_access_key = minio123
```

### Deploy MinIO

```Bash
kubectl apply -f ~/velero-v1.9.0-linux-amd64/examples/minio/00-minio-deployment.yaml
```

### Install Velero

```Bash
velero install \
    --provider aws \
    --plugins velero/velero-plugin-for-aws:v1.2.1 \
    --bucket velero \
    --secret-file ./credentials-velero \
    --use-volume-snapshots=false \
    --backup-location-config region=minio,s3ForcePathStyle="true",s3Url=http://minio.velero.svc:9000
```

### Deploy Nginx

```Bash
kubectl apply -f ~/velero-v1.9.0-linux-amd64/examples/nginx-app/base.yaml
```

### Check Deployments

```Bash
kubectl get deployments -l component=velero --namespace=velero
---
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
velero   1/1     1            1           44s
```

```Bash
kubectl get deployments --namespace=nginx-example
---
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/2     2            2           37s
```

### Backup

```Bash
velero backup create nginx-backup --selector app=nginx
# velero schedule create nginx-daily --schedule="@daily" --selector app=nginx
```

```Bash
velero backup get
---
NAME           STATUS      ERRORS   WARNINGS   CREATED                         EXPIRES   STORAGE LOCATION   SELECTOR
nginx-backup   Completed   0        0          2023-05-26 05:32:29 +0000 UTC   29d       default            app=nginx
```

### Simulate a Disaster

```Bash
kubectl delete namespace nginx-example
```

```Bash
kubectl get deployments --namespace=nginx-example
kubectl get services --namespace=nginx-example
kubectl get namespace/nginx-example
---
No resources found in nginx-example namespace.
No resources found in nginx-example namespace.
Error from server (NotFound): namespaces "nginx-example" not found
```

### Restore

```Bash
velero restore create --from-backup nginx-backup
---
Restore request "nginx-backup-20230526050649" submitted successfully.
Run `velero restore describe nginx-backup-20230526050649` or `velero restore logs nginx-backup-20230526050649` for more details.
```

```Bash
velero restore get
---
NAME                          BACKUP         STATUS      STARTED                         COMPLETED                       ERRORS   WARNINGS   CREATED                         SELECTOR
nginx-backup-20230526053306   nginx-backup   Completed   2023-05-26 05:33:06 +0000 UTC   2023-05-26 05:33:07 +0000 UTC   0        0          2023-05-26 05:33:06 +0000 UTC   <none>
```

### Clean up

```Bash
velero backup delete BACKUP_NAME
```

```Bash
kubectl delete namespace/velero clusterrolebinding/velero
kubectl delete crds -l component=velero
kubectl delete -f examples/nginx-app/base.yaml
```

### Uninstall

```Bash
velero uninstall
---
You are about to uninstall Velero.
Are you sure you want to continue (Y/N)? y
Waiting for velero namespace "velero" to be deleted
..........................................................................
Velero namespace "velero" deleted
Velero uninstalled ⛵
```

---

### Reference
- Velero, https://velero.io/, 2023-05-26-Fri.
- Kubernetes Backup Velero Blog KR, https://teamsmiley.github.io/2020/10/10/kubernetes-backup-velero/, 2023-05-24-Wed.
- MinIO WebUI Blog KR, https://www.bearpooh.com/130, 2023-05-24-Wed.
- Kubernetes Velero Install IBM KR, https://www.ibm.com/docs/ko/spp/10.1.12?topic=resources-kubernetes-installing-configuring-velero, 2023-05-24-Wed.
- MinIO Access and Secret Key Stackoverflow, https://stackoverflow.com/questions/67285745/how-can-i-get-minio-access-and-secret-key, 2023-05-24-Wed.
- MinIO Client Blog KR, https://www.lesstif.com/system-admin/minio-client-76709916.html, 2023-05-24-Wed.
- Quick Start Evaluation Install with MinIO, https://velero.io/docs/v1.11/contributions/minio/, 2023-05-26-Fri.
- cron, https://pkg.go.dev/github.com/robfig/cron, 2023-05-26-Fri.
