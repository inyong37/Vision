# postgres command not found

## Date

2023-04-13-Thursday.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS Image

## Problem

```Bash
root@1b0ca2b05e14:~/flat-manager# postgres createuser $(whoami)
bash: postgres: command not found
```

## Solution

Use `sudo -u`:

```Bash
root@1b0ca2b05e14:~/flat-manager# sudo -u postgres createuser $(whoami)
could not change directory to "/root/flat-manager": Permission denied
```
