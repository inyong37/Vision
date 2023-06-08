# Deploy Fedora VM with KubeVirt

## Date

2023-03-13-Monday.

## Environment

Ubuntu 22.04.2 LTS

Kubernetes 1.24.10

## [Deploy Virtual Machine Instance of Fedora](https://kubevirt.io/user-guide/virtual_machines/virtual_machine_instances/)

### Make vmi yaml file

```Bash
root@node87:~# vim testvmi-nocloud.yaml
```

```YAML
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  name: testvmi-nocloud
spec:
  terminationGracePeriodSeconds: 30
  domain:
    resources:
      requests:
        memory: 1024M
    devices:
      disks:
      - name: containerdisk
        disk:
          bus: virtio
      - name: emptydisk
        disk:
          bus: virtio
      - disk:
          bus: virtio
        name: cloudinitdisk
  volumes:
  - name: containerdisk
    containerDisk:
      image: kubevirt/fedora-cloud-container-disk-demo:latest
  - name: emptydisk
    emptyDisk:
      capacity: "2Gi"
  - name: cloudinitdisk
    cloudInitNoCloud:
      userData: |-
        #cloud-config
        password: fedora
        chpasswd: { expire: False }
```

### Create it

```Bash
root@node87:~# k apply -f testvmi-nocloud.yaml
```

### :tada: Verfiy

```Bash
root@node87:~# k get vmi
NAME              AGE   PHASE        IP    NODENAME   READY
testvmi-nocloud   3s    Scheduling                    False
root@node87:~# k get vmi
NAME              AGE     PHASE     IP          NODENAME   READY
testvmi-nocloud   2m25s   Running   10.39.0.1   node85     True
```

---

### Reference
- Virtual Machines Instances, https://kubevirt.io/user-guide/virtual_machines/virtual_machine_instances/, 2023-03-13-Mon.
