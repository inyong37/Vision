# Velero Backups are stuck in deleting status

## Date

2023-09-05-Tuesday.

## Environment

* Ubuntu 20.04.6 LTS
  * Kubernetes 1.27.4
    * Velero 1.11.1

## Problem

```Bash
NAME                          STATUS            ERRORS   WARNINGS   CREATED                         EXPIRES   STORAGE LOCATION   SELECTOR
backup-daily-20230904180038   PartiallyFailed   3        0          2023-09-04 18:00:38 +0000 UTC   9d        default            <none>
backup-daily-20230903180037   PartiallyFailed   3        0          2023-09-03 18:00:37 +0000 UTC   8d        default            <none>
backup-daily-20230902180036   PartiallyFailed   3        0          2023-09-02 18:00:36 +0000 UTC   7d        default            <none>
backup-daily-20230901180035   PartiallyFailed   3        0          2023-09-01 18:00:35 +0000 UTC   6d        default            <none>
backup-daily-20230831180034   Completed         0        0          2023-08-31 18:00:34 +0000 UTC   5d        default            <none>
backup-daily-20230830180033   Completed         0        0          2023-08-30 18:00:33 +0000 UTC   4d        default            <none>
backup-daily-20230829180032   Completed         0        0          2023-08-29 18:00:32 +0000 UTC   3d        default            <none>
backup-daily-20230828180031   Completed         0        0          2023-08-28 18:00:32 +0000 UTC   2d        default            <none>
backup-daily-20230827180030   Completed         0        0          2023-08-27 18:00:30 +0000 UTC   1d        default            <none>
backup-daily-20230826180029   Completed         0        0          2023-08-26 18:00:29 +0000 UTC   16h       default            <none>
backup-daily-20230825180028   Deleting          0        0          2023-08-25 18:00:29 +0000 UTC   7h ago    default            <none>
backup-daily-20230824180028   Deleting          0        0          2023-08-24 18:00:28 +0000 UTC   1d ago    default            <none>
backup-daily-20230823180027   Deleting          0        0          2023-08-23 18:00:27 +0000 UTC   2d ago    default            <none>
backup-daily-20230822180026   Deleting          0        0          2023-08-22 18:00:26 +0000 UTC   3d ago    default            <none>
```

```Bash
    error running command=restic forget --repo=s3:http://192.168.0.1:9000/main-infra/restic/osinfra --password-file=/tmp/credentials/velero/velero-repo-credentials-repository-password --cache-dir=/scratch/.cache/restic ..., stdout=, stderr=Fatal: unable to open config file: Stat: The specified key does not exist.
Is there a repository at the following location?
s3:http://192.168.0.1:9000/main-infra/restic/osinfra
: exit status 1
```

## Solution

`k get resticrepository -A`

```Bash
error: the server doesn't have a resource type "resticrepository"
```

`k get backuprepository -A`

```Bash
NAMESPACE   NAME                           AGE   REPOSITORY TYPE
velero      osinfra-default-restic-lh7qj   14d   restic
```

`k delete backuprepository osinfra-default-restic-lh7qj -n velero`

```Bash
backuprepository.velero.io "osinfra-default-restic-lh7qj" deleted
```

`k get deployment velero -n velero`

```Bash
NAME     READY   UP-TO-DATE   AVAILABLE   AGE
velero   1/1     1            1           17d
```

`k rollout restart deployment velero -n velero`

```Bash
deployment.apps/velero restarted
```

:tada: All deleting backups are gone.

---

### Reference
- Velero Error Checking Repository for Stale Locks Blog KR, https://1week.tistory.com/111, 2023-09-05-Tue.
