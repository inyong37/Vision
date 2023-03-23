# Install flat-manager for Building Flatpak Repository on CentOS

## Date

2023-03-22-Wednesday.

## Environment

CentOS Linux release 7.9.2009 (Core)

## Install

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

```Bash
```

```Bash
```

```Bash
```

```Bash
```


---

### Reference
- flat-manager GitHub, https://github.com/flatpak/flat-manager, 2023-03-22-Wed.
- Rustup Install, https://forge.rust-lang.org/infra/other-installation-methods.html, 2023-03-22-Wed.
- Fedora & RHEL Version, https://docs.fedoraproject.org/en-US/quick-docs/fedora-and-red-hat-enterprise-linux/index.html, 2023-03-23-Thu.
- Ostree Version Fedora, https://bodhi.fedoraproject.org/updates/?packages=ostree&page=2, 2023-03-23-Thu.
