# Enable 'systemctl'

## Date

2023-04-12-Wednesday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS Image

## Method 1. Enable 'systemctl' on Ubuntu Container

Without 'systemd' installed:

```Bash
root@1b0ca2b05e14:~# systemctl start postgresql
bash: systemctl: command not found
```

Install 'systemd':

```Bash
apt-get update && apt-get install -y systemd
```

After installing 'systemd':

```Bash
root@1b0ca2b05e14:~# systemctl start postgresql
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

The container has to be started with an 'init' system. 'systemctl' is a process that communicates with systemd over dbus. Therefore, 'dbus' and 'systemd' have to be started when container created/runned.

### Setup

```Bash
sudo docker create -it --privileged=true --name u1 ubuntu:22.04 /sbin/init
```

```Bash
sudo docker exec -it u1 /bin/bash
```

```Bash
apt-get update && apt-get install -y systemd
```

## Method 2. Use 'service' instead of 'systemctl'

```Bash
service postgresql start
```

:tada: Output:

```Bash
root@1b0ca2b05e14:/# service postgresql start
 * Starting PostgreSQL 14 database server
```

---

### Reference
- systemctl Blog KR, https://velog.io/@steveloper/Ubuntu-docker-container-%EC%97%90%EC%84%9C-systemctl-%EC%82%AC%EC%9A%A9%EC%8B%9C-%EB%B0%9C%EC%83%9D%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9CSystem-has-not-been-booted-with-systemd-as-init-system-PID-1.-Cant-operate.Failed-to-connect-to-bus-Host-is-down, 2023-04-12-Wed.
- systemctl Blog KR, https://sangchul.kr/290, 2023-04-12-Wed.
- Enable systemctl, https://forums.docker.com/t/systemctl-status-is-not-working-in-my-docker-container/9075, 2023-04-13-Thu.
