# Deploy Ubuntu Image Container

## Date

2022-10-27-Thursday.

2023-04-07-Friday.

## Environment

Ubuntu 20.04.4 LTS

## Deploy Container

### Method 1

```bash
sudo docker pull ubuntu
sudo docker create -it --name u1 ubuntu # without '-it': exited right away
sudo docker start u1
sudo docker exec -it u1 /bin/bash # not attach
exit # in container
sudo docker rm u1
```

### Method 2

```bash
sudo docker run it name u1 ubuntu # attach
# KEY: CONTROL & P or CONTROL & Q # in container
```

### Enable 'systemctl'

```Bash
System has not been booted with systemd as init system (PID 1). Can't operate.
Failed to connect to bus: Host is down
```

```Bash
sudo docker create -it --privileged=true --name u1 ubuntu:22.04 /sbin/init
```

```Bash
sudo docker exec -it u1 /bin/bash
```

```Bash
apt-get update && apt-get install -y systemd
```

---

### Reference
- Ubuntu Container Image Blog KR, https://sleepyeyes.tistory.com/67, 2022-10-27-Thu.
- systemctl Blog KR, https://velog.io/@steveloper/Ubuntu-docker-container-%EC%97%90%EC%84%9C-systemctl-%EC%82%AC%EC%9A%A9%EC%8B%9C-%EB%B0%9C%EC%83%9D%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9CSystem-has-not-been-booted-with-systemd-as-init-system-PID-1.-Cant-operate.Failed-to-connect-to-bus-Host-is-down, 2023-04-12-Wed.
- systemctl Blog KR, https://sangchul.kr/290, 2023-04-12-Wed.
