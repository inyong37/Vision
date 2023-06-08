# Clean up Disk on Ubuntu

## Date

2023-03-03-Friday.

## Environment

Ubuntu 22.04.1 LST with 128GB SSD (OS installed) and 1TB HDD (to clean-up)

## Check Volumes

```Bash
lsblk
```

## [Format the volume](https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/#cleaning-up-a-cluster) `/dev/sdb`

```Bash
DISK="/dev/sdb"
sgdisk --zap-all $DISK
```

### A. HDD 

```Bash
dd if=/dev/zero of="$DISK" bs=1M count=100 oflag=direct,dsync
```

### B. SSD


```Bash
blkdiscard $DISK
```

### Inform the OS of partition table changes

```Bash
# apt update && apt install parted -y
partprobe $DISK
```

## Verify

```Bash
root@node88:~# lsblk
NAME                      MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda                         8:0    0 119.2G  0 disk
├─sda1                      8:1    0     1G  0 part /boot/efi
├─sda2                      8:2    0     2G  0 part /boot
└─sda3                      8:3    0 116.2G  0 part
  └─ubuntu--vg-ubuntu--lv 253:0    0  58.1G  0 lvm  /var/lib/containers/storage/overlay
                                                    /
sdb                         8:16   0 931.5G  0 disk
sr0                        11:0    1  1024M  0 rom
```

---

### Reference
- Delete the data Rook-Ceph, https://rook.io/docs/rook/v1.10/Getting-Started/ceph-teardown/#delete-the-data-on-hosts, 2023-03-03-Fri.
