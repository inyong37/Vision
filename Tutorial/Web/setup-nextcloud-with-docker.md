# Setup Nextcloud on Docker

## Date

2023-05-04-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Setup Nextcloud on Docker

### 1. Install Docker

```Bash
curl -fsSL https://get.docker.com | sudo sh
```

### 2. Pull Nextcloud Image Container

```Bash
docker run \
--sig-proxy=false \
--name nextcloud-aio-mastercontainer \
--restart always \
--publish 80:80 \
--publish 8080:8080 \
--publish 8443:8443 \
--volume nextcloud_aio_mastercontainer:/mnt/docker-aio-config \
--volume /var/run/docker.sock:/var/run/docker.sock:ro \
nextcloud/all-in-one:latest
```

### 3. Setup Nextcloud

Open web browser `https://{ip_address}:8080`

FYI: get password `cat /var/lib/docker/volumes/nextcloud_aio_mastercontainer/_data/data/configuration.json | grep password`

---

### Reference
- Install Nextcloud, https://nextcloud.com/install/, 2023-05-04-Thu.
- Install Nextcloud Docker, https://github.com/nextcloud/all-in-one#how-to-use-this, 2023-05-04-Thu.
- Get Password, https://github.com/nextcloud/all-in-one/discussions/803, 2023-05-04-Thu.
