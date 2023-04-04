# Setup nginx

## Date

2023-04-04-Tuesday.

## Environment

Fedora 37

## Setup nginx

### Installing nginx

```Bash
sudo yum install -y yum-utils
```

Create the file as below:

```Bash
sudo vi /etc/yum.repos.d/nginx.repo
```

Contents:

```yml
[nginx-stable]
name=nginx stable repo
baseurl=http://nginx.org/packages/centos/$releasever/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true

[nginx-mainline]
name=nginx mainline repo
baseurl=http://nginx.org/packages/mainline/centos/$releasever/$basearch/
gpgcheck=1
enabled=0
gpgkey=https://nginx.org/keys/nginx_signing.key
module_hotfixes=true
```

```Bash
sudo yum install -y nginx
```

```Bash
sudo systemctl enable nginx.service
sudo systemctl start nginx.service
```

---

###
- Installing nginx, http://nginx.org/en/docs/install.html, 2023-04-04-Tue.
- Linux packages nginx, http://nginx.org/en/linux_packages.html, 2023-04-04-Tue.
- Guide nginx, http://nginx.org/en/docs/beginners_guide.html, 2023-04-04-Tue.
