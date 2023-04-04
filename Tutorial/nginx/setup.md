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

### Set Configuration

```Bash
sudo vim /etc/nginx/nginx.conf # Fedora
# sudo vim /etc/nginx/sites-enables/default # Debian
```

A. Changing a port:

```conf
  server {
    listen 12345;
    listen [::]:12345;
  }
```

```Bash
sudo systemctl restart nginx
```

Check changed port:

```Bash
sudo netstat -tlpn | grep nginx
> tcp        0      0 0.0.0.0:12345           0.0.0.0:*               LISTEN      137648/nginx: maste
> tcp6       0      0 :::12345                :::*                    LISTEN      137648/nginx: maste
sudo ss -tlpn | grep nginx
> LISTEN 0      511          0.0.0.0:12345      0.0.0.0:*    users:(("nginx",pid=137660,fd=8),("nginx",pid=137659,fd=8),("nginx",pid=137658,fd=8),("nginx",pid=137657,fd=8),("nginx",pid=137656,fd=8),("nginx",pid=137655,fd=8),("nginx",pid=137654,fd=8),("nginx",pid=137653,fd=8),("nginx",pid=137652,fd=8),("nginx",pid=137651,fd=8),("nginx",pid=137650,fd=8),("ngin
x",pid=137649,fd=8),("nginx",pid=137648,fd=8))                                                                                                         > LISTEN 0      511             [::]:12345         [::]:*    users:(("nginx",pid=137660,fd=9),("nginx",pid=137659,fd=9),("nginx",pid=137658,fd=9),("nginx",pid=137657,fd=9),("nginx",pid=137656,fd=9),("nginx",pid=137655,fd=9),("nginx",pid=137654,fd=9),("nginx",pid=137653,fd=9),("nginx",pid=137652,fd=9),("nginx",pid=137651,fd=9),("nginx",pid=137650,fd=9),("nginx",pid=137649,fd=9),("nginx",pid=137648,fd=9))
```

Bind the port

```Bash
sudo yum install -y policycoreutils
sudo semanage port -a -t http_port_t -p tcp 12345
sudo semanage port -m -t http_port_t -p tcp 12345
sudo systemctl restart nginx
```

Check:

```Bash
sudo netstat -tlpn | grep nginx
> tcp        0      0 0.0.0.0:12345           0.0.0.0:*               LISTEN      137776/nginx: maste
> tcp6       0      0 :::12345                :::*                    LISTEN      137776/nginx: maste
sudo ss -tlpn | grep nginx
> LISTEN 0      511          0.0.0.0:12345      0.0.0.0:*    users:(("nginx",pid=137788,fd=8),("nginx",pid=137787,fd=8),("nginx",pid=137786,fd=8),("nginx",pid=137785,fd=8),("nginx",pid=137784,fd=8),("nginx",pid=137783,fd=8),("nginx",pid=137782,fd=8),("nginx",pid=137781,fd=8),("nginx",pid=137780,fd=8),("nginx",pid=137779,fd=8),("nginx",pid=137778,fd=8),("nginx",pid=137777,fd=8),("nginx",pid=137776,fd=8))
> LISTEN 0      511             [::]:12345         [::]:*    users:(("nginx",pid=137788,fd=9),("nginx",pid=137787,fd=9),("nginx",pid=137786,fd=9),("nginx",pid=137785,fd=9),("nginx",pid=137784,fd=9),("nginx",pid=137783,fd=9),("nginx",pid=137782,fd=9),("nginx",pid=137781,fd=9),("nginx",pid=137780,fd=9),("nginx",pid=137779,fd=9),("nginx",pid=137778,fd=9),("nginx",pid=137777,fd=9),("nginx",pid=137776,fd=9))
```

Check

---

###
- Installing nginx, http://nginx.org/en/docs/install.html, 2023-04-04-Tue.
- Linux packages nginx, http://nginx.org/en/linux_packages.html, 2023-04-04-Tue.
- Guide nginx, http://nginx.org/en/docs/beginners_guide.html, 2023-04-04-Tue.
- Changing Nginx Ports IBM, https://www.ibm.com/docs/en/aspera-shares/1.9?topic=appendix-changing-nginx-ports, 2023-04-04-Tue.
