# Failed to run custom build command for 'ostree-sys v0.10.0'

## Date

2023-04-12-Wednesday

## Environment

Ubuntu 22.04.2 LTS

Docker 23.0.3

## Problem

```Bash
The following warnings were emitted during compilation:

warning: `PKG_CONFIG_ALLOW_SYSTEM_CFLAGS="1" "pkg-config" "--libs" "--cflags" "ostree-1" "ostree-1 >= 2021.5"` did not exit successfully: exit status: 1

error: failed to run custom build command for `ostree-sys v0.10.0`

Caused by:
  process didn't exit successfully: `/root/flat-manager/target/debug/build/ostree-sys-57d83f9a9e9e0983/build-script-build` (exit status: 1)
  --- stdout
  cargo:rerun-if-env-changed=OSTREE_1_NO_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_PATH
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_LIBDIR
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_SYSROOT_DIR
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR
  cargo:warning=`PKG_CONFIG_ALLOW_SYSTEM_CFLAGS="1" "pkg-config" "--libs" "--cflags" "ostree-1" "ostree-1 >= 2021.5"` did not exit successfully: exit status: 1
  error: could not find system library 'ostree-1' required by the 'ostree-sys' crate

  --- stderr
  Requested 'ostree-1 >= 2021.5' but version of OSTree is 2020.8

warning: build failed, waiting for other jobs to finish...
```

## Solution

```Bash
root@629879b650da:~# apt install ostree
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  debugedit elfutils gir1.2-flatpak-1.0 libasm1 unzip zstd
Use 'apt autoremove' to remove them.
The following NEW packages will be installed:
  ostree
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 182 kB of archives.
After this operation, 506 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 ostree amd64 2022.2-3 [182 kB]
Fetched 182 kB in 2s (111 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package ostree.
(Reading database ... 47743 files and directories currently installed.)
Preparing to unpack .../ostree_2022.2-3_amd64.deb ...
Unpacking ostree (2022.2-3) ...
Setting up ostree (2022.2-3) ...
root@629879b650da:~# ostree --version
libostree:
 Version: '2022.2'
 Features:
  - libsoup
  - gpgme
  - ex-fsverity
  - libarchive
  - selinux
  - avahi
  - libmount
  - systemd
  - release
  - p2p
```
