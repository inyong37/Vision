# Ubuntu apt update error: Could not get /var/lib/dpkg/lock-frontend

## Date

2023-02-10-Friday.

## Environment

Ubuntu 22.04.1 LTS

## Problem

When I commanded `apt update`, the error occurred as below:

```Bash
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```

## [Solution](https://kgu0724.tistory.com/71)

Kill Related Process:

```Bash
killall apt apt-get
```

:key: You may get a "There is no services" message.

Remove Related Directories:

```Bash
rm /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*
```

```Bash
dpkg --configure -a
```

:tada: Finally, `apt update` will work.

```Bash
apt update
```

---

### Reference
- 리눅스 에러 Could not get lock /var/lib/dpkg/lock-frontend, https://kgu0724.tistory.com/71, 2023-02-10-Fri.
