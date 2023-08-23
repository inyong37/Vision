# Delete a Container

## Date

2023-04-13-Thursday.

2023-08-23-Wednesday.

## Environment

* Ubuntu 22.04.4 LTS
  * Docker 23.0.3
* Ubuntu 22.04.3 LTS
  * Docker 24.0.5 

## Delete a Container

1. List containers: `docker ps -a`

```Bash
inyong@server:~$ docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                          PORTS     NAMES
1d981df57d12   coredns/coredns                       "/coredns -dns.port=…"   19 hours ago   Restarting (1) 41 seconds ago             test-coredns
```

2. Stop the container: `docker stop {container_name or container_id}`

```Bash
inyong@server:~$ docker stop 1d981df57d12
1d981df57d12
inyong@server:~$ docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                      PORTS     NAMES
1d981df57d12   coredns/coredns                       "/coredns -dns.port=…"   19 hours ago   Exited (1) 58 seconds ago             test-coredns
```

3. Remove the container: `docker rm {container_name or container_id}`

```Bash
inyong@server:~$ docker rm 1d981df57d12
1d981df57d12
inyong@server:~$ docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED        STATUS                      PORTS     NAMES
```
