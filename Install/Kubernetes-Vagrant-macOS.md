# :construction: Install Kubernetes Cluster using Vagrant on macOS with Apple Silicon

## Date

2023-01-18-Wednesday.

## Environmnet

macOS Ventura 13.0.1

Apple M1

### 1. Install Vagrant

```zsh
$ brew install hashicorp/tap/hashicorp-vagrant
```

### 2. Install VMware Fusion

https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-22H2

```zsh
$ ln -s /Applications/VMWare\ Fusion\ Tech\ Preview.app /Applications/VMWare\ Fusion.app
```

```zsh
sudo /opt/vagrant-vmware-desktop/bin/vagrant-vmware-utility api -debug
```

Verify running:

```zsh
$ sudo lsof -i -P | grep LISTEN | grep 'vagrant-v'
```

Or start to run:

```zsh
$ sudo launchctl load -w /Library/LaunchDaemons/com.vagrant.vagrant-vmware-utility.plist
```

```zsh
$ vagrant plugin install vagrant-vmware-desktop
```

---

### Reference
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-18-Wed.
- Setting up Vagrant 2.3.0 for Virtual Machine Management in Mac ( Apple M1 Pro), https://medium.com/geekculture/setting-up-vagrant-2-3-0-for-virtual-machine-management-in-mac-apple-m1-pro-9dc4ec9036db, 2023-01-16-Mon.
- VMware Fusion Public Tech Preview 22H2, https://customerconnect.vmware.com/downloads/get-download?downloadGroup=FUS-PUBTP-22H2, 2023-01-16-Mon.
