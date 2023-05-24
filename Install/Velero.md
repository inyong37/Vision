# Velero

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
./velero install \
--provider aws \
--plugins velero/velero-plugin-for-aws:v1.0.0. \
--bucket backup-testing-environment \
--secret-file ./credentials-velero \
--use-volume-snapshots=false \
--backup-location-config region=minio,s3ForcePathStyle="true",s3Url=http://{ip_address}:9000
```

Output:

```Bash
Velero is installed! ⛵ Use 'kubectl logs deployment/velero -n velero' to view the status.
```

---

### Reference
- Kubernetes Backup Velero Blog KR, https://teamsmiley.github.io/2020/10/10/kubernetes-backup-velero/, 2023-05-24-Wed.
- MinIO WebUI Blog KR, https://www.bearpooh.com/130, 2023-05-24-Wed.
- Kubernetes Velero Install IBM KR, https://www.ibm.com/docs/ko/spp/10.1.12?topic=resources-kubernetes-installing-configuring-velero, 2023-05-24-Wed.
- MinIO Access and Secret Key Stackoverflow, https://stackoverflow.com/questions/67285745/how-can-i-get-minio-access-and-secret-key, 2023-05-24-Wed.
