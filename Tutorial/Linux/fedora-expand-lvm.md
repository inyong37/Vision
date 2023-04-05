# Expand Disk LVM

## Date

2023-04-05-Wednesday.

## Environment

Fedora 37

## Expand LVM

Install a package:

```Bash
sudo yum install -y cloud-utils-growpart
```

Check disks:

```Bash
lsblk
```

Output:

```Bash
NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda               8:0    0 931.5G  0 disk
├─sda1            8:1    0   200M  0 part
├─sda2            8:2    0 914.3G  0 part
└─sda3            8:3    0    17G  0 part
sdb               8:16   0 238.5G  0 disk
├─sdb1            8:17   0   600M  0 part /boot/efi
├─sdb2            8:18   0     1G  0 part /boot
└─sdb3            8:19   0 236.9G  0 part
  └─fedora-root 253:0    0    15G  0 lvm  /
zram0           252:0    0     8G  0 disk [SWAP]
```

Already the machine's sdb3 VG is allocated 236.9 GB.

FYI: Allocate VG

```Bash
sudo pvresize /dev/sdb3
```

Check VG is expanded:

```Bash
sudo vgdisplay
```

Output:

```Bash
  --- Volume group ---
  VG Name               fedora
  System ID
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  2
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                1
  Open LV               1
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               <236.89 GiB
  PE Size               4.00 MiB
  Total PE              60643
  Alloc PE / Size       3840 / 15.00 GiB
  Free  PE / Size       56803 / <221.89 GiB
  VG UUID               VtcGRN-KK5L-S6jo-8X5J-Wp1q-jr85-sE2HG1
```

Check the path with `df -h` not with `lsblk`:

```Bash
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 4.0M     0  4.0M   0% /dev
tmpfs                    7.8G   28K  7.8G   1% /dev/shm
tmpfs                    3.1G  1.5M  3.1G   1% /run
/dev/mapper/fedora-root   15G   15G  685M  96% /            <- This is the path to expand.
tmpfs                    7.8G  4.0K  7.8G   1% /tmp
/dev/sdb2                960M  210M  751M  22% /boot
/dev/sdb1                599M  6.2M  593M   2% /boot/efi
tmpfs                    1.6G   40K  1.6G   1% /run/user/1000
tmpfs                    1.6G     0  1.6G   0% /run/user/0
```

Expand LVM:

```Bash
sudo lvextend -r -l +100%FREE /dev/mapper/fedora-root
```

:tada: Output:

```Bash
  Size of logical volume fedora/root changed from 15.00 GiB (3840 extents) to <236.89 GiB (60643 extents).
  Logical volume fedora/root successfully resized.
meta-data=/dev/mapper/fedora-root isize=512    agcount=4, agsize=983040 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=1, sparse=1, rmapbt=0
         =                       reflink=1    bigtime=1 inobtcount=1
data     =                       bsize=4096   blocks=3932160, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0, ftype=1
log      =internal log           bsize=4096   blocks=16384, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 3932160 to 62098432
```

---

### Reference
- Expand lvm Blog KR, https://helpit.tistory.com/2, 2023-04-05-Wed.
