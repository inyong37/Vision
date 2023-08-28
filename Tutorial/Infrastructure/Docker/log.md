# Log

## Date

2023-08-28-Monday.

## Environment

* Ubuntu 22.04.3 LTS
  * Docker 24.0.5
  * Docker Compose 2.20.2

* Ubuntu 20.04.4 LTS
  * Docker 24.0.5
  * Docker Compose 2.20.2

## Check the container's log

Location: `/var/lib/docker/containers/{container_id}/{container_id}-json.log`

## Log Rotation

### A. Configure Docker Daemon

Location: `/etc/docker/daemon.json`

```json
{
  "log-driver": "json-file"
  "log-opts": {
    "max-size": "10m",
    "max-file": 10
  }
}
```

Restart: `sudo systemctl restart docker`

### B. Start Option

```bash
docker run -d \
--log-driver json-file \
--log-opt max-size=10m \
--log-opt max-file=10 \
--name gitlab-runner --restart always \
-v /data/gitlab-runner/config:/etc/gitlab-runner \
-v /var/run/docker.sock:/var/run/docker.sock \
gitlab/gitlab-runner:v15.6.0
```

### C. Configure Docker Compose

File: `docker-compose.yml`

```yml
version: '3.9'

services:
  gitlab:
    image: 'gitlab/gitlab-ee:15.54-ee.0'
    container_name: gitlab
    restart: always
    hostname: 'gitlab'
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'https://gitlab.example.com'
...
  ports:
    - '80:80'
    - '433:433'
    - '8022:22'
  volumes:
    - './config:/etc/gitlab'
    - './logs:/var/log/gitlab'
    - './data:/var/opt/gitlab'
  logging:
    driver: 'json-file'
    options:
      max-size: '10m'
      max-file: '10'
```

---

### Reference
- Docker logging driver Blog KR, https://insight.infograb.net/blog/2022/11/22/docker-logging-driver/, 2023-08-28-Mon.
