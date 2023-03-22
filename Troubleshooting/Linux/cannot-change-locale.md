# LC_CTYPE: cannot change locale (UTF-8)

## Date

2023-02-22-Wednesday.

2023-03-22-Wednesday.

## Environment

Debian GNU/Linux 11 (bullseye)

CentOS 7

## Problem

An error occurred while building the acr122U driver.

## [Solution](https://timte.tistory.com/46)

### Edit `/etc/environment`

```YAML
LANG=en_US.utf-8
LC_ALL=en_US.utf-8
```

### Reboot

```Bash
reboot now
```

---

### Reference
- LC_CTYPE Error Blog KR, https://timte.tistory.com/46, 2023-02-22-Wed.
