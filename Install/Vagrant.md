# Vagrant

## Mac computers with Apple silicon

### 1. Install Vagrant

```zsh
$ brew install hashicorp/tap/hashicorp-vagrant
$ vagrant --version # Validate the installation
```

### 2. Install hypervisor

```zsh
$ vagrant plugin install vagrant-vmware-desktop
$ vagrant plugin list # Validate the installation
```

---

### Reference
- Virtual Machine on Apple Mac chip M1/M2 – Fusion/Vagrant, https://www.unixarena.com/2022/09/virtual-machine-on-apple-mac-chip-m1-m2-fusion-vagrant.html/, 2023-01-17-Tue.
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-17-Tue.
