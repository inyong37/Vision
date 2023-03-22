# error" linker `cc` not found

## Date

2023-03-22-Wednesday.

## Environment

CentOS 7

## Problem

While building 'flatpak-manager', an error occured:

```Bash
error: linker `cc` not found
  |
  = note: No such file or directory (os error 2)
```

## [Solution](https://trendoceans.com/fix-linker-cc-not-found/)

Install development tools:

```Bash
dnf groupinstall "Development Tools"
```

---

### Reference
- Fix linker cc not found Error Blog, https://trendoceans.com/fix-linker-cc-not-found/, 2023-03-22-Wed.
