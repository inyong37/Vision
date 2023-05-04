# Setup APM (Apache PHP MariaDB)

## Date

2023-05-03-Wednesday.

## Environment

Fedora 37 (Bare Metal Machine)

## Setup APM

### 0. Check Environment

Check OS:

```Bash
cat /etc/redhat-release
# Fedora release 37 (Thirty Seven)
```

Check Kernel:

```Bash
cat /proc/version
# Linux version 6.0.7-301.fc37.x86_64 (mockbuild@bkernel01.iad2.fedoraproject.org) (gcc (GCC) 12.2.1 20220819 (Red Hat 12.2.1-2), GNU ld version 2.38-24.fc37) #1 SMP PREEMPT_DYNAMIC Fri Nov 4 18:35:48 UTC 2022
```

### 1. Install Packages

```Bash
yum install -y libjpeg* libpng* freetype* gd-* gcc gcc-c++ gdbm-devel libtermcap-devel
```

### 2. Install Apache

```Bash
yum install -y httpd
```

### 3. Install MariaDB

```Bash
yum install -y mariadb mariadb-server
```

### 4. Install PHP

```Bash
yum install -y php php-common php-mysqlnd php-mbstring php-pdo php-gd php-xml php-json
```

Check APM:

```Bash
rpm -qa httpd mariadb php
# httpd-2.4.57-1.fc37.x86_64
# mariadb-10.5.18-1.fc37.x86_64
# php-8.1.18-1.fc37.x86_64
```

### 5. Start Services

```Bash
systemctl start httpd
systemctl enable httpd
systemctl start mariadb
systemctl enable mariadb
```

### 6. Open a Firewall

```Bash
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --reload
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
# iptables -vnL
```

Edit `/etc/sysconfig/selinux` :

Before:

```Bash
...
SELINUX=enforcing
...
```

After:

```Bash
...
SELINUX=disabled
...
```

### 7. Edit Apache Configuration

Edit `/etc/httpd/conf/httpd.conf`:

Before:

```conf
...
#ServerName www.example.com:80
...
```

After:

```Bash
ServerName {server_name}:80
```

### 8. Edit a PHP File

A. Go to a Workspace

```Bash
cd /var/www/html/
```

B. Make new php file

```Bash
echo "Hello World! by Inyong" > /var/www/html/index.php
```

### 9. Restart Apache

```Bash
systemctl restart httpd
```

### :tada: Verify `http://{server_name}/index.php`

```Bash
curl http://{server_name}/index.php
```

Output:

```Bash
Hello World! by Inyong
Made with APM
```

---

### Reference
- Setup APM Blog KR, https://wlsvud84.tistory.com/16, 2023-05-03-Wed.
- Install PHP on Fedora, https://tecadmin.net/install-lamp-on-fedora/, 2023-05-03-Wed.
