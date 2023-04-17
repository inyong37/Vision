# Docker Commit

## Date

2023-04-17-Monday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS

## Docker Commit

0-A. Check containers:

```Bash
docker ps
```

Output:

```Bash
CONTAINER ID   IMAGE                      COMMAND       CREATED      STATUS      PORTS     NAMES
af6be2f1204d   flatpak-repository:0.0.1   "/bin/bash"   2 days ago   Up 2 days             repo-con
```

0-B. Check images:

```Bash
docker images
```

Output:

```Bash
REPOSITORY                                     TAG       IMAGE ID       CREATED        SIZE
flatpak-repository                             0.0.1     ecb5a13275a6   3 days ago     5.95GB
```

1. Commit

```Bash
docker commit {container_id or container_name} {image_name}:{tag}
# docker commit repo-con flatpak-repository:0.0.2
```

Verify:

```Bash
docker images
```

Output:

```Bash
REPOSITORY                                     TAG       IMAGE ID       CREATED          SIZE
flatpak-repository                             0.0.2     c409fd815284   19 seconds ago   6.04GB
flatpak-repository                             0.0.1     ecb5a13275a6   3 days ago       5.95GB
```
