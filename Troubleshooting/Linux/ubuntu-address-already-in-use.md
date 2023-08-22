# Address Already in Use

## Date

2023-08-22-Tuesday.

## Environment

Ubuntu 22.04.3 LTS

## Problem

### While Starting CoreDNS Docker-Compose:

```Bash
inyong@server:~/dns$ docker-compose up -d
...
Creating test-coredns ... error

ERROR: for test-coredns  Cannot start service coredns: driver failed programming external connectivity on endpoint test-coredns (...): Error starting userland proxy: listen tcp4 0.0.0.0:53: bind: address already in use

ERROR: for coredns  Cannot start service coredns: driver failed programming external connectivity on endpoint test-coredns (...): Error starting userland proxy: listen tcp4 0.0.0.0:53: bind: address already in use
ERROR: Encountered errors while bringing up the project.
```

## Solution

### 1. Check `systemd resolve`

```bash
inyong@server:~/dns$ sudo systemctl status systemd-resolved
● systemd-resolved.service - Network Name Resolution
     Loaded: loaded (/lib/systemd/system/systemd-resolved.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2023-08-17 00:32:30 UTC; 5 days ago
       Docs: man:systemd-resolved.service(8)
             man:org.freedesktop.resolve1(5)
             https://www.freedesktop.org/wiki/Software/systemd/writing-network-configuration-managers
             https://www.freedesktop.org/wiki/Software/systemd/writing-resolver-clients
   Main PID: 790 (systemd-resolve)
     Status: "Processing requests..."
      Tasks: 1 (limit: 18891)
     Memory: 8.4M
        CPU: 1.622s
     CGroup: /system.slice/systemd-resolved.service
             └─790 /lib/systemd/systemd-resolved

Aug 17 00:32:30 server systemd[1]: Starting Network Name Resolution...
Aug 17 00:32:30 server systemd-resolved[790]: Positive Trust Anchors:
Aug 17 00:32:30 server systemd-resolved[790]: . IN DS 20326 8 2 ...
Aug 17 00:32:30 server systemd-resolved[790]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20>
Aug 17 00:32:30 server systemd-resolved[790]: Using system hostname 'server'.
Aug 17 00:32:30 server systemd[1]: Started Network Name Resolution.
Aug 17 00:40:54 server systemd-resolved[790]: Clock change detected. Flushing caches.
log file: sudo system
```

### 2. Stop `systemd-resolved`

```Bash
inyong@server:~/dns$ sudo systemctl status systemd-resolved
○ systemd-resolved.service - Network Name Resolution
     Loaded: loaded (/lib/systemd/system/systemd-resolved.service; enabled; vendor preset: enabled)
     Active: inactive (dead) since Tue 2023-08-22 06:42:16 UTC; 2s ago
       Docs: man:systemd-resolved.service(8)
             man:org.freedesktop.resolve1(5)
             https://www.freedesktop.org/wiki/Software/systemd/writing-network-configuration-managers
             https://www.freedesktop.org/wiki/Software/systemd/writing-resolver-clients
    Process: 790 ExecStart=/lib/systemd/systemd-resolved (code=exited, status=0/SUCCESS)
   Main PID: 790 (code=exited, status=0/SUCCESS)
     Status: "Shutting down..."
        CPU: 1.628s

Aug 17 00:32:30 server systemd-resolved[790]: Positive Trust Anchors:
Aug 17 00:32:30 server systemd-resolved[790]: . IN DS 20326 8 2 ...
Aug 17 00:32:30 server systemd-resolved[790]: Negative trust anchors: home.arpa 10.in-addr.arpa 16.172.in-addr.arpa 17.172.in-addr.arpa 18.172.in-addr.arpa 19.172.in-addr.arpa 20>
Aug 17 00:32:30 server systemd-resolved[790]: Using system hostname 'server'.
Aug 17 00:32:30 server systemd[1]: Started Network Name Resolution.
Aug 17 00:40:54 server systemd-resolved[790]: Clock change detected. Flushing caches.
Aug 22 06:42:16 server systemd[1]: Stopping Network Name Resolution...
Aug 22 06:42:16 server systemd[1]: systemd-resolved.service: Deactivated successfully.
Aug 22 06:42:16 server systemd[1]: Stopped Network Name Resolution.
Aug 22 06:42:16 server systemd[1]: systemd-resolved.service: Consumed 1.628s CPU time.
```

### 3. Disable `systemd-resolved`

```Bash
inyong@server:~/dns$ sudo systemctl disable systemd-resolved
Removed /etc/systemd/system/multi-user.target.wants/systemd-resolved.service.
Removed /etc/systemd/system/dbus-org.freedesktop.resolve1.service.
```

### :tada:

```Bash
inyong@server:~/dns$ docker-compose up -d
Starting test-coredns ... done
```

---

### Reference
- GitHub Issue, https://github.com/sameersbn/docker-bind/issues/65, 2023-08-22-Tue.
