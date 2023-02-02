# Install Vagrant on macOS with Apple Silicon

## Date

2023-01-17-Tuesday.

## Environment

macOS Ventura 13.0.1

Apple M1

## Contents

### 1. Install Vagrant

```zsh
brew install hashicorp/tap/hashicorp-vagrant
vagrant --version # Validate the installation
```

### 2. Install hypervisor

```zsh
vagrant plugin install vagrant-vmware-desktop
vagrant plugin list # Validate the installation
```

### Uninstall Vagrant

```zsh
sudo rm -rf /opt/vagrant /usr/local/bin/vagrant
sudo pkgutil --forget com.vagrant.vagrant

```

### Check

```Bash
$ vagrant global-status
```

> <img width="1384" alt="Screenshot 2023-01-30 at 10 42 00 AM" src="https://user-images.githubusercontent.com/20737479/215370412-8ec7959d-1e89-4196-9f0c-59ff8581ddfa.png">

### Connect

```Bash
$ vagrant ssh {name} # kubemaster
```

---

### Reference
- Virtual Machine on Apple Mac chip M1/M2 – Fusion/Vagrant, https://www.unixarena.com/2022/09/virtual-machine-on-apple-mac-chip-m1-m2-fusion-vagrant.html/, 2023-01-17-Tue.
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-17-Tue.
- Uninstalling Vagrant, https://developer.hashicorp.com/vagrant/docs/installation/uninstallation, 2023-01-17-Tue.
- 가상머신 생성은 Vagrant로!, https://blog.juho.kim/posts/2021-10-01_Vagrant/, 2023-01-27-Fri.
- Global Status, https://developer.hashicorp.com/vagrant/docs/cli/global-status, 2023-01-30-Mon.
