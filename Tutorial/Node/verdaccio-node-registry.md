# [Setup Node Package Registry "Verdaccio" with Docker] 

## Date

2023-05-15-Monday.

## Environment

Ubuntu 22.04.2 LTS

Docker 23.0.3

## Setup Node Package Registry "Verdaccio" with Docker

### Pull Docker Image Container

```Bash
docker pull verdaccio/verdaccio
# docker run -it --rm --name verdaccio -p 4873:4873 verdaccio/verdaccio
```

```Bash
V_PATH=/path/for/verdaccio; docker run -it --rm --name verdaccio \
  -e "VERDACCIO_PORT=8080" -p 8080:8080 \
  verdaccio/verdaccio
```

---

### Reference
- Install Verdaccio Docker, https://verdaccio.org/docs/docker/, 2023-05-15-Mon.
- Install Verdaccio with Heroku GitHub, https://github.com/juanpicado/verdaccio-heroku-example, 2023-05-15-Mon.
