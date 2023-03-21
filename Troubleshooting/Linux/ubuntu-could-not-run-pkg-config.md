# Could not run `"pkg-config" "--libs" "--cflags" "glib-2.0" "glib-2.0 >= 2.48"`

## Date

2023-03-21-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

## Problem

I was trying to build "flat-manager" with cargo:

```Bash
root@server:~# cd flat-manager/
root@server:~/flat-manager# cargo build
```

But an error occured:

```Bash
warning: Could not run `"pkg-config" "--libs" "--cflags" "glib-2.0" "glib-2.0 >= 2.48"`

error: failed to run custom build command for `glib-sys v0.14.0`

Caused by:
  process didn't exit successfully: `/root/flat-manager/target/debug/build/glib-sys-d0fffa16856d2be9/build-script-build` (exit status: 1)
    --- stdout
  cargo:rerun-if-env-changed=GLIB_2.0_NO_PKG_CONFIG
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
  cargo:warning=Could not run `"pkg-config" "--libs" "--cflags" "glib-2.0" "glib-2.0 >= 2.48"`
  The pkg-config command could not be found.

  Most likely, you need to install a pkg-config package for your OS.
  Try `apt install pkg-config`, or `yum install pkg-config`,
  or `pkg install pkg-config` depending on your distribution.

  If you've already installed it, ensure the pkg-config command is one of the
  directories in the PATH environment variable.

  If you did not expect this build to link to a pre-installed system library,
  then check documentation of the glib-sys crate for an option to
  build the library from source, or disable features or dependencies
  that require pkg-config.
```

## [Solution](https://webcreate.tistory.com/entry/pkgconfig-command-not-found-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95)

### Install `pkg-config`

```Bash
apt install pkg-config
```

---

### Reference
- pkg-config Command Error Blog KR, https://webcreate.tistory.com/entry/pkgconfig-command-not-found-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95, 2023-03-21-Tue.
