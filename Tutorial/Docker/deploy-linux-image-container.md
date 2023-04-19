# Deploy Linux Image Container

## Date

2022-10-27-Thursday.

2023-04-07-Friday.

## Environment

- Ubuntu 20.04.4 LTS
  - Docker version 23.0.4, build f480fb1
  - Ubuntu 22.04.2 LTS Image

- Fedora 37
  - Docker version 23.0.4, build f480fb1
  - Ubuntu 22.04.2 LTS Image

- Ubuntu 22.04.2 LTS
  - Docker version 23.0.3, build 3e7cbfd
  - Fedora 37 Image

## Deploy Linux Image Container

### :bulb: TLDR

```bash
sudo docker pull ubuntu
sudo docker create -it --name u1 ubuntu # without '-it': exited right away
sudo docker start u1
sudo docker exec -it u1 /bin/bash # not attach
exit # in container
sudo docker rm u1
```


### Method A. Step-by-Step

1. Pull an image

```Bash
sudo docker pull {linux_distribution}:{tag}
# sudo docker pull ubuntu # latest
# sudo docker pull ubuntu:20.04
# sudo docker pull ubuntu:22.04
# sudo docker pull fedora # latest
# sudo docker pull fedora:37
```

2. Create a container:

```Bash
sudo docker create -it --name {container_name} {linux_distribution}:{tag}
```

3. Start the container:

```Bash
sudo docker start {container_name}
```

4. Connect the container:

```Bash
sudo docker exec -it {container_name} /bin/bash
```

Appendix.A. Exit from the container:

```Bash
exit
```

Appendix.B. Stop the container:

```Bash
sudo docker stop {container_name}
```

Appendix.C. Remove the container:

```Bash
sudo docker rm {container_name}
```

Appendix.D. Remove the Image:

```Bash
sudo docker rmi {image_name}:{tag}
sudo docker image rm {image_name}:{tag}
```

### Method 2. Run

```bash
sudo docker run it name u1 ubuntu # attach
# KEY: CONTROL & P or CONTROL & Q # in container
```

---

### Reference
- Ubuntu Container Image Blog KR, https://sleepyeyes.tistory.com/67, 2022-10-27-Thu.
