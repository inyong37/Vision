# Set Timezone while building Ubuntu Docker Image

## Date

2023-04-12-Wednesday.

## Environment

Ubuntu 22.04.2 LTS

Docker 23.0.3

## Set Timezone

```Dockerfile
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

RUN apt-get install -y tzdata
```

---

### Reference
- Set Timezone Blog KR, https://stynxh.github.io/2020-07-26-set-timezone-when-ubuntu-docker-image-build/, 2023-04-12-Wed.
