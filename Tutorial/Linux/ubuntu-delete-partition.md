# Delete Partition on Ubuntu

## Date

2023-03-03-Friday.

## Environment

Ubuntu 22.04.1 LTS with 128GB SSD (OS installed)

## Delete Partition `/dev/sda4/`

```Bash
root@node87:~# fdisk /dev/sda

Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): d
Partition number (1-4, default 4): 4

Partition 4 has been deleted.

Command (m for help): w
The partition table has been altered.
Syncing disks.
```
