# iptables unknown option "--dport"

## Date

2023-04-13-Thu.

## Environment

Ubuntu 20.04.4 LTS

Docker 23.0.3

Ubuntu 22.04.2 LTS

## Problem

```Bash
root@1b0ca2b05e14:~/flat-manager# sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
iptables v1.8.7 (nf_tables): unknown option "--dport"
Try `iptables -h' or 'iptables --help' for more information.
```

## Solution

```Bash

```
