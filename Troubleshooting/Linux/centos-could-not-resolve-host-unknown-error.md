# Yum Install Could Not Resolve Host Unknown Error

## Environment

CentOS Linux release 7.9.2009 (Core)

## Date

2023-01-31-Tuesday.

## Problem

I was trying to install tmux (window manager in terminal interface), but yum-install failed as below:

```Bash
$ sudo yum install -y tmux
```

> <img width="1317" alt="Screenshot 2023-01-31 at 10 05 33 AM" src="https://user-images.githubusercontent.com/20737479/215632614-3f3122d5-805f-4aea-9bb6-292c490d0640.png">

## Solution

I looked up some similar problems and I found that the nameserver setup was cleared when I checked `cat /etc/resolv.conf`.

Therefore, I added nameservers such as Google's.

Add DNS server:

```Bash
$ vim /etc/resolv.conf
```

---

### Reference
- How to Fix “curl:(6) Could not resolve host” Error in Linux, https://itslinuxfoss.com/fix-curl-could-not-resolve-host-error-linux/, 2023-01-31-Tue.
- 리눅스 DNS 설정 방법, https://bono915.tistory.com/entry/Linux-%EB%A6%AC%EB%88%85%EC%8A%A4-DNS-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95, 2023-01-31-Tue.
