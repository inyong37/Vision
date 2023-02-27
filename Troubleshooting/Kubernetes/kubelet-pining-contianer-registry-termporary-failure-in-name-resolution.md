# kubelet Failed to pull image Temporary failure in name resolution

## Date

2023-02-24-Friday.

## Enviroment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

While deploying Linux VM on KubeVirt, an error occured as below:

```Bash
root@node85:~# k get vmis
NAME     AGE    PHASE        IP    NODENAME   READY
testvm   103s   Scheduling                    False
...
Events:
  Type     Reason     Age   From               Message
  ----     ------     ----  ----               -------
  Normal   Scheduled  64s   default-scheduler  Successfully assigned default/virt-launcher-testvm-kxlsg to node87
  Normal   Pulled     63s   kubelet            Container image "quay.io/kubevirt/virt-launcher:v0.58.1" already present on machine
  Normal   Created    63s   kubelet            Created container container-disk-binary
  Normal   Started    63s   kubelet            Started container container-disk-binary
  Normal   Pulling    63s   kubelet            Pulling image "quay.io/kubevirt/cirros-container-disk-demo"
  Warning  Failed     3s    kubelet            Failed to pull image "quay.io/kubevirt/cirros-container-disk-demo": rpc error: code = Unknown desc = pinging container registry quay.io: Get "https://quay.io/v2/": dial tcp: lookup quay.io: Temporary failure in name resolution
  Warning  Failed     3s    kubelet            Error: ErrImagePull
  Normal   BackOff    3s    kubelet            Back-off pulling image "quay.io/kubevirt/cirros-container-disk-demo"
  Warning  Failed     3s    kubelet            Error: ImagePullBackOff
```

## Solution

Change DNS server (nameserver) address

### 1. Edit `/etc/resolv.conf`

Before:

```YAML
# This is /run/systemd/resolve/stub-resolv.conf managed by man:systemd-resolved(8).
# Do not edit.
#
# This file might be symlinked as /etc/resolv.conf. If you're looking at
# /etc/resolv.conf and seeing this text, you have followed the symlink.
#
# This is a dynamic resolv.conf file for connecting local clients to the
# internal DNS stub resolver of systemd-resolved. This file lists all
# configured search domains.
#
# Run "resolvectl status" to see details about the uplink DNS servers
# currently in use.
#
# Third party programs should typically not access this file directly, but only
# through the symlink at /etc/resolv.conf. To manage man:resolv.conf(5) in a
# different way, replace this symlink by a static file or a different symlink.
#
# See man:systemd-resolved.service(8) for details about the supported modes of
# operation for /etc/resolv.conf.

nameserver 127.0.0.53
options edns0 trust-ad
search .
```

After:

```YAML
nameserver 8.8.8.8
```

### 2. Edit `/etc/netplan/00-installer-config.yaml`

Before:

```YAML
...
nameservers:
  addresses:
  - private nameserver
  search: []
...
```

After:

```YAML
...
nameservers:
  addresses:
  - 8.8.8.8
  - 8.8.4.4
  search: []
...
```

Apply:

```Bash
netplan apply
```

### :tada: Verify

```Bash
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  18s   default-scheduler  Successfully assigned default/virt-launcher-testvm-4dq6n to node87
  Normal  Pulled     17s   kubelet            Container image "quay.io/kubevirt/virt-launcher:v0.58.1" already present on machine
  Normal  Created    17s   kubelet            Created container container-disk-binary
  Normal  Started    17s   kubelet            Started container container-disk-binary
  Normal  Pulling    16s   kubelet            Pulling image "quay.io/kubevirt/cirros-container-disk-demo"
  Normal  Pulled     7s    kubelet            Successfully pulled image "quay.io/kubevirt/cirros-container-disk-demo" in 9.812895297s
  Normal  Created    6s    kubelet            Created container volumecontainerdisk-init
  Normal  Started    6s    kubelet            Started container volumecontainerdisk-init
  Normal  Pulled     5s    kubelet            Container image "quay.io/kubevirt/virt-launcher:v0.58.1" already present on machine
  Normal  Created    5s    kubelet            Created container compute
  Normal  Started    5s    kubelet            Started container compute
  Normal  Pulling    5s    kubelet            Pulling image "quay.io/kubevirt/cirros-container-disk-demo"
  Normal  Pulled     1s    kubelet            Successfully pulled image "quay.io/kubevirt/cirros-container-disk-demo" in 3.947816006s
  Normal  Created    1s    kubelet            Created container volumecontainerdisk
  Normal  Started    1s    kubelet            Started container volumecontainerdisk
```
