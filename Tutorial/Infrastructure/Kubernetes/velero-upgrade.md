# [Upgrade Velero](https://velero.io/docs/v1.11/upgrade-to-1.11/)

## Date

2023-08-18-Friday.

## Environment

- Ubuntu 22.04.2 LTS
  - Kubernetes 1.24.10
- Ubuntu 20.04.1 LTS
  - Kubernetes 1.23.3

## [Upgrade to 1.11 (latest in Aug. 2023)](https://velero.io/docs/v1.11/upgrade-to-1.11/)

From Velero v1.10, except for using restic to do file-system level backup and restore, kopia is also been integrated, it could be upgraded from v1.10 to v1.11 directly, but it would be a little bit of difference when upgrading to v1.11 from a version lower than v1.10.0.

### Upgrade from version lower than v.1.10.0

1. [Install the Velero CLI](https://velero.io/docs/v1.11/basic-install/):

```Bash
wget https://github.com/vmware-tanzu/velero/releases/download/v1.11.1/velero-v1.11.1-linux-amd64.tar.gz
tar -xvf velero-v1.11.1-linux-amd64.tar.gz
rm /bin/velero
mv velero-v1.11.1-linux-amd64/velero /bin/
```

2. Update the Velero custom resource definitions (CRDs) to include schema change across all CRDs that are at the core of the new features in this release:

```Bash
velero install --crds-only --dry-run -o yaml | kubectl apply -f -
```

3. Update the container image and objects field used by the Velero deployment and, optionally, the restic daemon set:

```Bash
# uploader_type value could be restic or kopia
kubectl get deploy -n velero -ojson \
| sed "s#\"image\"\: \"velero\/velero\:v[0-9]*.[0-9]*.[0-9]\"#\"image\"\: \"velero\/velero\:v1.11.0\"#g" \
| sed "s#\"server\",#\"server\",\"--uploader-type=$uploader_type\",#g" \
| sed "s#default-volumes-to-restic#default-volumes-to-fs-backup#g" \
| sed "s#default-restic-prune-frequency#default-repo-maintain-frequency#g" \
| sed "s#restic-timeout#fs-backup-timeout#g" \
| kubectl apply -f -

# optional, if using the restic daemon set
echo $(kubectl get ds -n velero restic -ojson) \
| sed "s#\"image\"\: \"velero\/velero\:v[0-9]*.[0-9]*.[0-9]\"#\"image\"\: \"velero\/velero\:v1.11.0\"#g" \
| sed "s#\"name\"\: \"restic\"#\"name\"\: \"node-agent\"#g" \
| sed "s#\[ \"restic\",#\[ \"node-agent\",#g" \
| kubectl apply -f -
kubectl delete ds -n velero restic --force --grace-period 0
```

:bulb: If upgraded from v1.9.x, there still remains some resources left over in the cluster and never used in v1.11.x, which could be deleted through kubectl and it is based on your desire:

* resticrepository CRD and related CRs

* velero-restic-credentials secret in velero install namespace

### Upgrade from v1.10

If it’s directly upgraded from v1.10, the other steps remain the same only except for step 3 above. The details as below:

3. Update the container image used by the Velero deployment, plugin and, optionally, the node agent daemon set:

```Bash
# set the container and image of the init container for plugin accordingly,
# if you are using other plugin
kubectl set image deployment/velero \
    velero=velero/velero:v1.11.0 \
    velero-plugin-for-aws=velero/velero-plugin-for-aws:v1.7.0 \
    --namespace velero

# optional, if using the node agent daemonset
kubectl set image daemonset/node-agent \
    node-agent=velero/velero:v1.11.0 \
    --namespace velero
```

---

### Reference
- Upgrade to 1.11, https://velero.io/docs/v1.11/upgrade-to-1.11/, 2023-08-18-Fri.
- Install, https://velero.io/docs/v1.11/basic-install/, 2023-08-18-Fri.
