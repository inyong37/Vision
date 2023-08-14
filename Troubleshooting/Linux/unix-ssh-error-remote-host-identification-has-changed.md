# WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!

## Date

2023-02-10-Friday.

## Environment

SSH Client: macOS 13.0.1

SSH Server: Ubuntu 22.04.1 LTS, Fedora 37

## Problem

I tried to connect via ssh, but got the following error:

```Bash
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
```

## [Solutions](https://kingsong.tistory.com/127)

### #1

```Bash
ssh-keygen -R {ip_address}
```

### #2

```Bash
rm /User/{user_name}/.ssh/known_host # or rm /root/.ssh/known_hosts
```

### #3 Edit known_hosts file

---

### Reference
- SSH 접속 오류 : REMOTE HOST IDENTIFICATION HAS CHANGED - RSA key 오류 해결법, https://kingsong.tistory.com/127, 2023-02-10-Fri.
