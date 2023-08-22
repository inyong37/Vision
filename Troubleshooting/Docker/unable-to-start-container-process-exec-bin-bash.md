# unable to start container process: exec: "/bin/bash"

## Date

2023-05-17-Wednesday.

## Environment

* Ubuntu 20.04.4 LTS
  * Docker 23.0.6

## Problem

```Bash
(base) root@desktop:~/workspace# docker exec -it 2fa0d13a792c /bin/bash
OCI runtime exec failed: exec failed: unable to start container process: exec: "/bin/bash": stat /bin/bash: no such file or directory: unknown
```

## Solution - Use `sh`

There is no bash binary. You can use sh instead of it.

```Bash
(base) root@desktop:~/workspace# docker exec -it 2fa0d13a792c /bin/sh
~ $
```

---

### Reference
- Error bin bash Blog KR, https://gymcoding.github.io/2020/09/21/docker-error-1/, 2023-05-17-Wed.
