# error: linking with `cc` failed: exit status: 1

## Date

20203-03-21-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

## Problem

While building flat-manager with cargo, an error occured:

```Bash
error: linking with `cc` failed: exit status: 1
```

## [Solution](https://github.com/rust-lang/rust/issues/25289)

```Bash
apt install gcc-multilib
```

---

### Reference
- error linking with cc failed GitHub Issue, https://github.com/rust-lang/rust/issues/25289, 2023-03-21-Tue.
