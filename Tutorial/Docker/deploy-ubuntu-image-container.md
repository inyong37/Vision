# Deploy 'Ubuntu' Image Container

## Date

2022-10-27-Thursday.

2023-04-07-Friday.

## Environment

Ubuntu 20.04.4 LTS

## Deploy 'Ubuntu' Image Container

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

---

### Reference
- Ubuntu Container Image Blog KR, https://sleepyeyes.tistory.com/67, 2022-10-27-Thu.
