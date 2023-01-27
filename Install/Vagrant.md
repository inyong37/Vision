# Vagrant

## Mac computers with Apple silicon

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

---

### Reference
- Virtual Machine on Apple Mac chip M1/M2 – Fusion/Vagrant, https://www.unixarena.com/2022/09/virtual-machine-on-apple-mac-chip-m1-m2-fusion-vagrant.html/, 2023-01-17-Tue.
- Install Vagrant, https://developer.hashicorp.com/vagrant/downloads, 2023-01-17-Tue.
- Uninstalling Vagrant, https://developer.hashicorp.com/vagrant/docs/installation/uninstallation, 2023-01-17-Tue.
- 가상머신 생성은 Vagrant로!, https://blog.juho.kim/posts/2021-10-01_Vagrant/, 2023-01-27-Fri.
