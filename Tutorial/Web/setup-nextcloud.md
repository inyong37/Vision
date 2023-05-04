# Setup Nextcloud

## Date

2023-05-04-Thursday.

## Environment

Ubuntu 22.04.1 LTS

## Setup Nextcloud

### 0. Install a Package

```Bash
apt-get install -y  unzip
```

### 1. Install Nginx

```Bash
apt-get install -y nginx
```

```Bash
systemctl start nginx
systemctl enable nginx
```

### 2. Configure Nginx

Edit `vim /etc/nginx/nginx.conf`:

Before:

```conf
...
  # server_tokens off;
...
```

After:

```conf
...
  server_tokens off;
...
```

Restart Nginx:

```Bash
systemctl restart nginx
```

### 3. Install Nextcloud

```Bash
cd /var/www
wget https://download.nextcloud.com/server/releases/nextcloud-12.0.3.zip
unzip nextcloud-12.0.3.zip
rm -rf nextcloud-12.0.3.zip
```

Set `nextcloud` user:

```Bash
adduser nextcloud
chown -R nextcloud:www-data /var/www/nextcloud
chmod -R o-rwx /var/www/nextcloud
```

### 4. Install PHP

```Bash
VERSION=7.1
apt-get install -y php-cli=$VERSON php-json php-curl php-imap php-gd php-mysql php-xml php-zip php-intl php-imagick php-mbstring php-fpm
```

### 5. Configure PHP for Nextcloud

Make `/etc/php/

```Bash

```

---

### Reference
- Install Nextcloud Ubuntu Blog KR, https://velog.io/@windsekirun/%EC%A0%9C%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-NextCloud-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-on-VPS, 2023-05-04-Thu.
