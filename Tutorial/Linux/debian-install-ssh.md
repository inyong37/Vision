# [Enable SSH](https://linuxopsys.com/topics/enable-ssh-on-debian)

## Date

2023-02-22-Wednesday.

## Environment

Debian GNU/Linux 11 (bullseye)

## Content

:key: All commands are executed on root authority

### 1. Install openssh-server

```Bash
apt update && apt install openssh-server
```

### 2. Restart and Enable SSH

```Bash
systemctl start sshd
```

```Bash
systemctl enable ssh
```

---

### Reference
- Enable SSH, https://linuxopsys.com/topics/enable-ssh-on-debian, 2023-02-22-Wed.
