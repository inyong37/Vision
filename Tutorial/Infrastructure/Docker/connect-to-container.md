# Connect to Container

## Date

2023-08-22-Tuesday.

## Environment

* Ubuntu 22.04.3 LTS
  * Docker 24.0.5
 
## Connect to Container

### List Container IDs: `docker ps -a`

```Bash
inyong@server:~/dns$ docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS                         PORTS     NAMES
...
```

### Connect to the Container: `docker exec -it {container_id} /bin/bash`

---

### Reference
- Connect to a Container Blog KR, https://bluese05.tistory.com/21, 2023-08-22-Tue.
