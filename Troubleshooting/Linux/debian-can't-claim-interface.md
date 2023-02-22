# Can't claim interface while connecting ACR122U

## Date

2023-02-22-Wednesday.

## Environment

Debian GNU/Linux 11 (Bullseye)

## Problem

I installed the ARC122U driver and checked the pcsc status, but it doesn't connect due to conflict

## [Solution](https://ludovicrousseau.blogspot.com/2013/11/linux-nfc-driver-conflicts-with-ccid.html)

### Remove/move file

```Bash
mv /lib/modules/*/kernel/drivers/nfc/pn533 $HOME/pn533-backup
```

### Restart `pcscd`

```Bash
systemctl restart pcscd
```

### :tada: Verify

Using systemctl:

```Bash
root@DESKTOP-8AI2B51:~# systemctl status pcscd
● pcscd.service - PC/SC Smart Card Daemon
     Loaded: loaded (/lib/systemd/system/pcscd.service; indirect; vendor preset: enabled)
     Active: inactive (dead) since Wed 2023-02-22 16:07:09 KST; 1s ago
TriggeredBy: ● pcscd.socket
       Docs: man:pcscd(8)
    Process: 8235 ExecStart=/usr/sbin/pcscd --foreground --auto-exit (code=exited, status=0/SUCCESS)
   Main PID: 8235 (code=exited, status=0/SUCCESS)
        CPU: 46ms

Feb 22 16:06:03 DESKTOP-8AI2B51 systemd[1]: Started PC/SC Smart Card Daemon.
Feb 22 16:07:09 DESKTOP-8AI2B51 systemd[1]: pcscd.service: Succeeded.
```

Using pcsc tool:

```Bash
root@DESKTOP-8AI2B51:~# pcsc_scan
Using reader plug'n play mechanism
Scanning present readers...
0: ACS ACR122U 00 00

Wed Feb 22 16:06:05 2023
 Reader 0: ACS ACR122U 00 00
  Event number: 0
  Card state: Card removed,
 \
```

---

### Reference
- https://ludovicrousseau.blogspot.com/2013/11/linux-nfc-driver-conflicts-with-ccid.html, 2023-02-22-Wed.
