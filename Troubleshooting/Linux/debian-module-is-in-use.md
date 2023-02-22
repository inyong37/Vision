# rmmod: Error: Module is in use

## Date

2023-02-22-Wednesday.

## Environment

Debian GNU/Linux 11 (bullseye)

## Problem

A conflict occurred between pcsc and linux subsystem nfc, so I ran the rmmod command, but an error occurred.

## [Solution](https://stackoverflow.com/questions/42429871/device-driver-cannot-remove-rmmod-error-module-is-in-use)

### Use `-f` Option

```Bash
rmmod -f pn533
```

---

### Reference
- Module is in use Stackoverflow, https://stackoverflow.com/questions/42429871/device-driver-cannot-remove-rmmod-error-module-is-in-use, 2023-02-22-Wed.
