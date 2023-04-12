# Setup flat-manager

Setup Server of 'flat-manager' for Building and Hosting Flatpak Repository on Fedora 37

:construction: Setup Client of 'flat-manager' for Committing Applications and Publishing Flatpak Repository on Debian 11

## Date

1. ~~2023-03-20-Monday.~~
2. ~~2023-03-22-Wednesday.~~
3. 2023-03-23-Thursday.
4. 2023-03-29-Wednesday.
5. 2023-04-10-Monday.

## Environment

1. ~~Ubuntu 22.04.1 LTS~~
2. ~~CentOS Linux release 7.9.2009 (Core)~~
3. Fedora 37 with User Authority
4. Debian GNU/Linux 11 (bullseye) with User Authority
5. Ubuntu 22.04.02 LTS & Docker Image/Contiainer with Root Authority

## 5. [Install Server of flat-manager for Building and Publishing Repository on Ubuntu 22 Container]

## 4. [Install Server of flat-manager for Building and Publishing Repository on Debian 11](debian-user-flat-manager.sh)

## 3. [Install Server of flat-manager for Building and Publishing Flatpak Repository on Fedora 37](fedora-user-flat-manager.sh)

1. [Install Rust](https://doc.rust-lang.org/book/ch01-01-installation.html):

```Bash
cd $HOME
curl https://sh.rustup.rs -sSf | sh -s -- -y
source "$HOME/.cargo/env"
```

2. Install Package Manager DNF and Packages; cargo, postgresql, ostree, git, and tmux:

:bulb: `ostree`: command `ostree` didn't installed via installing 'ostree-devel'

```Bash
sudo yum install -y dnf
sudo dnf install -y cargo postgresql-devel ostree-devel ostree git tmux
```

3. Build "flat-manager":

```Bash
cd $HOME
git clone https://github.com/flatpak/flat-manager.git
cd flat-manager
cargo build
```

:tada: Building successed without any errors:

```Bash
    Finished dev [unoptimized + debuginfo] target(s) in 2m 16s
warning: the following packages contain code that will be rejected by a future version of Rust: nom v4.2.3
note: to see what the problems were, use the option `--future-incompat-report`, or run `cargo report future-incompatibilities --id 1`
```

4. Start Database:

```Bash
sudo dnf install -y postgresql-server postgresql-contrib
sudo systemctl enable postgresql
sudo postgresql-setup --initdb --unit postgresql
sudo systemctl start postgresql
sudo -u postgres createuser $(whoami)
sudo -u postgres createdb --owner=$(whoami) repo
```

5. Build the Repository Server:

```Bash
cp example.env .env
cp example-config.json config.json
ostree --repo=repo init --mode=archive-z2
ostree --repo=beta-repo init --mode=archive-z2
mkdir build-repo
export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name testtoken)
```

:tada: Output:

```Bash
    Finished dev [unoptimized + debuginfo] target(s) in 0.18s
warning: the following packages contain code that will be rejected by a future version of Rust: nom v4.2.3
note: to see what the problems were, use the option `--future-incompat-report`, or run `cargo report future-incompatibilities --id 2`
     Running `target/debug/gentoken --base64 --secret-file - --name testtoken`
```

6. Run the Repository Server

```Bash
cargo run --bin flat-manager
```

:tada: Output:

```
    Finished dev [unoptimized + debuginfo] target(s) in 0.18s
warning: the following packages contain code that will be rejected by a future version of Rust: nom v4.2.3
note: to see what the problems were, use the option `--future-incompat-report`, or run `cargo report future-incompatibilities --id 3`
     Running `target/debug/flat-manager`
Running migration 20181023152211
Running migration 20181023152228
Running migration 20181023152240
Running migration 20181102103939
Running migration 20190124101838
Running migration 20190204135447
Running migration 20190307075207
Running migration 20190307094436
Running migration 20220805212616
Running migration 20220906002415
Running migration 20221214225546
[2023-03-27T02:16:53Z INFO  actix_server::builder] Starting 12 workers
[2023-03-27T02:16:53Z INFO  actix_server::builder] Starting server on 127.0.0.1:8080
[2023-03-27T02:16:53Z INFO  flatmanager::app] Started http server: 127.0.0.1:8080
```

7. Enable Port

```Bash
sudo iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
sudo setenforce 0
```

8. [Tunnel the Server via Ngrok (KR)](https://blog.outsider.ne.kr/1159):

```Bash
cd $HOME
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar xvzf ngrok-v3-stable-linux-amd64.tgz -C /usr/local/bin
cd /usr/local/bin
sudo chmod 755 ngrok
ngrok http 8080
```

A. [Install](https://fedoraproject.org/wiki/Cryptography) and [Make a GPG Key](https://fedoraproject.org/wiki/Creating_GPG_Keys):

```Bash
[root@node77 ~]# dnf install -y gnupg
Last metadata expiration check: 2:29:07 ago on Mon 27 Mar 2023 09:25:17 AM KST.
Package gnupg2-2.3.7-3.fc37.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[root@node77 ~]# gpg2 --full-gen-key
gpg (GnuPG) 2.3.7; Copyright (C) 2021 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: directory '/root/.gnupg' created
gpg: keybox '/root/.gnupg/pubring.kbx' created
Please select what kind of key you want:
   (1) RSA and RSA
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
   (9) ECC (sign and encrypt) *default*
  (10) ECC (sign only)
  (14) Existing key from card
Your selection? 1
RSA keys may be between 1024 and 4096 bits long.
What keysize do you want? (3072) 4096
Requested keysize is 4096 bits
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 0
Key does not expire at all
Is this correct? (y/N) y

GnuPG needs to construct a user ID to identify your key.

Real name: user
Email address: 
Comment: test
You selected this USER-ID:
    "user (test) <>"

Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: agent_genkey failed: No pinentry
Key generation failed: No pinentry
```

### Commit Local Repository to Remote Repository on 'flat-manager' installed Fedora 37 Machine

Build 

```Bash
export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name test)
# ./flat-manager-client push --commit $(./flat-manager-client create http://127.0.0.1:8080 stable) {application}/{local_repo}
./flat-manager-client push --commit $(./flat-manager-client create http://127.0.0.1:8080 stable) flatpak-test/local-repo
```

:tada: Output:

```Bash
Uploading refs to http://127.0.0.1:8080/api/v1/build/6: ['app/org.flatpak.Hello/x86_64/master']
Refs contain 6 metadata objects
Remote missing 6 of those
Has 3 file objects for those
Remote missing 3 of those
Uploading file objects
Uploading 3 files (568 bytes)
Uploading metadata objects
Uploading 6 files (964 bytes)
Uploading deltas
Creating ref app/org.flatpak.Hello/x86_64/master with commit 2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac
Committing build http://127.0.0.1:8080/api/v1/build/6
```

Logs on Server:

```Bash
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55764 "POST /api/v1/build HTTP/1.1" test 200 150 Python/3.11 aiohttp/3.8.4 0.005146
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "GET /api/v1/build/6/missing_objects HTTP/1.1" test 200 462 Python/3.11 aiohttp/3.8.4 0.001893
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "GET /api/v1/build/6/missing_objects HTTP/1.1" test 200 232 Python/3.11 aiohttp/3.8.4 0.000933
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "POST /api/v1/build/6/upload HTTP/1.1" test 200 12 Python/3.11 aiohttp/3.8.4 0.001075
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "POST /api/v1/build/6/upload HTTP/1.1" test 200 21 Python/3.11 aiohttp/3.8.4 0.001363
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "POST /api/v1/build/6/build_ref HTTP/1.1" test 200 146 Python/3.11 aiohttp/3.8.4 0.003728
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "POST /api/v1/build/6/commit HTTP/1.1" test 200 160 Python/3.11 aiohttp/3.8.4 0.002865
[2023-03-30T05:48:58Z INFO  flatmanager::logger] 127.0.0.1:55780 "GET /api/v1/build/6 HTTP/1.1" test 200 168 Python/3.11 aiohttp/3.8.4 0.000987
[2023-03-30T05:48:58Z INFO  flatmanager::jobs::commit_job] #1: Handling Job Commit: build: 6, end-of-life: , eol-rebase: , token-type: None
[2023-03-30T05:48:58Z INFO  flatmanager::jobs::commit_job] #1: Committing ref app/org.flatpak.Hello/x86_64/master (2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac)
[2023-03-30T05:48:58Z ERROR flatmanager::jobs::job_executor] #1: Job failed: InternalError: Failed to run "flatpak" "build-commit-from" "--timestamp=NOW" "--no-update-summary" "--untrusted" "--force" "--disable-fsync" "--src-repo=build-repo/6/upload" "--src-ref=2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac" "build-repo/6" "app/org.flatpak.Hello/x86_64/master": No such file or directory (os error 2)
```

### Committing Local Repository to Remote Repository on 'flatpak' installed Debian 11 Machine

Client #1:

```Bash
inyong@server:~/flat-manager$ export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name test)
  Updating crates.io index
Downloaded quick-error v1.2.3
...
Downloaded trust-dns-proto v0.7.4
Downloaded 323 crates (21.8 MB) in 2.15s (largest was `ring` at 5.1 MB)
  Compiling autocfg v1.1.0
  ...
  Compiling flat-manager v0.4.1 (/home/inyong/flat-manager)
    Finished dev [unoptimized + debuginfo] target(s) in 3m 56s
      Running `target/debug/gentoken --base64 --secret-file - --name test`
```

Client #2:

```Bash
inyong@server:~/flat-manager$ ./flat-manager-client push --commit $(./flat-manager-client create https://{random.ngrok.io} stable) ../flatpak-test/local-repo
Uploading refs to https://{random.ngrok.io}.ngrok.io/api/v1/build/7: ['app/org.flatpak.Hello/x86_64/master']
Refs contain 6 metadata objects
Remote missing 6 of those
Has 3 file objects for those
Remote missing 3 of those
Uploading file objects
Uploading 3 files (568 bytes)
Uploading metadata objects
Uploading 6 files (964 bytes)
Uploading deltas
Creating ref app/org.flatpak.Hello/x86_64/master with commit 2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac
Committing build https://{random.ngrok.io}.ngrok.io/api/v1/build/7
```

Server #1 before installing 'flatpak' on the server machine:

```Bash
[2023-03-30T06:56:31Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build HTTP/1.1" test 200 150 Python/3.10 aiohttp/3.8.1 0.008887
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/7/missing_objects HTTP/1.1" test 200 462 Python/3.10 aiohttp/3.8.1 0.008166
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/7/missing_objects HTTP/1.1" test 200 232 Python/3.10 aiohttp/3.8.1 0.004853
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/7/upload HTTP/1.1" test 200 12 Python/3.10 aiohttp/3.8.1 0.034073
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/7/upload HTTP/1.1" test 200 21 Python/3.10 aiohttp/3.8.1 0.038063
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/7/build_ref HTTP/1.1" test 200 146 Python/3.10 aiohttp/3.8.1 0.008277
[2023-03-30T06:56:32Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/7/commit HTTP/1.1" test 200 160 Python/3.10 aiohttp/3.8.1 0.009280
[2023-03-30T06:56:32Z INFO  flatmanager::jobs::commit_job] #2: Handling Job Commit: build: 7, end-of-life: , eol-rebase: , token-type: None
[2023-03-30T06:56:32Z INFO  flatmanager::jobs::commit_job] #2: Committing ref app/org.flatpak.Hello/x86_64/master (2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac)
[2023-03-30T06:56:32Z ERROR flatmanager::jobs::job_executor] #2: Job failed: InternalError: Failed to run "flatpak" "build-commit-from" "--timestamp=NOW" "--no-update-summary" "--untrusted" "--force" "--disable-fsync" "--src-repo=build-repo/7/upload" "--src-ref=2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac" "build-repo/7" "app/org.flatpak.Hello/x86_64/master": No such file or directory (os error 2)
[2023-03-30T06:56:33Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/7 HTTP/1.1" test 200 556 Python/3.10 aiohttp/3.8.1 0.003020
```

### After Installing 'flatpak' on the Server Machine:

Client #1:

```Bash
inyong@server:~/flat-manager$ ./flat-manager-client push --commit $(./flat-manager-client create https://{random.ngrok.io}.ngrok.io stable) ../flatpak-test/local-repo
Uploading refs to https://{random.ngrok.io}.ngrok.io/api/v1/build/8: ['app/org.flatpak.Hello/x86_64/master']
Refs contain 6 metadata objects
Remote missing 6 of those
Has 3 file objects for those
Remote missing 3 of those
Uploading file objects
Uploading 3 files (568 bytes)
Uploading metadata objects
Uploading 6 files (964 bytes)
Uploading deltas
Creating ref app/org.flatpak.Hello/x86_64/master with commit 2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac
Committing build https://{random.ngrok.io}.ngrok.io/api/v1/build/8
```

Server #1:

```Bash
[2023-03-30T07:20:28Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build HTTP/1.1" test 200 150 Python/3.10 aiohttp/3.8.1 0.008955
[2023-03-30T07:20:28Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/8/missing_objects HTTP/1.1" test 200 462 Python/3.10 aiohttp/3.8.1 0.004631
[2023-03-30T07:20:28Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/8/missing_objects HTTP/1.1" test 200 232 Python/3.10 aiohttp/3.8.1 0.001258
[2023-03-30T07:20:29Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/8/upload HTTP/1.1" test 200 12 Python/3.10 aiohttp/3.8.1 0.036976
[2023-03-30T07:20:29Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/8/upload HTTP/1.1" test 200 21 Python/3.10 aiohttp/3.8.1 0.007179
[2023-03-30T07:20:29Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/8/build_ref HTTP/1.1" test 200 146 Python/3.10 aiohttp/3.8.1 0.008533
[2023-03-30T07:20:29Z INFO  flatmanager::logger] {client_address} "POST /api/v1/build/8/commit HTTP/1.1" test 200 160 Python/3.10 aiohttp/3.8.1 0.009812
[2023-03-30T07:20:29Z INFO  flatmanager::jobs::commit_job] #3: Handling Job Commit: build: 8, end-of-life: , eol-rebase: , token-type: None
[2023-03-30T07:20:29Z INFO  flatmanager::jobs::commit_job] #3: Committing ref app/org.flatpak.Hello/x86_64/master (2b0af3d5191525e896226d34e4eac262cb6b6827e4ef3867ca293d221d33d9ac)
[2023-03-30T07:20:29Z INFO  flatmanager::jobs::commit_job] #3: running build-update-repo
[2023-03-30T07:20:29Z INFO  flatmanager::logger] {client_address} "GET /api/v1/build/8 HTTP/1.1" test 200 168 Python/3.10 aiohttp/3.8.1 0.001322
[2023-03-30T07:20:29Z INFO  flatmanager::jobs::commit_job] #3: Removing upload directory
[2023-03-30T07:20:29Z INFO  flatmanager::jobs::job_executor] #3: Job succeeded
```

## [Setup GPG](https://blogs.gnome.org/alexl/2017/02/10/maintaining-a-flatpak-repository/)

:bulb: Before to start installing packages, shutdown the server. 

```Bash
sudo dnf install -y gnupg pinentry
```

Create a custom key:

```Bash
mkdir gpg
gpg2 --homedir gpg --quick-gen-key {user_name}@{domain}
```

:tada: Output:

```Bash
pub   ed25519 2023-03-31 [SC] [expires: 2025-03-30]
      35752B2F847935C5A822F10FA3EFDAA6552EECBF
uid                      user@example.com
sub   cv25519 2023-03-31 [E]
```

Sign the repo:

```Bash
flatpak build-sign repo --gpg-sign=35752B2F847935C5A822F10FA3EFDAA6552EECBF --gpg-homedir=gpg
```

Sign the summary file:

```Bash
flatpak build-update-repo repo --gpg-sign=35752B2F847935C5A822F10FA3EFDAA6552EECBF --gpg-homedir=gpg
```

Export the public key for the repo:

```Bash
gpg2 --homedir=gpg --export 35752B2F847935C5A822F10FA3EFDAA6552EECBF > example.gpg
```

Use this key instead of `--no-gpg-verify` on user-side:

```Bash
flatpak remote-add --gpg-import=example.gpg example-repo http://example.com/repo
```

---

## ~~2. Install flat-manager for Building Flatpak Repository on CentOS 7~~

All commands were executed on root authority.

```bash
yum install dnf
```

```Bash
curl https://sh.rustup.rs -sSf | sh
...
>
```

Press 'Enter' at `>`

```Bash
dnf install postgresql-devel
```

```Bash
dnf install ostree-devel
```

Install development tools:

```Bash
dnf groupinstall "Development Tools"
```

Clone and build flat-manager

But an error occured:

```Bash
The following warnings were emitted during compilation:

warning: `PKG_CONFIG_ALLOW_SYSTEM_CFLAGS="1" "pkg-config" "--libs" "--cflags" "ostree-1" "ostree-1 >= 2021.5"` did not exit successfully: exit status: 1

error: failed to run custom build command for `ostree-sys v0.10.0`

Caused by:
  process didn't exit successfully: `/root/flat-manager/target/debug/build/ostree-sys-a27872bfc8f84508/build-script-build` (exit status: 1)
  --- stdout
  cargo:rerun-if-env-changed=OSTREE_1_NO_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_PATH
  cargo:rerun-if-env-changed=PKG_CONFIG_PATH
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_LIBDIR
  cargo:rerun-if-env-changed=PKG_CONFIG_LIBDIR
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64-unknown-linux-gnu
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR_x86_64_unknown_linux_gnu
  cargo:rerun-if-env-changed=HOST_PKG_CONFIG_SYSROOT_DIR
  cargo:rerun-if-env-changed=PKG_CONFIG_SYSROOT_DIR
  cargo:warning=`PKG_CONFIG_ALLOW_SYSTEM_CFLAGS="1" "pkg-config" "--libs" "--cflags" "ostree-1" "ostree-1 >= 2021.5"` did not exit successfully: exit status: 1
  error: could not find system library 'ostree-1' required by the 'ostree-sys' crate

  --- stderr
  Requested 'ostree-1 >= 2021.5' but version of OSTree is 2019.1

warning: build failed, waiting for other jobs to finish...
[root@node77 flat-manager]# dnf install ostree-devel
Last metadata expiration check: 0:47:14 ago on Wed 22 Mar 2023 02:14:56 PM KST.
Package ostree-devel-2019.1-2.el7.x86_64 is already installed.
Dependencies resolved.
Nothing to do.
Complete!
```

:bulb: I need ostree version 2021.5 or higher to build this. [However, since Fedora 36, the 2021.5 version is supported.](https://bodhi.fedoraproject.org/updates/?packages=ostree&page=2) [The currently installed OS, CentOS 7, is compatible with Feodra 19 to 27, and CentOS 8 is compatible with Fedora 28.](https://docs.fedoraproject.org/en-US/quick-docs/fedora-and-red-hat-enterprise-linux/index.html) So the flat-manager installation will retry with Fedora 37.

---

## ~~1. Install flat-manager for Building Flatpak Repository on Ubuntu 22~~

All commands were executed on root authority.

```Bash
apt-get install gcc g++ libudev-dev pkg-config file make cmake
apt-get install perl yasm
apt-get install openssl libudev-dev file curl jq
apt-get install build-essential libssl-dev git libclang-dev
apt-get install intltool
apt-get install libglib2.0-dev
apt install gcc-multilib
```

Install cargo:

```Bash
apt install cargo
```

[Install postgresql](https://www.postgresql.org/download/linux/ubuntu/):

```Bash
apt install wget ca-certificates
sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
apt-get update
apt-get -y install postgresql
```

Install ostree:

```Bash
apt install ostree libostree-dev
```

Clone flat-manager:

```Bash
git clone https://github.com/flatpak/flat-manager.git
```

Build:

```Bash
cd {workspace}/flat-manager
cargo build
```

```Bash
Compiling flat-manager v0.4.1 (/root/flat-manager)
error: linking with `cc` failed: exit status: 1
  |
  = note: "cc" "-m64" "/tmp/rustcJTstdJ/symbols.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.167gf0o9o17p7739.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1a69cv5jq7eop9ur.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1an9ziwdjvundh6z.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1gi1wx3vst73l3l9.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1lyem05dzb82hzcg.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1mg1w1uvcyy158aa.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1o5n69z8zathadjt.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1tvhzfz7pa58kdv0.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.1xnul73gfaxrwpl5.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2b97fnqeu5iv5xwz.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2emmt64tl7o3hy80.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2ka5fkr6r7bmjc6s.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2pf33hmuwqnjf9z4.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2qtex0a96c64cl9j.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.2uf8856jx3a0f0co.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.32flyl1ynh2og1e9.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.3791kpfakhjmcd3s.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.3i7odkbeg22cg82n.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.3sguikh6b5iw4cj8.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.3yrjkgutb84v4d9y.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.409gu5nn5v20jv34.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.497tm2abnlemjq05.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.4avt3ivypqf2hwww.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.4jowx7hc0qlln4t5.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.4pyifmlwtadkak53.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.5g7dnqnn31m24j3r.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.gdmwkvd7gzdqh.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.hlm9tl8mexwe66g.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.piqx9fmfibjrqvf.rcgu.o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d.26yo4a44jy3xdz4k.rcgu.o" "-Wl,--as-needed" "-L" "/root/flat-manager/target/debug/deps" "-L" "/root/flat-manager/target/debug/build/brotli-sys-c0a27acabdb9b138/out" "-L" "/usr/lib/x86_64-linux-gnu" "-L" "/root/flat-manager/target/debug/build/ring-565de3fe1e474494/out" "-L" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib" "-Wl,-Bstatic" "/root/flat-manager/target/debug/deps/libflatmanager-2172893fddd9fdd5.rlib" "/root/flat-manager/target/debug/deps/libfiletime-b753758d78df8b7a.rlib" "/root/flat-manager/target/debug/deps/libjsonwebtoken-f396b0c3cdce7429.rlib" "/root/flat-manager/target/debug/deps/libpem-c88437636648ab9c.rlib" "/root/flat-manager/target/debug/deps/libbase64-fdd705b8fb7cffd1.rlib" "/root/flat-manager/target/debug/deps/libbase64-0b88a04759406a00.rlib" "/root/flat-manager/target/debug/deps/libsimple_asn1-d164d2a6ea48eb0d.rlib" "/root/flat-manager/target/debug/deps/libnum_bigint-1d9cdc6a86412ca6.rlib" "/root/flat-manager/target/debug/deps/libring-eecbc6750d6868e1.rlib" "/root/flat-manager/target/debug/deps/libspin-e37c43ddec5eb60c.rlib" "/root/flat-manager/target/debug/deps/libuntrusted-97cd9a69916e3bce.rlib" "/root/flat-manager/target/debug/deps/libtokio_process-944de106a2768294.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_queue-ecadd9c937619b05.rlib" "/root/flat-manager/target/debug/deps/libwalkdir-c46c713b90805ba5.rlib" "/root/flat-manager/target/debug/deps/libsame_file-80c931eaa8c275f9.rlib" "/root/flat-manager/target/debug/deps/libostree-26145448634ad183.rlib" "/root/flat-manager/target/debug/deps/libhex-75c11233f1668394.rlib" "/root/flat-manager/target/debug/deps/libradix64-92915cff80f5aa2d.rlib" "/root/flat-manager/target/debug/deps/libarrayref-f6df4c1ade89c260.rlib" "/root/flat-manager/target/debug/deps/libgio-4bf14f803a068174.rlib" "/root/flat-manager/target/debug/deps/libthiserror-ec9dd2d207d8e730.rlib" "/root/flat-manager/target/debug/deps/libglib-6dbdfe1ca7cd8ae9.rlib" "/root/flat-manager/target/debug/deps/libonce_cell-6b60731e13fb7b3a.rlib" "/root/flat-manager/target/debug/deps/libostree_sys-81ad5610b7e881ca.rlib" "/root/flat-manager/target/debug/deps/libgio_sys-77418b28133dc16b.rlib" "/root/flat-manager/target/debug/deps/libgobject_sys-f4e0209b545e4cb8.rlib" "/root/flat-manager/target/debug/deps/libglib_sys-d5e7de360f9b66f6.rlib" "/root/flat-manager/target/debug/deps/librand-7f800c9927285a3c.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-c7e8716211f4dc32.rlib" "/root/flat-manager/target/debug/deps/librand_core-69d3af3286961144.rlib" "/root/flat-manager/target/debug/deps/libgetrandom-9aa149158e325e81.rlib" "/root/flat-manager/target/debug/deps/libtempfile-8a198e71606ec4ad.rlib" "/root/flat-manager/target/debug/deps/libfastrand-ea5c5d539f632998.rlib" "/root/flat-manager/target/debug/deps/libremove_dir_all-b743452179863578.rlib" "/root/flat-manager/target/debug/deps/libaskama-1831d1539b514ff9.rlib" "/root/flat-manager/target/debug/deps/libaskama_shared-e443ef2faa3c2fa1.rlib" "/root/flat-manager/target/debug/deps/libtoml-b0a404dfcf288dcf.rlib" "/root/flat-manager/target/debug/deps/libactix_files-106d88fe073b3343.rlib" "/root/flat-manager/target/debug/deps/libv_htmlescape-aa4f84e69b9eed54.rlib" "/root/flat-manager/target/debug/deps/libv_escape-df314753d5af7561.rlib" "/root/flat-manager/target/debug/deps/libmime_guess-c343d336432add9d.rlib" "/root/flat-manager/target/debug/deps/libunicase-5fb8df8193b332e1.rlib" "/root/flat-manager/target/debug/deps/libactix_web_actors-14c77e25bf2093ae.rlib" "/root/flat-manager/target/debug/deps/libfutures-d269d395b590cc88.rlib" "/root/flat-manager/target/debug/deps/libfutures_executor-99a25e92f2632375.rlib" "/root/flat-manager/target/debug/deps/libfutures_util-fbb145ca9ffc4707.rlib" "/root/flat-manager/target/debug/deps/libfutures_io-d8d7758e5ce2d5f4.rlib" "/root/flat-manager/target/debug/deps/libfutures_channel-dfb515a129880ca2.rlib" "/root/flat-manager/target/debug/deps/libfutures_sink-2640ce46f70dbfda.rlib" "/root/flat-manager/target/debug/deps/libfutures_task-a72bef1361827909.rlib" "/root/flat-manager/target/debug/deps/libpin_utils-028999b49d772fa6.rlib" "/root/flat-manager/target/debug/deps/libfutures_core-ac26ad95600e8c95.rlib" "/root/flat-manager/target/debug/deps/libactix_multipart-649cb97b6db1407e.rlib" "/root/flat-manager/target/debug/deps/libtwoway-f3f906811e431e09.rlib" "/root/flat-manager/target/debug/deps/libunchecked_index-607c97c09a22c53f.rlib" "/root/flat-manager/target/debug/deps/libactix_web-faa19d9065a13414.rlib" "/root/flat-manager/target/debug/deps/libawc-995fff0fc66ba255.rlib" "/root/flat-manager/target/debug/deps/libactix_testing-b0c81b7835dcb43a.rlib" "/root/flat-manager/target/debug/deps/libactix_server-d6f7566baf0dbd15.rlib" "/root/flat-manager/target/debug/deps/libtokio_signal-9a0dda5619387036.rlib" "/root/flat-manager/target/debug/deps/libsignal_hook_registry-9fdd7ca057fc636f.rlib" "/root/flat-manager/target/debug/deps/libmio_uds-20ee0a54a0a93cc1.rlib" "/root/flat-manager/target/debug/deps/libactix_router-824538138ebca56b.rlib" "/root/flat-manager/target/debug/deps/libdiesel_migrations-c1b94c5bb754f1e6.rlib" "/root/flat-manager/target/debug/deps/libmigrations_internals-3674f228acc7d050.rlib" "/root/flat-manager/target/debug/deps/libdiesel-a7bffd050586e8e1.rlib" "/root/flat-manager/target/debug/deps/libpq_sys-e6f574fca58d708f.rlib" "/root/flat-manager/target/debug/deps/libr2d2-1f5c720da5644c69.rlib" "/root/flat-manager/target/debug/deps/libscheduled_thread_pool-53d8dd7189b03105.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-5fe22fb26b475a72.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-926334878304ccf7.rlib" "/root/flat-manager/target/debug/deps/libsmallvec-bfa855a1a14adce5.rlib" "/root/flat-manager/target/debug/deps/liblock_api-67f5d8626147a54a.rlib" "/root/flat-manager/target/debug/deps/libactix-9cb206e1b1a57749.rlib" "/root/flat-manager/target/debug/deps/libactix_http-a9919ae7bf193c8d.rlib" "/root/flat-manager/target/debug/deps/libsha1-cfd1b0e37faaa4ac.rlib" "/root/flat-manager/target/debug/deps/libsha1_smol-b3033a63e758f6f2.rlib" "/root/flat-manager/target/debug/deps/libbase64-a6058bb2c3f89caa.rlib" "/root/flat-manager/target/debug/deps/librand-70bdad1c5cd17ccb.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-1b04c8d42cd78e38.rlib" "/root/flat-manager/target/debug/deps/libppv_lite86-580c5e6d16835829.rlib" "/root/flat-manager/target/debug/deps/librand_core-b97f56d513c2140c.rlib" "/root/flat-manager/target/debug/deps/libgetrandom-cd5dd474dd59f429.rlib" "/root/flat-manager/target/debug/deps/libserde_urlencoded-f856737eb768cb86.rlib" "/root/flat-manager/target/debug/deps/liburl-009c44392e5e1be4.rlib" "/root/flat-manager/target/debug/deps/libidna-c45ad26dd6779f39.rlib" "/root/flat-manager/target/debug/deps/libform_urlencoded-d94e33afbe4401a5.rlib" "/root/flat-manager/target/debug/deps/libdtoa-c07ecd3b0e88ade5.rlib" "/root/flat-manager/target/debug/deps/libhttparse-c6b311cd15293032.rlib" "/root/flat-manager/target/debug/deps/libchrono-d86c84e3f5072733.rlib" "/root/flat-manager/target/debug/deps/libnum_integer-6651e5df0527c33e.rlib" "/root/flat-manager/target/debug/deps/libnum_traits-aab9ea8fc30e3349.rlib" "/root/flat-manager/target/debug/deps/libserde_json-c875b04b8aaa1f78.rlib" "/root/flat-manager/target/debug/deps/libryu-9a5a9e3e280974ba.rlib" "/root/flat-manager/target/debug/deps/libitoa-c3384ae0ed635300.rlib" "/root/flat-manager/target/debug/deps/libserde-65ea612a1e1f4f1b.rlib" "/root/flat-manager/target/debug/deps/libencoding_rs-bfc1cd5445c328e5.rlib" "/root/flat-manager/target/debug/deps/liblanguage_tags-f5b7c92bc5fb821f.rlib" "/root/flat-manager/target/debug/deps/libpercent_encoding-6f6e36fad6acdbd8.rlib" "/root/flat-manager/target/debug/deps/libmime-0f8d1457191cfcac.rlib" "/root/flat-manager/target/debug/deps/libflate2-456ba404c413225a.rlib" "/root/flat-manager/target/debug/deps/libcrc32fast-d36cd25afc2640d5.rlib" "/root/flat-manager/target/debug/deps/libbrotli2-8afcad11a36e2e20.rlib" "/root/flat-manager/target/debug/deps/libbrotli_sys-0537c9b6808a4221.rlib" "/root/flat-manager/target/debug/deps/libtime-45afa61f0b242654.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-ea98704df43053b0.rlib" "/root/flat-manager/target/debug/deps/libahash-081fc11524e694d4.rlib" "/root/flat-manager/target/debug/deps/libconst_random-ce6867e80b3bafb4.rlib" "/root/flat-manager/target/debug/deps/libactix_utils-14427d042b7eb27e.rlib" "/root/flat-manager/target/debug/deps/libactix_connect-b8d62ed2b0df33ac.rlib" "/root/flat-manager/target/debug/deps/libeither-cdb2f1fe245191c7.rlib" "/root/flat-manager/target/debug/deps/libh2-7557b68c33a007ea.rlib" "/root/flat-manager/target/debug/deps/libindexmap-e8ed4b166fc5e7da.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-d767707f5e3d14af.rlib" "/root/flat-manager/target/debug/deps/libstring-3aebfae9a2abd91f.rlib" "/root/flat-manager/target/debug/deps/libhttp-9592fae592345a05.rlib" "/root/flat-manager/target/debug/deps/libitoa-ddd0f79e24b25b74.rlib" "/root/flat-manager/target/debug/deps/libactix_service-6b59047c11bfbb70.rlib" "/root/flat-manager/target/debug/deps/libactix_server_config-91f81284ce364dac.rlib" "/root/flat-manager/target/debug/deps/libactix_codec-f7ea47c7b1b829d4.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_channel-07a25ea0fb5bcb52.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_utils-e6b700d6731e9468.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-29fadb62e3ad86fd.rlib" "/root/flat-manager/target/debug/deps/libtrust_dns_resolver-c177cd626e5dfa93.rlib" "/root/flat-manager/target/debug/deps/libtrust_dns_proto-5d2541cb90c9693f.rlib" "/root/flat-manager/target/debug/deps/liburl-c023bce137bc930f.rlib" "/root/flat-manager/target/debug/deps/libpercent_encoding-ff829dab53c398b2.rlib" "/root/flat-manager/target/debug/deps/libtokio_udp-bbffcaa1ab1d8e00.rlib" "/root/flat-manager/target/debug/deps/libtokio_codec-b66cdef611102d6f.rlib" "/root/flat-manager/target/debug/deps/libsocket2-b855a7d4242efd4b.rlib" "/root/flat-manager/target/debug/deps/libidna-970241c8ad27e4b6.rlib" "/root/flat-manager/target/debug/deps/libunicode_normalization-b4f63b623b3884f9.rlib" "/root/flat-manager/target/debug/deps/libtinyvec-988e0ec6e1a8add7.rlib" "/root/flat-manager/target/debug/deps/libtinyvec_macros-12960b2ed051d614.rlib" "/root/flat-manager/target/debug/deps/libunicode_bidi-6e9d6f22cbeff65d.rlib" "/root/flat-manager/target/debug/deps/libmatches-88da6780f3e088c0.rlib" "/root/flat-manager/target/debug/deps/libresolv_conf-ce3404fd1e8ef848.rlib" "/root/flat-manager/target/debug/deps/libhostname-5bfb9d694f4b09de.rlib" "/root/flat-manager/target/debug/deps/libmatch_cfg-36b1d71b0463a193.rlib" "/root/flat-manager/target/debug/deps/libquick_error-a50f414a4fc21ea3.rlib" "/root/flat-manager/target/debug/deps/liblru_cache-7420758be71e8ca4.rlib" "/root/flat-manager/target/debug/deps/liblinked_hash_map-b544fb87ad7aeb7e.rlib" "/root/flat-manager/target/debug/deps/libfailure-375d7ae69bb7a9c7.rlib" "/root/flat-manager/target/debug/deps/libbacktrace-12b4b79a1c21f181.rlib" "/root/flat-manager/target/debug/deps/libminiz_oxide-96def5e6800e28e1.rlib" "/root/flat-manager/target/debug/deps/libadler-f058e3c8e8538cb8.rlib" "/root/flat-manager/target/debug/deps/libobject-5940bbe4bfec8269.rlib" "/root/flat-manager/target/debug/deps/libaddr2line-297bbb90d2e3e4a5.rlib" "/root/flat-manager/target/debug/deps/libgimli-f8a76d971791bd3b.rlib" "/root/flat-manager/target/debug/deps/librustc_demangle-bf8fd8f0219439e4.rlib" "/root/flat-manager/target/debug/deps/libtokio_tcp-af5c3327a234b7c3.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-6a3f004a3623f053.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-d13baf245ced330f.rlib" "/root/flat-manager/target/debug/deps/librand-f3958daf0a24a0fc.rlib" "/root/flat-manager/target/debug/deps/librand_xorshift-8b18ef96ac1ef7a7.rlib" "/root/flat-manager/target/debug/deps/librand_pcg-de9862f244714752.rlib" "/root/flat-manager/target/debug/deps/librand_hc-bd2a2f31b459be60.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-5898e2f7b54a9c5b.rlib" "/root/flat-manager/target/debug/deps/librand_isaac-b3f913bc7cb49855.rlib" "/root/flat-manager/target/debug/deps/librand_core-0bbf2b4baa773d35.rlib" "/root/flat-manager/target/debug/deps/librand_os-10b65c028efa95d0.rlib" "/root/flat-manager/target/debug/deps/librand_jitter-48e0683e00a13cf0.rlib" "/root/flat-manager/target/debug/deps/librand_core-9eb4206b96bb779f.rlib" "/root/flat-manager/target/debug/deps/liblock_api-af53d69d34d6b80e.rlib" "/root/flat-manager/target/debug/deps/libbitflags-4007a0edb5520d45.rlib" "/root/flat-manager/target/debug/deps/libactix_rt-203d0337b45e8524.rlib" "/root/flat-manager/target/debug/deps/libactix_threadpool-c0003d6b600c1227.rlib" "/root/flat-manager/target/debug/deps/libthreadpool-c5525a1be4e12835.rlib" "/root/flat-manager/target/debug/deps/libtokio_timer-b19aa87cdac1b978.rlib" "/root/flat-manager/target/debug/deps/libtokio_reactor-8d7d59cc5feacadf.rlib" "/root/flat-manager/target/debug/deps/libtokio_sync-47ec4449e420a74d.rlib" "/root/flat-manager/target/debug/deps/libfnv-f7c691c4fbe066a5.rlib" "/root/flat-manager/target/debug/deps/libtokio_io-1f2ca29b48e479c5.rlib" "/root/flat-manager/target/debug/deps/libbytes-18c8594c6e29bdfe.rlib" "/root/flat-manager/target/debug/deps/libbyteorder-bcdf9fbfae9fe933.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-6091d751628f445a.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-1585c391aacb67df.rlib" "/root/flat-manager/target/debug/deps/libsmallvec-33c8487ac39f7ea7.rlib" "/root/flat-manager/target/debug/deps/libmaybe_uninit-58df6ddc2b0aeceb.rlib" "/root/flat-manager/target/debug/deps/liblock_api-cefd8d6dc22f73bc.rlib" "/root/flat-manager/target/debug/deps/libscopeguard-9df96870819ebbe7.rlib" "/root/flat-manager/target/debug/deps/libmio-eb70f91e16e61db6.rlib" "/root/flat-manager/target/debug/deps/libslab-c43d379778e7fe7a.rlib" "/root/flat-manager/target/debug/deps/libiovec-e44dfe016232a07e.rlib" "/root/flat-manager/target/debug/deps/libnet2-44bdea4789ef06e2.rlib" "/root/flat-manager/target/debug/deps/libcopyless-5183c0bc9820a870.rlib" "/root/flat-manager/target/debug/deps/libtokio_current_thread-4e066e5800398810.rlib" "/root/flat-manager/target/debug/deps/libtokio_executor-781c8f0b69d28ef4.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_utils-3fc4f370b5549c49.rlib" "/root/flat-manager/target/debug/deps/liblazy_static-5c82f33e65a85b2c.rlib" "/root/flat-manager/target/debug/deps/libcfg_if-bffdd88a2bb82d24.rlib" "/root/flat-manager/target/debug/deps/libfutures-3ed8fa8054d0a926.rlib" "/root/flat-manager/target/debug/deps/libenv_logger-3f0ff6ce845e8622.rlib" "/root/flat-manager/target/debug/deps/libatty-550c085497708e63.rlib" "/root/flat-manager/target/debug/deps/libtermcolor-831d8fa44b92008d.rlib" "/root/flat-manager/target/debug/deps/libhumantime-e00672f17408dbe1.rlib" "/root/flat-manager/target/debug/deps/libregex-b5b4725d54f71217.rlib" "/root/flat-manager/target/debug/deps/libaho_corasick-ed33694c12a52a5f.rlib" "/root/flat-manager/target/debug/deps/libregex_syntax-da1d05d4ebdf6330.rlib" "/root/flat-manager/target/debug/deps/libtokio-1930f36e9ce8cf8d.rlib" "/root/flat-manager/target/debug/deps/libnum_cpus-be9e8ce780e28ca2.rlib" "/root/flat-manager/target/debug/deps/libsocket2-254982db8c388c10.rlib" "/root/flat-manager/target/debug/deps/libmemchr-907d396cc347c886.rlib" "/root/flat-manager/target/debug/deps/libbytes-35392eddbb173e91.rlib" "/root/flat-manager/target/debug/deps/libpin_project_lite-a9515d54ff34c783.rlib" "/root/flat-manager/target/debug/deps/libmio-c29e042997ba6ae2.rlib" "/root/flat-manager/target/debug/deps/liblibc-061cb0a3f9a05e81.rlib" "/root/flat-manager/target/debug/deps/liblog-92ff8c57bdffc353.rlib" "/root/flat-manager/target/debug/deps/libcfg_if-781d043472d95efa.rlib" "/root/flat-manager/target/debug/deps/libdotenv-688953d6a60e56cc.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-16dfa5a88c8a9870.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_unwind-488231ba9287eba2.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libobject-5efba96be6ed90d3.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libmemchr-db4ccd285e67acce.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libaddr2line-472498f2dee2b7bb.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgimli-25f09215467a5a0d.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_demangle-f7d3eaf981fbbad3.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd_detect-bd735aa1e8b0b356.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libhashbrown-d7df93f3cf036104.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libminiz_oxide-45c141746ed539f5.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libadler-f9a811623104d988.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_alloc-04c895baa87181e8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunwind-b11573bcb5018c0a.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcfg_if-0dcc283b7d0d17a7.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblibc-8deba1eda384b5a8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc-0882b8eba599d4a8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_core-33f2a4adaef7f99b.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcore-d8e7d70f28b040cc.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcompiler_builtins-087ef387fa5359a4.rlib" "-Wl,-Bdynamic" "-lgobject-2.0" "-lostree-1" "-lgio-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgio-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgobject-2.0" "-lglib-2.0" "-lpq" "-lgcc_s" "-lutil" "-lrt" "-lpthread" "-lm" "-ldl" "-lc" "-Wl,--eh-frame-hdr" "-Wl,-znoexecstack" "-L" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib" "-o" "/root/flat-manager/target/debug/deps/flat_manager-8c46326b91402a6d" "-Wl,--gc-sections" "-pie" "-Wl,-zrelro,-znow" "-nodefaultlibs"
  = note: /usr/bin/ld: cannot find -lpq: No such file or directory
          collect2: error: ld returned 1 exit status


error: could not compile `flat-manager` due to previous error
warning: build failed, waiting for other jobs to finish...
error: linking with `cc` failed: exit status: 1
  |
  = note: "cc" "-m64" "/tmp/rustcMq3WNf/symbols.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.105cj0fkrbvooqvn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.11dqzp1o4hgqe9n4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.12mam0qb342j7jlg.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.13rqrzt88kgaal9x.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.15eplys2wmkn45ec.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1a0ymch7zt13cddr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1avl1sjlxecxkr8j.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1cd9hpddwxdm04m4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1craus41sgfnal62.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1ctpfa415q94ov25.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1d329e7sxaa8tb9a.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1d8egvbui95hgrxq.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1eiz16mfuln8hg6v.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1fxp5y4nzted8rih.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1gmo37bk3tca96ri.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1ipmrt0253y7oo7z.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1kyaskkd9nc89zxu.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1mgua1jhobry1xu1.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1nifsp1e1eud32jh.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1nsd2ls6ygqp73hw.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1oulmidzmgw23qkr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1pejbgl258fvxjms.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1rdxrr554yt1fr0d.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1s2tn37i3e8oc23c.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1tfr6cxh9l3pvlnp.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1xe5nefmjlo1z7e.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1xs5ztji3e7d0nop.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1y1vtmi2g1ocosgu.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.1yy9c99j0ucinu22.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.20qupgicffsroz20.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.23klz114r05tyx2w.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.23w6rkfcjfvhf8c.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.240m2w01tu2lhxvd.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.29j4dkq3beufcvbl.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2ay6ovb5sbnnsqs3.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2e8zetfevt5sow22.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2eqgvvrxjwg9a5d2.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2fewca19y5efmo8k.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2i79kdk8f6hpuryf.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2iwb5s5d2nzfhq4f.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2ixz6e5zfa5e7div.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2l6l84tbr14dmi9a.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2lvj1m9kusz4kjpk.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2md72mr5pzijwsug.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2nz7mx6dydoioi6f.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2p3a5vkfx2fovyad.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2q1w2hh6co8yrk0c.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2qnhjr9yxw65qei.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2tfblg54e0plt94c.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2uf2lcn9oiia2elq.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2up39i3b67262mru.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2w455nphflzmh3wn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.2w6iwysnhbhdbul6.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.31r2cvpjnfu8ydj4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.32bdasbp5fbw4ce4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.32mhy18bz10tjgx.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.33iwagyzstfcc0ah.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3731nytr8cldcn40.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.37dq9rq1yrogg73b.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.397446ik0sa6rhaz.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.39vt1vht3g74po9h.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.39w3jye073nc1fys.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3arhu6r2abvrk1s.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3cdgtgptew26bxmx.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3df8ry2nymeqin9f.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3ef89570rwvpoupt.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3equp4sfcli8uscj.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3euwgukove7bk0yf.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3fltxc3a9jirp77e.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3fsxtgh4e9zi66ap.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3gcnon33r02tjool.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3gnuhr2g06zkbdgn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3h7u0fdv4ag24qe.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3hv4xjv7v5dblj1g.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3js290inuf72wnlj.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3khq2mqcza866vp.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3kjtbpwh58wr2z7n.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3l30203z3tango2y.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3ojg8rmrwtg7m8nk.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3ok92ne10p5qos54.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3owlfma4gtd8vh5b.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3pikluk6vc14lte3.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3pp9xte93helw7bn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3q74y6q42llmsynh.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3qnu4mig0fz177gf.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3qse3ammndbdvatj.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3qxhf0bnr5simk88.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3uyfcsxxifzyivp0.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3w8e96x8eb5dpgf3.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3wxcnvvjgghxd5bx.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3xdwusfoefpo5wek.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3xq695slq3eocwgg.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3ywnko643jk0xw0h.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.3zznwms58cdyd46s.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.402r7ue4pt1uthpu.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.413yx4cn2imvpnok.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.42zmvp0jluwc478k.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.43v3wrkuew053ig1.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.45wz16ho1nww9cer.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.46c8awwzbwi0oxnr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.46d7yknpd492bsqr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4aceiv9y8soz6f04.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4asqrk7tn2gfvq1t.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4b6em3ycvtaga8wr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4bmiali0rwdulrms.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4ccgan8s3n3oawpm.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4clud200sysln8kk.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4drkwnfx9d7q5cl1.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4iemftvmwkun1lv1.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4j15axpwxjqo1fvc.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4jmd0jvttmvll5pp.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4mjquf9f60ngp0d4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4mybuymrpa35df7s.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4pvo74kyad68791a.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4pwsj2dt1edohn03.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4s5qsebpo3y30rl3.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4twq8uc2389pez0i.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4v1y0niyifmgl37s.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4w9qqivekc5lqo2l.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.4yaq7offei3d804o.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.55sszstolcos2965.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.59n9wtfc1wy5i81v.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5az7l2ezw6fku5lt.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5azb9856hdkgwvcn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5eumtkmz85zveaij.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5ffx0hue158tdy6o.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5gghec8bhsmenvmn.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.5guvszkd91e4rkcj.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.6lpkc6hqrjklga0.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.6m0632spyt3vbqd.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.8d0bume4q04k10f.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.bxnjrzj256kx7uu.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.cs316ff1nns3zq5.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.d1nf32cintxvvjq.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.eixjjvthsguu3pe.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.fhmgb0a87ngy3t8.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.fojc5ceiu5grutr.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.gk9f2e3y1la5xej.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.ivbwb5319yzv6aj.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.kdkrn3gg9aoyr8f.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.l29uy9htgubf79b.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.njh0kytp0ffnipf.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.oftervmwcbf2qqy.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.pdrfiqt2qmh00fy.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.pogtitr7f4uurn2.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.qquo9bxlk8kt3q8.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.r3g0bthjrzkwrd0.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.rltlr79qsadctwm.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.rrqn84zntd9hhig.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.ty4785qyaz5uyw4.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.tyhvvgxc2h85wq1.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.tzk6wusnb13knr7.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.vo57qhkn0lyrq2l.rcgu.o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab.l2qxns3a6t0iy8w.rcgu.o" "-Wl,--as-needed" "-L" "/root/flat-manager/target/debug/deps" "-L" "/root/flat-manager/target/debug/build/brotli-sys-c0a27acabdb9b138/out" "-L" "/usr/lib/x86_64-linux-gnu" "-L" "/root/flat-manager/target/debug/build/ring-565de3fe1e474494/out" "-L" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib" "-Wl,-Bstatic" "/root/flat-manager/target/debug/deps/libenv_logger-3f0ff6ce845e8622.rlib" "/root/flat-manager/target/debug/deps/libatty-550c085497708e63.rlib" "/root/flat-manager/target/debug/deps/libtermcolor-831d8fa44b92008d.rlib" "/root/flat-manager/target/debug/deps/libhumantime-e00672f17408dbe1.rlib" "/root/flat-manager/target/debug/deps/libfutures_locks-bca58c048d5a73f5.rlib" "/root/flat-manager/target/debug/deps/libflatmanager-2172893fddd9fdd5.rlib" "/root/flat-manager/target/debug/deps/libtokio-1930f36e9ce8cf8d.rlib" "/root/flat-manager/target/debug/deps/libsocket2-254982db8c388c10.rlib" "/root/flat-manager/target/debug/deps/libbytes-35392eddbb173e91.rlib" "/root/flat-manager/target/debug/deps/libmio-c29e042997ba6ae2.rlib" "/root/flat-manager/target/debug/deps/libfiletime-b753758d78df8b7a.rlib" "/root/flat-manager/target/debug/deps/libjsonwebtoken-f396b0c3cdce7429.rlib" "/root/flat-manager/target/debug/deps/libpem-c88437636648ab9c.rlib" "/root/flat-manager/target/debug/deps/libbase64-fdd705b8fb7cffd1.rlib" "/root/flat-manager/target/debug/deps/libbase64-0b88a04759406a00.rlib" "/root/flat-manager/target/debug/deps/libsimple_asn1-d164d2a6ea48eb0d.rlib" "/root/flat-manager/target/debug/deps/libnum_bigint-1d9cdc6a86412ca6.rlib" "/root/flat-manager/target/debug/deps/libring-eecbc6750d6868e1.rlib" "/root/flat-manager/target/debug/deps/libspin-e37c43ddec5eb60c.rlib" "/root/flat-manager/target/debug/deps/libuntrusted-97cd9a69916e3bce.rlib" "/root/flat-manager/target/debug/deps/libtokio_process-944de106a2768294.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_queue-ecadd9c937619b05.rlib" "/root/flat-manager/target/debug/deps/libwalkdir-c46c713b90805ba5.rlib" "/root/flat-manager/target/debug/deps/libsame_file-80c931eaa8c275f9.rlib" "/root/flat-manager/target/debug/deps/libostree-26145448634ad183.rlib" "/root/flat-manager/target/debug/deps/libhex-75c11233f1668394.rlib" "/root/flat-manager/target/debug/deps/libradix64-92915cff80f5aa2d.rlib" "/root/flat-manager/target/debug/deps/libarrayref-f6df4c1ade89c260.rlib" "/root/flat-manager/target/debug/deps/libgio-4bf14f803a068174.rlib" "/root/flat-manager/target/debug/deps/libthiserror-ec9dd2d207d8e730.rlib" "/root/flat-manager/target/debug/deps/libglib-6dbdfe1ca7cd8ae9.rlib" "/root/flat-manager/target/debug/deps/libonce_cell-6b60731e13fb7b3a.rlib" "/root/flat-manager/target/debug/deps/libostree_sys-81ad5610b7e881ca.rlib" "/root/flat-manager/target/debug/deps/libgio_sys-77418b28133dc16b.rlib" "/root/flat-manager/target/debug/deps/libgobject_sys-f4e0209b545e4cb8.rlib" "/root/flat-manager/target/debug/deps/libglib_sys-d5e7de360f9b66f6.rlib" "/root/flat-manager/target/debug/deps/librand-7f800c9927285a3c.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-c7e8716211f4dc32.rlib" "/root/flat-manager/target/debug/deps/librand_core-69d3af3286961144.rlib" "/root/flat-manager/target/debug/deps/libgetrandom-9aa149158e325e81.rlib" "/root/flat-manager/target/debug/deps/libtempfile-8a198e71606ec4ad.rlib" "/root/flat-manager/target/debug/deps/libfastrand-ea5c5d539f632998.rlib" "/root/flat-manager/target/debug/deps/libremove_dir_all-b743452179863578.rlib" "/root/flat-manager/target/debug/deps/libaskama-1831d1539b514ff9.rlib" "/root/flat-manager/target/debug/deps/libaskama_shared-e443ef2faa3c2fa1.rlib" "/root/flat-manager/target/debug/deps/libtoml-b0a404dfcf288dcf.rlib" "/root/flat-manager/target/debug/deps/libactix_files-106d88fe073b3343.rlib" "/root/flat-manager/target/debug/deps/libv_htmlescape-aa4f84e69b9eed54.rlib" "/root/flat-manager/target/debug/deps/libv_escape-df314753d5af7561.rlib" "/root/flat-manager/target/debug/deps/libmime_guess-c343d336432add9d.rlib" "/root/flat-manager/target/debug/deps/libunicase-5fb8df8193b332e1.rlib" "/root/flat-manager/target/debug/deps/libactix_web_actors-14c77e25bf2093ae.rlib" "/root/flat-manager/target/debug/deps/libfutures-d269d395b590cc88.rlib" "/root/flat-manager/target/debug/deps/libfutures_executor-99a25e92f2632375.rlib" "/root/flat-manager/target/debug/deps/libfutures_util-fbb145ca9ffc4707.rlib" "/root/flat-manager/target/debug/deps/libfutures_io-d8d7758e5ce2d5f4.rlib" "/root/flat-manager/target/debug/deps/libfutures_channel-dfb515a129880ca2.rlib" "/root/flat-manager/target/debug/deps/libpin_project_lite-a9515d54ff34c783.rlib" "/root/flat-manager/target/debug/deps/libfutures_sink-2640ce46f70dbfda.rlib" "/root/flat-manager/target/debug/deps/libfutures_task-a72bef1361827909.rlib" "/root/flat-manager/target/debug/deps/libpin_utils-028999b49d772fa6.rlib" "/root/flat-manager/target/debug/deps/libfutures_core-ac26ad95600e8c95.rlib" "/root/flat-manager/target/debug/deps/libactix_multipart-649cb97b6db1407e.rlib" "/root/flat-manager/target/debug/deps/libtwoway-f3f906811e431e09.rlib" "/root/flat-manager/target/debug/deps/libunchecked_index-607c97c09a22c53f.rlib" "/root/flat-manager/target/debug/deps/libdiesel_migrations-c1b94c5bb754f1e6.rlib" "/root/flat-manager/target/debug/deps/libmigrations_internals-3674f228acc7d050.rlib" "/root/flat-manager/target/debug/deps/libdiesel-a7bffd050586e8e1.rlib" "/root/flat-manager/target/debug/deps/libpq_sys-e6f574fca58d708f.rlib" "/root/flat-manager/target/debug/deps/libr2d2-1f5c720da5644c69.rlib" "/root/flat-manager/target/debug/deps/libscheduled_thread_pool-53d8dd7189b03105.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-5fe22fb26b475a72.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-926334878304ccf7.rlib" "/root/flat-manager/target/debug/deps/libsmallvec-bfa855a1a14adce5.rlib" "/root/flat-manager/target/debug/deps/liblock_api-67f5d8626147a54a.rlib" "/root/flat-manager/target/debug/deps/libmpart_async-40c386317e14a371.rlib" "/root/flat-manager/target/debug/deps/libtokio_fs-b93e3247fe512ca8.rlib" "/root/flat-manager/target/debug/deps/libtokio_threadpool-bfab51a9d7f9281f.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_queue-4fe8248da062e585.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_deque-432b49bd3766b573.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_epoch-0f1a9c1785e3ad54.rlib" "/root/flat-manager/target/debug/deps/libmemoffset-d2211f3aa5b510f9.rlib" "/root/flat-manager/target/debug/deps/librand-202386a9097a14d9.rlib" "/root/flat-manager/target/debug/deps/libfutures_fs-fc2a424048317d77.rlib" "/root/flat-manager/target/debug/deps/libfutures_cpupool-85fcd256916d9640.rlib" "/root/flat-manager/target/debug/deps/libdotenv-688953d6a60e56cc.rlib" "/root/flat-manager/target/debug/deps/libactix_web-faa19d9065a13414.rlib" "/root/flat-manager/target/debug/deps/libawc-995fff0fc66ba255.rlib" "/root/flat-manager/target/debug/deps/libactix_testing-b0c81b7835dcb43a.rlib" "/root/flat-manager/target/debug/deps/libactix_server-d6f7566baf0dbd15.rlib" "/root/flat-manager/target/debug/deps/libtokio_signal-9a0dda5619387036.rlib" "/root/flat-manager/target/debug/deps/libsignal_hook_registry-9fdd7ca057fc636f.rlib" "/root/flat-manager/target/debug/deps/libmio_uds-20ee0a54a0a93cc1.rlib" "/root/flat-manager/target/debug/deps/libactix_router-824538138ebca56b.rlib" "/root/flat-manager/target/debug/deps/libactix-9cb206e1b1a57749.rlib" "/root/flat-manager/target/debug/deps/libactix_http-a9919ae7bf193c8d.rlib" "/root/flat-manager/target/debug/deps/libsha1-cfd1b0e37faaa4ac.rlib" "/root/flat-manager/target/debug/deps/libsha1_smol-b3033a63e758f6f2.rlib" "/root/flat-manager/target/debug/deps/libbase64-a6058bb2c3f89caa.rlib" "/root/flat-manager/target/debug/deps/librand-70bdad1c5cd17ccb.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-1b04c8d42cd78e38.rlib" "/root/flat-manager/target/debug/deps/libppv_lite86-580c5e6d16835829.rlib" "/root/flat-manager/target/debug/deps/librand_core-b97f56d513c2140c.rlib" "/root/flat-manager/target/debug/deps/libgetrandom-cd5dd474dd59f429.rlib" "/root/flat-manager/target/debug/deps/libserde_urlencoded-f856737eb768cb86.rlib" "/root/flat-manager/target/debug/deps/liburl-009c44392e5e1be4.rlib" "/root/flat-manager/target/debug/deps/libidna-c45ad26dd6779f39.rlib" "/root/flat-manager/target/debug/deps/libform_urlencoded-d94e33afbe4401a5.rlib" "/root/flat-manager/target/debug/deps/libdtoa-c07ecd3b0e88ade5.rlib" "/root/flat-manager/target/debug/deps/libhttparse-c6b311cd15293032.rlib" "/root/flat-manager/target/debug/deps/libchrono-d86c84e3f5072733.rlib" "/root/flat-manager/target/debug/deps/libnum_integer-6651e5df0527c33e.rlib" "/root/flat-manager/target/debug/deps/libnum_traits-aab9ea8fc30e3349.rlib" "/root/flat-manager/target/debug/deps/libserde_json-c875b04b8aaa1f78.rlib" "/root/flat-manager/target/debug/deps/libryu-9a5a9e3e280974ba.rlib" "/root/flat-manager/target/debug/deps/libitoa-c3384ae0ed635300.rlib" "/root/flat-manager/target/debug/deps/libserde-65ea612a1e1f4f1b.rlib" "/root/flat-manager/target/debug/deps/libencoding_rs-bfc1cd5445c328e5.rlib" "/root/flat-manager/target/debug/deps/libregex-b5b4725d54f71217.rlib" "/root/flat-manager/target/debug/deps/libaho_corasick-ed33694c12a52a5f.rlib" "/root/flat-manager/target/debug/deps/libregex_syntax-da1d05d4ebdf6330.rlib" "/root/flat-manager/target/debug/deps/liblanguage_tags-f5b7c92bc5fb821f.rlib" "/root/flat-manager/target/debug/deps/libpercent_encoding-6f6e36fad6acdbd8.rlib" "/root/flat-manager/target/debug/deps/libmime-0f8d1457191cfcac.rlib" "/root/flat-manager/target/debug/deps/libflate2-456ba404c413225a.rlib" "/root/flat-manager/target/debug/deps/libcrc32fast-d36cd25afc2640d5.rlib" "/root/flat-manager/target/debug/deps/libbrotli2-8afcad11a36e2e20.rlib" "/root/flat-manager/target/debug/deps/libbrotli_sys-0537c9b6808a4221.rlib" "/root/flat-manager/target/debug/deps/libtime-45afa61f0b242654.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-ea98704df43053b0.rlib" "/root/flat-manager/target/debug/deps/libahash-081fc11524e694d4.rlib" "/root/flat-manager/target/debug/deps/libconst_random-ce6867e80b3bafb4.rlib" "/root/flat-manager/target/debug/deps/libactix_utils-14427d042b7eb27e.rlib" "/root/flat-manager/target/debug/deps/libactix_connect-b8d62ed2b0df33ac.rlib" "/root/flat-manager/target/debug/deps/libeither-cdb2f1fe245191c7.rlib" "/root/flat-manager/target/debug/deps/libh2-7557b68c33a007ea.rlib" "/root/flat-manager/target/debug/deps/libindexmap-e8ed4b166fc5e7da.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-d767707f5e3d14af.rlib" "/root/flat-manager/target/debug/deps/libstring-3aebfae9a2abd91f.rlib" "/root/flat-manager/target/debug/deps/libhttp-9592fae592345a05.rlib" "/root/flat-manager/target/debug/deps/libitoa-ddd0f79e24b25b74.rlib" "/root/flat-manager/target/debug/deps/libactix_service-6b59047c11bfbb70.rlib" "/root/flat-manager/target/debug/deps/libactix_server_config-91f81284ce364dac.rlib" "/root/flat-manager/target/debug/deps/libactix_codec-f7ea47c7b1b829d4.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_channel-07a25ea0fb5bcb52.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_utils-e6b700d6731e9468.rlib" "/root/flat-manager/target/debug/deps/libhashbrown-29fadb62e3ad86fd.rlib" "/root/flat-manager/target/debug/deps/libtrust_dns_resolver-c177cd626e5dfa93.rlib" "/root/flat-manager/target/debug/deps/libtrust_dns_proto-5d2541cb90c9693f.rlib" "/root/flat-manager/target/debug/deps/liburl-c023bce137bc930f.rlib" "/root/flat-manager/target/debug/deps/libpercent_encoding-ff829dab53c398b2.rlib" "/root/flat-manager/target/debug/deps/libtokio_udp-bbffcaa1ab1d8e00.rlib" "/root/flat-manager/target/debug/deps/libtokio_codec-b66cdef611102d6f.rlib" "/root/flat-manager/target/debug/deps/libsocket2-b855a7d4242efd4b.rlib" "/root/flat-manager/target/debug/deps/libidna-970241c8ad27e4b6.rlib" "/root/flat-manager/target/debug/deps/libunicode_normalization-b4f63b623b3884f9.rlib" "/root/flat-manager/target/debug/deps/libtinyvec-988e0ec6e1a8add7.rlib" "/root/flat-manager/target/debug/deps/libtinyvec_macros-12960b2ed051d614.rlib" "/root/flat-manager/target/debug/deps/libunicode_bidi-6e9d6f22cbeff65d.rlib" "/root/flat-manager/target/debug/deps/libmatches-88da6780f3e088c0.rlib" "/root/flat-manager/target/debug/deps/libresolv_conf-ce3404fd1e8ef848.rlib" "/root/flat-manager/target/debug/deps/libhostname-5bfb9d694f4b09de.rlib" "/root/flat-manager/target/debug/deps/libmatch_cfg-36b1d71b0463a193.rlib" "/root/flat-manager/target/debug/deps/libquick_error-a50f414a4fc21ea3.rlib" "/root/flat-manager/target/debug/deps/liblru_cache-7420758be71e8ca4.rlib" "/root/flat-manager/target/debug/deps/liblinked_hash_map-b544fb87ad7aeb7e.rlib" "/root/flat-manager/target/debug/deps/libfailure-375d7ae69bb7a9c7.rlib" "/root/flat-manager/target/debug/deps/libbacktrace-12b4b79a1c21f181.rlib" "/root/flat-manager/target/debug/deps/libminiz_oxide-96def5e6800e28e1.rlib" "/root/flat-manager/target/debug/deps/libadler-f058e3c8e8538cb8.rlib" "/root/flat-manager/target/debug/deps/libobject-5940bbe4bfec8269.rlib" "/root/flat-manager/target/debug/deps/libmemchr-907d396cc347c886.rlib" "/root/flat-manager/target/debug/deps/libaddr2line-297bbb90d2e3e4a5.rlib" "/root/flat-manager/target/debug/deps/libgimli-f8a76d971791bd3b.rlib" "/root/flat-manager/target/debug/deps/librustc_demangle-bf8fd8f0219439e4.rlib" "/root/flat-manager/target/debug/deps/libtokio_tcp-af5c3327a234b7c3.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-6a3f004a3623f053.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-d13baf245ced330f.rlib" "/root/flat-manager/target/debug/deps/librand-f3958daf0a24a0fc.rlib" "/root/flat-manager/target/debug/deps/librand_xorshift-8b18ef96ac1ef7a7.rlib" "/root/flat-manager/target/debug/deps/librand_pcg-de9862f244714752.rlib" "/root/flat-manager/target/debug/deps/librand_hc-bd2a2f31b459be60.rlib" "/root/flat-manager/target/debug/deps/librand_chacha-5898e2f7b54a9c5b.rlib" "/root/flat-manager/target/debug/deps/librand_isaac-b3f913bc7cb49855.rlib" "/root/flat-manager/target/debug/deps/librand_core-0bbf2b4baa773d35.rlib" "/root/flat-manager/target/debug/deps/librand_os-10b65c028efa95d0.rlib" "/root/flat-manager/target/debug/deps/librand_jitter-48e0683e00a13cf0.rlib" "/root/flat-manager/target/debug/deps/librand_core-9eb4206b96bb779f.rlib" "/root/flat-manager/target/debug/deps/liblock_api-af53d69d34d6b80e.rlib" "/root/flat-manager/target/debug/deps/libbitflags-4007a0edb5520d45.rlib" "/root/flat-manager/target/debug/deps/libactix_rt-203d0337b45e8524.rlib" "/root/flat-manager/target/debug/deps/libactix_threadpool-c0003d6b600c1227.rlib" "/root/flat-manager/target/debug/deps/libthreadpool-c5525a1be4e12835.rlib" "/root/flat-manager/target/debug/deps/libtokio_timer-b19aa87cdac1b978.rlib" "/root/flat-manager/target/debug/deps/libtokio_reactor-8d7d59cc5feacadf.rlib" "/root/flat-manager/target/debug/deps/libtokio_sync-47ec4449e420a74d.rlib" "/root/flat-manager/target/debug/deps/libfnv-f7c691c4fbe066a5.rlib" "/root/flat-manager/target/debug/deps/libtokio_io-1f2ca29b48e479c5.rlib" "/root/flat-manager/target/debug/deps/libbytes-18c8594c6e29bdfe.rlib" "/root/flat-manager/target/debug/deps/libbyteorder-bcdf9fbfae9fe933.rlib" "/root/flat-manager/target/debug/deps/libparking_lot-6091d751628f445a.rlib" "/root/flat-manager/target/debug/deps/libparking_lot_core-1585c391aacb67df.rlib" "/root/flat-manager/target/debug/deps/libsmallvec-33c8487ac39f7ea7.rlib" "/root/flat-manager/target/debug/deps/libmaybe_uninit-58df6ddc2b0aeceb.rlib" "/root/flat-manager/target/debug/deps/liblock_api-cefd8d6dc22f73bc.rlib" "/root/flat-manager/target/debug/deps/libscopeguard-9df96870819ebbe7.rlib" "/root/flat-manager/target/debug/deps/libnum_cpus-be9e8ce780e28ca2.rlib" "/root/flat-manager/target/debug/deps/libmio-eb70f91e16e61db6.rlib" "/root/flat-manager/target/debug/deps/libslab-c43d379778e7fe7a.rlib" "/root/flat-manager/target/debug/deps/libiovec-e44dfe016232a07e.rlib" "/root/flat-manager/target/debug/deps/libnet2-44bdea4789ef06e2.rlib" "/root/flat-manager/target/debug/deps/liblibc-061cb0a3f9a05e81.rlib" "/root/flat-manager/target/debug/deps/liblog-92ff8c57bdffc353.rlib" "/root/flat-manager/target/debug/deps/libcfg_if-781d043472d95efa.rlib" "/root/flat-manager/target/debug/deps/libcopyless-5183c0bc9820a870.rlib" "/root/flat-manager/target/debug/deps/libtokio_current_thread-4e066e5800398810.rlib" "/root/flat-manager/target/debug/deps/libtokio_executor-781c8f0b69d28ef4.rlib" "/root/flat-manager/target/debug/deps/libcrossbeam_utils-3fc4f370b5549c49.rlib" "/root/flat-manager/target/debug/deps/liblazy_static-5c82f33e65a85b2c.rlib" "/root/flat-manager/target/debug/deps/libcfg_if-bffdd88a2bb82d24.rlib" "/root/flat-manager/target/debug/deps/libfutures-3ed8fa8054d0a926.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd-16dfa5a88c8a9870.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libpanic_unwind-488231ba9287eba2.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libobject-5efba96be6ed90d3.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libmemchr-db4ccd285e67acce.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libaddr2line-472498f2dee2b7bb.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libgimli-25f09215467a5a0d.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_demangle-f7d3eaf981fbbad3.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libstd_detect-bd735aa1e8b0b356.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libhashbrown-d7df93f3cf036104.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libminiz_oxide-45c141746ed539f5.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libadler-f9a811623104d988.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_alloc-04c895baa87181e8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libunwind-b11573bcb5018c0a.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcfg_if-0dcc283b7d0d17a7.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liblibc-8deba1eda384b5a8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/liballoc-0882b8eba599d4a8.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/librustc_std_workspace_core-33f2a4adaef7f99b.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcore-d8e7d70f28b040cc.rlib" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib/libcompiler_builtins-087ef387fa5359a4.rlib" "-Wl,-Bdynamic" "-lgobject-2.0" "-lostree-1" "-lgio-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgio-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgobject-2.0" "-lglib-2.0" "-lgobject-2.0" "-lglib-2.0" "-lpq" "-lgcc_s" "-lutil" "-lrt" "-lpthread" "-lm" "-ldl" "-lc" "-Wl,--eh-frame-hdr" "-Wl,-znoexecstack" "-L" "/usr/lib/rustlib/x86_64-unknown-linux-gnu/lib" "-o" "/root/flat-manager/target/debug/deps/delta_generator_client-c36b092f2edbb0ab" "-Wl,--gc-sections" "-pie" "-Wl,-zrelro,-znow" "-nodefaultlibs"
  = note: /usr/bin/ld: cannot find -lpq: No such file or directory
          collect2: error: ld returned 1 exit status


error: could not compile `flat-manager` due to previous error
```

:bulb: Errors... Retrying on Fedora-based CentOS with numerous package errors during build

---

### Reference
- flat-manager GitHub, https://github.com/flatpak/flat-manager, 2023-03-20-Mon.
- postgresql Download, https://www.postgresql.org/download/linux/ubuntu/, 2023-03-20-Mon.
- failed to run custom build command, https://github.com/openethereum/openethereum/issues/415, 2023-03-21-Tue.
- Install ostree-dev, https://zoomadmin.com/HowToInstall/UbuntuPackage/libostree-dev, 2023-03-21-Tue.
- flat-manager GitHub, https://github.com/flatpak/flat-manager, 2023-03-22-Wed.
- Rustup Install, https://forge.rust-lang.org/infra/other-installation-methods.html, 2023-03-22-Wed.
- Fedora & RHEL Version, https://docs.fedoraproject.org/en-US/quick-docs/fedora-and-red-hat-enterprise-linux/index.html, 2023-03-23-Thu.
- Ostree Version Fedora, https://bodhi.fedoraproject.org/updates/?packages=ostree&page=2, 2023-03-23-Thu.
- Install Rust, https://doc.rust-lang.org/book/ch01-01-installation.html, 2023-03-23-Thu.
- Install ngrok, https://ngrok.com/download, 2023-03-27-Mon.
- Check Ports on Internal Machine Blog KR, https://fblens.com/16, 2023-03-27-Mon.
- Check Ports on External Machine Blog KR, https://meetup.nhncloud.com/posts/204, 2023-03-27-Mon.
- Install GnuPG Fedora, https://fedoraproject.org/wiki/Cryptography, 2023-03-27-Mon.
- Create GPG Key Fedora, https://fedoraproject.org/wiki/Creating_GPG_Keys, 2023-03-27-Mon.
- ngrok, https://ngrok.com/, 2023-03-27-Mon.
- Tunneling Service via ngrok Blog KR, https://blog.outsider.ne.kr/1159, 2023-03-27-Mon.
- Install RUST without any Interaction Stackoverflow, https://stackoverflow.com/questions/57251508/run-rustups-curl-fetched-installer-script-non-interactively, 2023-03-28-Tue.
- Hosting a Flatpak Repository Blog, https://blogs.gnome.org/alexl/2017/02/10/maintaining-a-flatpak-repository/, 2023-03-31-Fri.
