# :construction: Set-up 'flat-manager' Client

## Date

2023-03-27-Monday.

## Environment

Ubuntu 22.04.1 LTS

## Set-up 'flat-manager' Client

```Bash
apt install flatpak flatpak-builder cargo libpq-dev postgresql postgresql-contrib pkg-config libssl-dev python3-aiohttp python3-pip git -y
apt install gir1.2-ostree-1.0 libostree-dev -y
pip3 install tenacity
```

```Bash
git clone https://github.com/flatpak/flat-manager.git
cd flat-manager/
export REPO_TOKEN=$(echo -n "secret" | base64 | cargo run --bin gentoken -- --base64 --secret-file - --name testtoken)
./flat-manager-client push --commit $(./flat-manager-client create https://35a7-220-94-163-20.jp.ngrok.io stable) local-repo

