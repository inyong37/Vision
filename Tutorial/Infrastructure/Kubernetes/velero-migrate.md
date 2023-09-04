# Migrate Velero

## Date

2023-09-04-Monday.

## Environment

* Ubuntu 22.04.2 LTS
  * Kubernetes 1.24.10
* Ubuntu 20.04.1 LTS
  * Kubernetes 1.23.3

## [Restore Velero Backup to Another Cluster](https://velero.io/docs/main/migration-case/)

Requirements:
1. Velero does not natively support the migration of PVs snapshots across cloud providers. If you would like to migrate volume data between cloud platforms, enable File System Backup, which will backup volume contents at the filesystem level.
2. Velero doesn't support restoring into a cluster with a lower Kubernetes version than where the backup was taken.
  * Migrating workloads across clusters that are not running the same version of Kubernetes might be possible, but some factors need to be considered before migration, including the compatibility of API groups between clusters for each custom resource.
3. The Velero plugin for AWS and Azure does not support migrating data between regions. If you need to do this, you must use File System Backup.

### Setup Velero on Both Clusters: Install and Backup

On source Kubernetes cluster:

```Bash
velero install {[install_arguments]}
velero backup create {[backup_arguments]}
velero backup get
```

On target Kubernetes cluster:

```Bash
velero install {[install_arguments]}
velero backup get
```

### Restore on Target Kubernetes Cluster

```Bash
velero restore create {[restore_arguments]}
```

---

### Reference
- Restore to Another Cluster, https://velero.io/docs/main/migration-case/, 2023-09-04-Mon.
- Restore Reference, https://velero.io/docs/main/restore-reference/, 2023-09-04-Mon.
- Restore Resource Modifiers, https://velero.io/docs/main/restore-resource-modifiers/, 2023-09-04-Mon.
- Restore Hooks, https://velero.io/docs/main/restore-hooks/, 2023-09-04-Mon.
