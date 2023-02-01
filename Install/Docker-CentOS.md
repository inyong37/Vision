# [Install Docker on CentOS](https://docs.docker.com/engine/install/centos/)

Set up the repository:

```Bash
$ sudo yum install -y yum-utils
$ sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

To install the latest version, run:

```Bash
$ sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Start:

```Bash
$ sudo systemctl start docker
```

---

### Reference

- docker, https://docs.docker.com/engine/install/centos/, 2023-01-26-Thu.
