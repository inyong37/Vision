# [Velero](https://velero.io/)

Velero is an open source tool to safely backup and restore, perform disaster recovery, and migrate Kubernetes cluster resources and persistent volumes.

## Date

2023-05-24-Wednesday.

## Environment

- Ubuntu 22.04.2 LTS
  - Kubernetes 1.24.10
- Ubuntu 20.04.1 LTS
  - Kubernetes 1.23.3 

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

## [Autocompletion](https://velero.io/docs/main/customize-installation/#enabling-shell-autocompletion)

```Bash
echo 'source <(velero completion bash)' >>~/.bashrc
velero completion bash >/etc/bash_completion.d/velero
```

### Alias

```Bash
echo 'alias v=velero' >>~/.bashrc
echo 'complete -F __start_velero v' >>~/.bashrc
```

---

## [Restic](https://github.com/restic/restic) | [Restic Integration](https://velero.io/docs/v1.9/restic/)

Restic is a backup program. It supports the three major operating systems (Linux, macOS, Windows) and a few smaller ones (FreeBSD, OpenBSD).

Velero has support for backing up and restoring Kubernetes volumes using a free open-source backup tool called restic. This support is considered beta quality. Velero has always allowed you to take snapshots of persistent volumes as part of your backups if you're using one of the supported cloud providers' block storage offerings (Amazon EBS Volumes, Azure Managed Disks, Google Persistent Disks). It also provides a plugin model that enables anyone to implement additional object and block storage backends, outside the main Velero repository.

If you need a volume snapshot plugin for your storage platform, or if you're using EFS, AzureFile, NFS, emptyDir, local, or any other volume type that doesn't have a native snapshot concept, Restic might be for you.

Restic is not tied to a specific storage platform, which means that this integration also paves the way for future work to enable cross-volume-type data migrations. :key: hostPath volumes are not supported, but the local volume type is supported.

###  To back up

Velero supports two approaches of discovering pod volumes that need to be backed  up using Restic:

- Opt-in approach: Where every pod containing a volume to be backed up using Restic must be annotated with the volume's name.
- Opt-out approach: Where all pod volumes are backed up using Restic, with the ability to opt-out any volumes that should not be backed up.

### Using the opt-out approach

Velero will back up all pod volumes using Restic with the exception of:

- Volumes mouting the default service account token, Kubernetes secrets, and config maps
- Hostpath volumes

Exclude:

```Bash
kubectl -n {namespace} annotate pod/{pod_name} backup.velero.io/backup-volumes-excludes={YOUR_VOLUME_NAME_1},{YOUR_VOLUME_NAME_2},{...}
```

Backup:

```Bash
velero backup create {backup_name} --default-volumes-to-restic {other_options}
```

### Using opt-in pod volume backup

Every pod containing a volume to be backed up using Restic must be annotated with the volume's name using the annotation.

Contain:

```Bash
kubectl -n {namespace} annotate pod/{pod_name} backup.velero.io/backup-volumes={YOUR_VOLUME_NAME_1},{YOUR_VOLUME_NAME_2},{...}
```

Backup:

```Bash
velero backup create {backup_name} {OPTIONS...}
```

### Restore

```Bash
velero restore create --from-backup {BACKUP_NAME} {OPTIONS...}
```

### Limitations

- hostPath volumes are not supported. Local persistent volumes are supported.
- Those of you familiar with restic may know that it encrypts all of its data. Velero uses a static, common encryption key for all Restic repositories it creates. This means that anyone who has access to your bucket can decrypt your Restic backup data. Make sure that you limit access to the Restic bucket appropriately.
- An incremental backup chain will be maintained across pod reschedules for PVCs. However, for pod volumes that are not PVCs, such as emptyDir volumes, when a pod is deleted/recreated (for example, by a ReplicaSet/Deployment), the next backup of those volumes will be full rather than incremental, because the pod volume’s lifecycle is assumed to be defined by its pod.
- Restic scans each file in a single thread. This means that large files (such as ones storing a database) will take a long time to scan for data deduplication, even if the actual difference is small.
- If you plan to use Velero’s Restic integration to backup 100GB of data or more, you may need to customize the resource limits to make sure backups complete successfully.
- Velero’s Restic integration backs up data from volumes by accessing the node’s filesystem, on which the pod is running. For this reason, Velero’s Restic integration can only backup volumes that are mounted by a pod and not directly from the PVC. For orphan PVC/PV pairs (without running pods), some Velero users overcame this limitation running a staging pod (i.e. a busybox or alpine container with an infinite sleep) to mount these PVC/PV pairs prior taking a Velero backup.

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
- Autocompletion, https://velero.io/docs/main/customize-installation/#enabling-shell-autocompletion, 2023-05-31-Wed.
- restic, https://github.com/restic/restic, 2023-05-31-Wed.
- Restic Integration, https://velero.io/docs/v1.9/restic/, 2023-05-31-Wed.
