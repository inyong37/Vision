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

### :tada: Check It on Target Kubernetes Cluster

```Bash
velero restore {get | describe | logs} {restore_name}
```

### Restore Commands

```Bash
create
delete
describe
get
logs
```

### Workflow

* Velero Client -> Kubernetes API Server; create a `Restore` object
* RestoreController
  * notices the new `Restore` object and validates
  * fetches basic information, tarball
  * extracts the tarball and performs preprocesses
  * restores resources
    * The RestoreController makes sure the target namespace exists. If the target namespace does not exist, then the RestoreController will create a new one on the cluster.
    * If the resource is a Persistent Volume (PV), the RestoreController will rename the PV and remap its namespace.
    * If the resource is a Persistent Volume Claim (PVC), the RestoreController will modify the PVC metadata.
    * Execute the resource’s RestoreItemAction custom plugins, if you have configured one.
    * Update the resource object’s namespace if you’ve configured namespace remapping.
    * The RestoreController adds a velero.io/backup-name label with the backup name and a velero.io/restore-name with the restore name to the resource. This can help you easily identify restored resources and which backup they were restored from.
  * creates the resource object on the target cluster
* additional steps by Velero
  * If the resource is a Pod, the RestoreController will execute any Restore Hooks and wait for the hook to finish.
  * If the resource is a PV restored by File System Backup, the RestoreController waits for File System Backup’s restore to complete. The RestoreController sets a timeout for any resources restored with File System Backup during a restore. The default timeout is 4 hours, but you can configure this be setting using --fs-backup-timeout restore option.
  * If the resource is a Custom Resource Definition, the RestoreController waits for its availability in the cluster. The timeout is 1 minute.
* If any failures happen finishing these steps, the RestoreController will log an error in the restore result and will continue restoring.

---

### Reference
- Restore to Another Cluster, https://velero.io/docs/main/migration-case/, 2023-09-04-Mon.
- Restore Reference, https://velero.io/docs/main/restore-reference/, 2023-09-04-Mon.
- Restore Resource Modifiers, https://velero.io/docs/main/restore-resource-modifiers/, 2023-09-04-Mon.
- Restore Hooks, https://velero.io/docs/main/restore-hooks/, 2023-09-04-Mon.
