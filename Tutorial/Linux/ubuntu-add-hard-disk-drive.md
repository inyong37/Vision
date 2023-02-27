# Add Extra Hard Disk Drive on Ubuntu

## Date

2023-02-27-Monday.

## Environment

Ubuntu 22.04.1 LTS

## [Add Extra HDD (< 2TB)](https://smoh.tistory.com/377)

### 1. Check mounted disks

```Bash
root@node85:~# fdisk -l
Disk /dev/sda: 119.24 GiB, 128035676160 bytes, 250069680 sectors
Disk model: SAMSUNG MZ7LN128
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 6CD4F8AF-203F-42D7-84E4-D8B62BABDBC6

Device       Start       End   Sectors   Size Type
/dev/sda1     2048   2203647   2201600     1G EFI System
/dev/sda2  2203648   6397951   4194304     2G Linux filesystem
/dev/sda3  6397952 250066943 243668992 116.2G Linux filesystem


Disk /dev/sdb: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: WDC WD10EZEX-60M
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x5d9cbe51


Disk /dev/mapper/ubuntu--vg-ubuntu--lv: 58.09 GiB, 62377689088 bytes, 121831424 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

### 2. Check using disks

```Bash
root@node85:~# df -h
Filesystem                         Size  Used Avail Use% Mounted on
tmpfs                              784M  2.5M  781M   1% /run
/dev/mapper/ubuntu--vg-ubuntu--lv   57G   19G   36G  35% /
tmpfs                              3.9G   84K  3.9G   1% /dev/shm
tmpfs                              5.0M     0  5.0M   0% /run/lock
/dev/sda2                          2.0G  128M  1.7G   7% /boot
/dev/sda1                          1.1G  6.1M  1.1G   1% /boot/efi
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/3b44ae20b7405d2f4f9d3714bad5dd428e1eadba7be90ae92bcfdf2be9232434/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/203081035f644a94577f51bfb3d6b5173362aa69e3192d6d8514ca8bd9fc1bb1/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/924326d97e272eb0b6e05c8359ba685c19668c459c8f8500b9eec492287f9606/merged
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/58737281e618d2fbaa734a066e2ea87c661a6b34411a7c173938ae7e48531ce1/userdata/shm
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/935d4257ec54f7c779797ef3412622be8c67fd676b339965bcc47393be339829/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/2861fa4ea8682d6268a298e1e59732aae43e5f1dd541cb241d666719cf8a9606/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/31c14c50b433beee88934fde518bcf63ea0a027c6f9f1e47b9ffd53d12a12344/merged
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/017be0e661540f0454aba4bd674e4d85b3356da33dd3aea32c2f19e5d7a63166/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/1b5bf9213aff5e974be1dbeec37d5b297a8498f920b4871c1a90cf8f048279d9/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/368d9dc618722b5b9721778227040e8ff6e2aba6cb49f1948c64aebb0eae095c/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/30e9c55abd8343ae8f79e9c15d0f40b6963f480983d8184b409ec6a82afca629/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/1d066b5f4a052557a84285189724a341edd3218f1c7fa698c6ab6eda6c5e300c/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/dcac499662de325225fac53c382c3d691f9c2c4211cf55bdfa9b4452687f0067/merged
tmpfs                              7.6G   12K  7.6G   1% /var/lib/kubelet/pods/09cc54e5-cb20-4c55-9ee7-66d9b566c884/volumes/kubernetes.io~projected/kube-api-access-shqcd
tmpfs                              170M   12K  170M   1% /var/lib/kubelet/pods/46a23347-4a9f-4efe-bedf-8f58f9e3d62d/volumes/kubernetes.io~projected/kube-api-access-tmdr9
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/69019984a84dfdadcaea35050b04fb45043c4277d0bdc493095c9e3b96ba1819/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/fa07d5b245845f4126a6170d8b59c868c318f373309e242e486cf2a80c1e7378/merged
tmpfs                              170M   12K  170M   1% /var/lib/kubelet/pods/a8aeaab9-ff20-4778-9551-e4c643400245/volumes/kubernetes.io~projected/kube-api-access-nl78z
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/b59a4f56a3f29109c1e4afb9d5a56c0eb785c11d39215939d009911fd82ecb32/merged
tmpfs                              7.6G   12K  7.6G   1% /var/lib/kubelet/pods/cc8ccac1-5ef6-4863-9573-3989c6b3f272/volumes/kubernetes.io~projected/kube-api-access-7cpkh
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/9afd36e422bef9b120f283ed288979f45581395f3a01b9ea5e14ba8ee6e7f6a6/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/ae45dd25f491b24acc408885a3188400745bb2e96404631a761dcc27076b01e0/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/eff13edcf743194547983bd28199fce1c4293fea5413f6b52a5f517252be454a/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/9a42e5d0f40e7c4bbc92cf91943083bcfe26e814a536193270dc1332becffcc0/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/ffb93650b08142eaa9cdc8f10a81f724d1c0067eacd36309614d852eaa2457c5/merged
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/3f6a8e752dd83a13e2e4f490d990937c474d63e3286a1cabadc49e25e070235e/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/9d71bddf40680047e4b50c390c194b8081228ae5c82b71b7130a3375b5278035/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/eca543efaa3bb659cbedc89e9a06294a9e42fcd99b8bedf653a09cb9eb8eb0ac/merged
shm                                 64M     0   64M   0% /run/containers/storage/overlay-containers/3e9523f41a2aeb0a123c86d36358fb92bc8e35c60f6dc7ff169ffb898fd1bfd3/userdata/shm
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/02e507a5414aac7819765db0c3788b6960f18645e572e06ffd789fbf1dbce5cd/merged
overlay                             57G   19G   36G  35% /var/lib/containers/storage/overlay/a5c4580ddc9f8f39ea59a2c59d097c3b0531b3af6151d427b5b5316a31eb4dd8/merged
tmpfs                              784M  4.0K  784M   1% /run/user/1000
tmpfs                              784M  4.0K  784M   1% /run/user/0
```

### 3. Compose partition

```Bash
root@node85:~# fdisk /dev/sdb

Welcome to fdisk (util-linux 2.37.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-1953525167, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-1953525167, default 1953525167):

Created a new partition 1 of type 'Linux' and of size 931.5 GiB.

Command (m for help): p
Disk /dev/sdb: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: WDC WD10EZEX-60M
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x5d9cbe51

Device     Boot Start        End    Sectors   Size Id Type
/dev/sdb1        2048 1953525167 1953523120 931.5G 83 Linux

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

### 4. Check mounted disks

```Bash
root@node85:~# fdisk -l
Disk /dev/sda: 119.24 GiB, 128035676160 bytes, 250069680 sectors
Disk model: SAMSUNG MZ7LN128
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 6CD4F8AF-203F-42D7-84E4-D8B62BABDBC6

Device       Start       End   Sectors   Size Type
/dev/sda1     2048   2203647   2201600     1G EFI System
/dev/sda2  2203648   6397951   4194304     2G Linux filesystem
/dev/sda3  6397952 250066943 243668992 116.2G Linux filesystem


Disk /dev/sdb: 931.51 GiB, 1000204886016 bytes, 1953525168 sectors
Disk model: WDC WD10EZEX-60M
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: dos
Disk identifier: 0x5d9cbe51

Device     Boot Start        End    Sectors   Size Id Type
/dev/sdb1        2048 1953525167 1953523120 931.5G 83 Linux


Disk /dev/mapper/ubuntu--vg-ubuntu--lv: 58.09 GiB, 62377689088 bytes, 121831424 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

### 5. Format the new disk

```Bash
root@node85:~# mkfs.ext4 /dev/sdb1
mke2fs 1.46.5 (30-Dec-2021)
Creating filesystem with 244190390 4k blocks and 61054976 inodes
Filesystem UUID: e3f8281b-0352-4ece-8454-1e6863442b3d
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
	4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968,
	102400000, 214990848

Allocating group tables: done
Writing inode tables: done
Creating journal (262144 blocks):
done
Writing superblocks and filesystem accounting information:
done
```

### 6. Check UUID

```Bash
root@node85:~# blkid
/dev/mapper/ubuntu--vg-ubuntu--lv: UUID="8a5bd3d6-297b-4f27-9100-cdbd0255c789" BLOCK_SIZE="4096" TYPE="ext4"
/dev/sda2: UUID="a7e5a642-cf0d-4d2a-ada9-9dfe927aca88" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="bde5b34a-6d0f-4b56-bb62-8713958d2e5e"
/dev/sda3: UUID="qQ51eH-JHBm-oNqW-N8Rx-52cG-KvxI-xRJzeY" TYPE="LVM2_member" PARTUUID="d8bfe24a-0f4e-42d5-afbb-a267d344a61b"
/dev/sda1: UUID="E33B-A260" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="272efe31-27a5-4ba8-982c-c9604b9a0784"
/dev/sdb1: UUID="e3f8281b-0352-4ece-8454-1e6863442b3d" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="5d9cbe51-01"
```

### 7. Make directory for the new disk

```Bash
root@node85:~# mkdir -p /data
```

### 8. Add mounting information for the new disk

```Bash
vim /etc/fstab
```

```YAML
...
# /data
UUID=e3f8281b-0352-4ece-8454-1e6863442b3d       /data   ext4    defaults        0       0
```

### 9. Mount the new disk

```Bash
mount -a
```

### 10. Verify

```Bash
root@node85:~# df -h | grep sdb
/dev/sdb1                          916G   28K  870G   1% /data
```

---

### Reference
- Add Hard Disk Drive Blog KR, https://smoh.tistory.com/377, 2023-02-27-Mon.
