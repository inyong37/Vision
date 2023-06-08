# Create Parition on Ubuntu

## Date

2023-03-03-Friday.

## Environment

Ubuntu 22.04.1 LTS with 1TB HDD (OS installed)

## Create Partition on `/dev/sda/`

```Bash
root@node87:~# fdisk /dev/sda

Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

This disk is currently in use - repartitioning is probably a bad idea.
It's recommended to umount all file systems, and swapoff all swap
partitions on this disk.


Command (m for help): n
Partition number (4-128, default 4):
First sector (1953521664-1953525134, default 1953521664):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (1953521664-1953525134, default 1953525134):

Created a new partition 4 of type 'Linux filesystem' and of size 1.7 MiB.

Command (m for help): w
The partition table has been altered.
Syncing disks.
```

> <img width="663" alt="Screenshot 2023-03-03 at 2 48 38 PM" src="https://user-images.githubusercontent.com/20737479/222641631-4ba67ff9-360d-486c-b834-230e4476c216.png">
