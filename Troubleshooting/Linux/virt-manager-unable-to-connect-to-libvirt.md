# Unable to connect to libvirt

## Date

2023-10-06-Friday.

## Environment

* Ubuntu 20.04.4 LTS
  * virt-manager 2.2.1

## Problem

QEMU/KVM - Not Connected

```
Unable to connect to libvirt qemu:///system.

Verify that the 'libvirtd' daemon is running.
```

## Solution

Run it with:

```Bash
sudo virt-manager
```

---

### Reference
- https://ubuntuforums.org/showthread.php?t=2480264, 2023-10-06-Fri.
