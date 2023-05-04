# Setup Nginx

## Date

2023-04-04-Tuesday.

## Environment

Fedora 37 (Bare Metal Machine)

## Setup Nginx

### 0. Install a Package

```Bash
yum install -y yum-utils
```

### 1. Setup a Nginx Repository

```Bash
vim /etc/yum.repos.d/nginx.repo
```

Contents:

```yaml
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

### 2. Install Nginx

```Bash
yum install -y nginx
```

### 3. Start a Service

```Bash
systemctl start nginx
systemctl enable nginx
```

### 4. Set a Directory

```Bash
mkdir -p /ncp/data/www
chown -R nginx:nginx /ncp/data/www
cp /usr/share/nginx/html/index.html /ncp/data/www/index.html
ls -al /ncp/data/www
```

### 5. Set a Configuration

```Bash
vim /etc/nginx/nginx.conf # Fedora
# vim /etc/nginx/sites-enables/default # Debian
```

A. Setup port and server name:

Before:

```conf
...
    server {
        listen       80;
        listen       [::]:80;
        server_name  _;
        root         /usr/share/nginx/html;
...
```

After:

```conf
...
    server {
        listen       {port_number}; # 12345
        listen       [::]:{port_number}; # 12345
        server_name  {server_name}; # localhost
...
```

Restart the service:

```Bash
systemctl restart nginx
```

FYI: Check changed port:

```Bash
netstat -tlpn | grep nginx
```

Output:

```Bash
tcp        0      0 0.0.0.0:12345           0.0.0.0:*               LISTEN      137648/nginx: maste
tcp6       0      0 :::12345                :::*                    LISTEN      137648/nginx: maste
```

```Bash
ss -tlpn | grep nginx
```

Output:

```Bash
LISTEN 0      511          0.0.0.0:12345      0.0.0.0:*    users:(("nginx",pid=137660,fd=8),("nginx",pid=137659,fd=8),("nginx",pid=137658,fd=8),("nginx",pid=137657,fd=8),("nginx",pid=137656,fd=8),("nginx",pid=137655,fd=8),("nginx",pid=137654,fd=8),("nginx",pid=137653,fd=8),("nginx",pid=137652,fd=8),("nginx",pid=137651,fd=8),("nginx",pid=137650,fd=8),("nginx",pid=137649,fd=8),("nginx",pid=137648,fd=8))                     
LISTEN 0      511             [::]:12345         [::]:*    users:(("nginx",pid=137660,fd=9),("nginx",pid=137659,fd=9),("nginx",pid=137658,fd=9),("nginx",pid=137657,fd=9),("nginx",pid=137656,fd=9),("nginx",pid=137655,fd=9),("nginx",pid=137654,fd=9),("nginx",pid=137653,fd=9),("nginx",pid=137652,fd=9),("nginx",pid=137651,fd=9),("nginx",pid=137650,fd=9),("nginx",pid=137649,fd=9),("nginx",pid=137648,fd=9))
```

Bind the port:

```Bash
yum install -y policycoreutils
semanage port -a -t http_port_t -p tcp 12345
semanage port -m -t http_port_t -p tcp 12345
systemctl restart nginx
```

Check:

```Bash
netstat -tlpn | grep nginx
```

Output:

```Bash
tcp        0      0 0.0.0.0:12345           0.0.0.0:*               LISTEN      137776/nginx: maste
tcp6       0      0 :::12345                :::*                    LISTEN      137776/nginx: maste
```

Check:

```Bash
ss -tlpn | grep nginx
```

Output:

```Bash
LISTEN 0      511          0.0.0.0:12345      0.0.0.0:*    users:(("nginx",pid=137788,fd=8),("nginx",pid=137787,fd=8),("nginx",pid=137786,fd=8),("nginx",pid=137785,fd=8),("nginx",pid=137784,fd=8),("nginx",pid=137783,fd=8),("nginx",pid=137782,fd=8),("nginx",pid=137781,fd=8),("nginx",pid=137780,fd=8),("nginx",pid=137779,fd=8),("nginx",pid=137778,fd=8),("nginx",pid=137777,fd=8),("nginx",pid=137776,fd=8))
LISTEN 0      511             [::]:12345         [::]:*    users:(("nginx",pid=137788,fd=9),("nginx",pid=137787,fd=9),("nginx",pid=137786,fd=9),("nginx",pid=137785,fd=9),("nginx",pid=137784,fd=9),("nginx",pid=137783,fd=9),("nginx",pid=137782,fd=9),("nginx",pid=137781,fd=9),("nginx",pid=137780,fd=9),("nginx",pid=137779,fd=9),("nginx",pid=137778,fd=9),("nginx",pid=137777,fd=9),("nginx",pid=137776,fd=9))
```

### 6. Edit a Homepage

```Bash
mv /usr/share/nginx/html/index.html /usr/share/nginx/html/index.html.backup
vim /usr/share/nginx/html/index.html
```

```html
Hello World! by Inyong
Made with Nginx
```

Restart Nginx:

```Bash
systemctl restart nginx
```

### :tada: Verify

```Bash
curl {server_name}:{port_number}
# curl localhost:12345
```

Output:

```Bash
Hello World! by Inyong
Made with Ngnix
```

---

### Reference
- Setup Nginx CentOS Blog KR, https://docs.3rdeyesys.com/compute/ncloud_compute_lemp_nginx_install_setting_centos_guide.html#yum-%EC%9C%A0%ED%8B%B8%EB%A6%AC%ED%8B%B0-%EC%84%A4%EC%B9%98, 2023-05-03-Wed.
- Installing nginx, http://nginx.org/en/docs/install.html, 2023-04-04-Tue.
- Linux packages nginx, http://nginx.org/en/linux_packages.html, 2023-04-04-Tue.
- Guide nginx, http://nginx.org/en/docs/beginners_guide.html, 2023-04-04-Tue.
- Changing Nginx Ports IBM, https://www.ibm.com/docs/en/aspera-shares/1.9?topic=appendix-changing-nginx-ports, 2023-04-04-Tue.
