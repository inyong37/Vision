# Unmet dependencies while apt install

## Date

2023-02-28-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

## Problem

While trying to install chrony, the error occured:

```Bash
root@node85:~# apt install chrony
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 buildah : Depends: golang-github-containers-common (> 0.44) but it is not going to be installed
 chrony : Conflicts: time-daemon
 podman : Depends: golang-github-containers-common but it is not going to be installed
 systemd-timesyncd : Conflicts: time-daemon
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

```Bash
root@node85:~# apt --fix-broken install
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Correcting dependencies... Done
The following additional packages will be installed:
  golang-github-containers-common golang-github-containers-image
The following NEW packages will be installed:
  golang-github-containers-common golang-github-containers-image
0 upgraded, 2 newly installed, 0 to remove and 19 not upgraded.
33 not fully installed or removed.
Need to get 0 B/57.3 kB of archives.
After this operation, 131 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
debconf: delaying package configuration, since apt-utils is not installed
(Reading database ... 68949 files and directories currently installed.)
Preparing to unpack .../golang-github-containers-image_5.16.0-3_all.deb ...
Unpacking golang-github-containers-image (5.16.0-3) ...
dpkg: error processing archive /var/cache/apt/archives/golang-github-containers-image_5.16.0-3_all.deb (--unpack):
 trying to overwrite '/etc/containers/registries.conf', which is also in package containers-common 100:1-22
Preparing to unpack .../golang-github-containers-common_0.44.4+ds1-1_all.deb ...
Unpacking golang-github-containers-common (0.44.4+ds1-1) ...
dpkg: error processing archive /var/cache/apt/archives/golang-github-containers-common_0.44.4+ds1-1_all.deb (--unpack):
 trying to overwrite '/etc/containers/policy.json', which is also in package containers-common 100:1-22
Errors were encountered while processing:
 /var/cache/apt/archives/golang-github-containers-image_5.16.0-3_all.deb
 /var/cache/apt/archives/golang-github-containers-common_0.44.4+ds1-1_all.deb
needrestart is being skipped since dpkg has failed
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

## [Solution](https://phoenixnap.com/kb/fix-sub-process-usr-bin-dpkg-returned-error-code-1)

### 1. Check dpkg

```Bash
root@node85:~# dpkg --configure -a
Setting up session-migration (0.3.6) ...
Created symlink /etc/systemd/user/graphical-session-pre.target.wants/session-migration.service → /usr/lib/systemd/user/session-migration.service.
Setting up libproxy1v5:amd64 (0.4.17-2) ...
Setting up slirp4netns (100:1.1.8-4) ...
Setting up libarchive13:amd64 (3.6.0-1ubuntu1) ...
Setting up uidmap (1:4.8.1-2ubuntu2.1) ...
dpkg: dependency problems prevent configuration of podman:
 podman depends on golang-github-containers-common; however:
  Package golang-github-containers-common is not installed.

dpkg: error processing package podman (--configure):
 dependency problems - leaving unconfigured
Setting up libprotobuf23:amd64 (3.12.4-1ubuntu7) ...
Setting up libnet1:amd64 (1.1.6+dfsg-3.1build3) ...
Setting up dnsmasq-base (2.86-1.1ubuntu0.1) ...
Setting up libprotobuf-c1:amd64 (1.3.3-1ubuntu2.1) ...
Setting up dns-root-data (2021011101) ...
Setting up libdconf1:amd64 (0.40.0-3) ...
Setting up containernetworking-plugins (0.9.1+ds1-1) ...
Setting up catatonit (0.1.7-1) ...
Setting up libavahi-common-data:amd64 (0.8-5ubuntu5) ...
Setting up golang-github-containernetworking-plugin-dnsname (1.3.1+ds1-2) ...
Setting up libsoup2.4-common (2.74.2-3) ...
Setting up fuse-overlayfs (100:1.5.0-2) ...
Setting up glib-networking-common (2.72.0-1) ...
Setting up python3-protobuf (3.12.4-1ubuntu7) ...
dpkg: dependency problems prevent configuration of buildah:
 buildah depends on golang-github-containers-common (>> 0.44); however:
  Package golang-github-containers-common is not installed.

dpkg: error processing package buildah (--configure):
 dependency problems - leaving unconfigured
Setting up glib-networking-services (2.72.0-1) ...
Setting up libavahi-common3:amd64 (0.8-5ubuntu5) ...
Setting up dconf-service (0.40.0-3) ...
Setting up criu (3.17.1-1) ...
Setting up libavahi-glib1:amd64 (0.8-5ubuntu5) ...
Setting up libavahi-client3:amd64 (0.8-5ubuntu5) ...
Setting up dconf-gsettings-backend:amd64 (0.40.0-3) ...
Setting up crun (100:1.2-2) ...
Setting up gsettings-desktop-schemas (42.0-1ubuntu1) ...
Processing triggers for dbus (1.12.20-2ubuntu4.1) ...
Processing triggers for libglib2.0-0:amd64 (2.72.4-0ubuntu1) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Setting up glib-networking:amd64 (2.72.0-1) ...
Setting up libsoup2.4-1:amd64 (2.74.2-3) ...
Setting up libostree-1-1:amd64 (2022.2-3) ...
Processing triggers for libc-bin (2.35-0ubuntu3.1) ...
Errors were encountered while processing:
 podman
 buildah
```

### 2. Remove all packages with errors

```Bash
root@node85:~# apt remove --purge buildah podman
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  catatonit criu crun dconf-gsettings-backend dconf-service dns-root-data dnsmasq-base fuse-overlayfs glib-networking glib-networking-common glib-networking-services
  golang-github-containernetworking-plugin-dnsname gsettings-desktop-schemas libarchive13 libavahi-client3 libavahi-common-data libavahi-common3 libavahi-glib1 libdconf1 libnet1
  libostree-1-1 libprotobuf-c1 libprotobuf23 libproxy1v5 libsoup2.4-1 libsoup2.4-common python3-protobuf session-migration slirp4netns uidmap
Use 'apt autoremove' to remove them.
The following packages will be REMOVED:
  buildah* podman*
0 upgraded, 0 newly installed, 2 to remove and 25 not upgraded.
2 not fully installed or removed.
After this operation, 58.4 MB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 68949 files and directories currently installed.)
Removing buildah (1.23.1+ds1-2) ...
Removing podman (3.4.4+ds1-1ubuntu1) ...
(Reading database ... 68662 files and directories currently installed.)
Purging configuration files for podman (3.4.4+ds1-1ubuntu1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)
debconf: falling back to frontend: Readline
Scanning processes...
Scanning processor microcode...
Scanning linux images...

Running kernel seems to be up-to-date.

The processor microcode seems to be up-to-date.

No services need to be restarted.

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
```

### A. Unless, try to remove only podman

```Bash
root@node85:~# apt remove podman
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 buildah : Depends: golang-github-containers-common (> 0.44) but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

### B. Unless, try to remove only buildah

```Bash
root@node85:~# apt remove buildah
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 podman : Depends: golang-github-containers-common but it is not going to be installed
          Recommends: buildah (>= 1.21.0) but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

---

### Reference
- apt install Blog, https://phoenixnap.com/kb/fix-sub-process-usr-bin-dpkg-returned-error-code-1, 2023-02-28-Tue.
