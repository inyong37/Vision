# Allow Root SSH Connection on Ubuntu 22.04 LTS

## Date

2023-02-01-Wednesday.

## Environment

Ubuntu 22.04 LTS

## Problem

User ssh login works, but the root ssh login doesn't work.

## [Solution](https://linuxconfig.org/allow-ssh-root-login-on-ubuntu-22-04-jammy-jellyfish-linux)

### 1. Permit Root Login in Configuration

After Ubuntu 22, for security, allowing root login via ssh has to be edited by root user in configuration file.

Edit:

```Bash
$ sudo vim /etc/ssh/sshd_config
```

Edit PermitRootLogin with yes argument:

Before:

```YAML
#PermitRootLogin prohibit-password
```

After:

```YAML
...
PermitRootLogin yes
...
```

### 2. Restart SSH

```Bash
systemctl restart ssh
```

### 3. Set Root Password

```Bash
sudo passwd
```

### 4. Allow SSH in firewall

```
sudo ufw allow ssh
```

---

### Reference
- Allow SSH root login on Ubuntu 22.04 Jammy Jellyfish Linux, https://linuxconfig.org/allow-ssh-root-login-on-ubuntu-22-04-jammy-jellyfish-linux, 2023-02-01-Wed.
