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
apt-get install -y php-cli php-json php-curl php-imap php-gd php-mysql php-xml php-zip php-intl php-imagick php-mbstring php-fpm
```

Start PHP service

```Bash
systemctl start php8.1-fpm.service
systemctl enable php8.1-fpm.service
```

### 5. Configure PHP for Nextcloud

Make `/etc/php/8.1/fpm/pool.d/nextcloud.conf` file:

```Bash
[nextcloud]
listen = /var/run/nextcloud.sock
 
listen.owner = nextcloud
listen.group = www-data
 
user = nextcloud
group = www-data
 
pm = ondemand
pm.max_children = 30
pm.process_idle_timeout = 60s
pm.max_requests = 500
 
env[HOSTNAME] = $HOSTNAME
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp
```

Restart php service:

```Bash
systemctl restart php8.1-fpm.service
```

### 6. Install MariaDB

```Bash
apt-get install -y mariadb-server mariadb-client
```

Install DB:

```Bash
mysql_secure_installation
```

### 7. Configure DB for Nextcloud

Login to DB:

```Bash
mysql -u root -p
```

Configure DB with password `PASSWORD`:

```mysql
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 40
Server version: 10.6.12-MariaDB-0ubuntu0.22.04.1 Ubuntu 22.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE nextcloud;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> CREATE USER "nextcloud"@"localhost";
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> SET password FOR "nextcloud"@"localhost" = password('[PASSWORD]');
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON nextcloud.* TO "nextcloud"@"localhost" IDENTIFIED BY "[PASSWORD]";
Query OK, 0 rows affected (0.002 sec)

MariaDB [(none)]> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.001 sec)

MariaDB [(none)]> EXIT
Bye
```

### 8. Configure Nextcloud

Make `/etc/nginx/sites-available/nextcloud` file:

```conf
upstream php-handler {

    server unix:/var/run/nextcloud.sock;
}

server {

    listen 80;
    listen [::]:80;
    server_name {server_name};

    root /var/www/nextcloud/;

    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
    add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains;';

    location = /robots.txt {

        allow all;
        log_not_found off;
        access_log off;
    }

    location = /.well-known/carddav {

        return 301 $scheme://$host/remote.php/dav;
    }

    location = /.well-known/caldav {

        return 301 $scheme://$host/remote.php/dav;
    }

    client_max_body_size 512M;
    fastcgi_buffers 64 4K;

    gzip on;
    gzip_vary on;
    gzip_comp_level 4;
    gzip_min_length 256;
    gzip_proxied expired no-cache no-store private no_last_modified no_etag auth;
    gzip_types application/atom+xml application/javascript application/json application/ld+json application/manifest+json application/rss+xml application/vnd.geo+json application/vnd.ms-fontobject application/x-font-ttf application/x-web-app-manifest+json application/xhtml+xml application/xml font/opentype image/bmp image/svg+xml image/x-icon text/cache-manifest text/css text/plain text/vcard text/vnd.rim.location.xloc text/vtt text/x-component text/x-cross-domain-policy;

    location / {

        rewrite ^ /index.php$uri;
    }

    location ~ ^/.well-known/acme-challenge/* {

        allow all;
    }

    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)/ {

        deny all;
    }

    location ~ ^/(?:\.|autotest|occ|issue|indie|db_|console) {

        deny all;
    }

    location ~ ^/(?:index|remote|public|cron|core/ajax/update|status|ocs/v[12]|updater/.+|ocs-provider/.+)\.php(?:$|/) {

        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_param modHeadersAvailable true;
        fastcgi_param front_controller_active true;
        fastcgi_pass php-handler;
        fastcgi_intercept_errors on;
        fastcgi_request_buffering off;
    }

    location ~ ^/(?:updater|ocs-provider)(?:$|/) {

        try_files $uri/ =404;
        index index.php;
    }

    location ~* \.(?:css|js|woff|svg|gif)$ {

        try_files $uri /index.php$uri$is_args$args;
        add_header Cache-Control "public, max-age=7200";
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection "1; mode=block";
        add_header X-Robots-Tag none;
        add_header X-Download-Options noopen;
        add_header X-Permitted-Cross-Domain-Policies none;

        access_log off;
    }

    location ~* \.(?:png|html|ttf|ico|jpg|jpeg)$ {

        try_files $uri /index.php$uri$is_args$args;
        access_log off;
    }
}
```

Verify:

```Bash
ln -s /etc/nginx/sites-available/nextcloud /etc/nginx/sites-enabled/nextcloud
nginx -t
```

Output:

```Bash
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Restart services:

```Bash
systemctl restart nginx
systemctl restart php8.1-fpm
```

### 9. Certificate Let's Encrypt

```Bash
apt-get install -y certbot
certbot certonly --webroot -w /var/www/nextcloud --agree-tos --email {email} -d {domain} --rsa-key-size 4096
openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096
chmod 600 /etc/ssl/certs/dhparam.pem
```

### 10. Configure SSL

Edit `/etc/nginx/sites-available/nextcloud`:

Make new server for 443 port.

After:

```conf
...
server {

    listen 80;
    listen [::]:80;
    server_name {server_name};
    return 301 https://$server_name$request_uri;
}

server {

    listen 443 ssl;
    listen [::]:443 ssl;
    server_name {server_name};
    root /var/www/nextcloud;
    
    ssl on;
    ssl_certificate /etc/letsencrypt/live/{server_name}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{server_name}/privkey.pem;
    ssl_dhparam /etc/ssl/certs/dhparam.pem;

    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout 1440m;
    ssl_buffer_size 8k;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;

    ssl_ciphers 'kEECDH+ECDSA+AES128 kEECDH+ECDSA+AES256 kEECDH+AES128 kEECDH+AES256 kEDH+AES128 kEDH+AES256 DES-CBC3-SHA +SHA !aNULL !eNULL !LOW !kECDH !DSS !MD5 !EXP !PSK !SRP !CAMELLIA !SEED';
    ssl_prefer_server_ciphers on;

    ssl_trusted_certificate /etc/letsencrypt/live/{server_name}/chain.pem;
    ssl_stapling on;
    ssl_stapling_verify on;

    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Robots-Tag none;
    add_header X-Download-Options noopen;
    add_header X-Permitted-Cross-Domain-Policies none;
    add_header Strict-Transport-Security 'max-age=31536000; includeSubDomains;';
    
    location = /robots.txt {
...
```

Reload Nginx:

```Bash
systemctl reload nginx.service
```

---

### Reference
- Install Nextcloud Ubuntu Blog KR, https://velog.io/@windsekirun/%EC%A0%9C%EB%A1%9C%EB%B6%80%ED%84%B0-%EC%8B%9C%EC%9E%91%ED%95%98%EB%8A%94-NextCloud-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0-on-VPS, 2023-05-04-Thu.
- Install Certbot, https://eff-certbot.readthedocs.io/en/stable/install.html, 2023-05-04-Thu.
- Let's Encrypt Blog KR, https://velog.io/@chldppwls12/Lets-Encrypt-SSL-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EB%B0%9C%EA%B8%89-%EB%B0%8F-%EA%B0%B1%EC%8B%A0, 2023-05-04-Thu.
