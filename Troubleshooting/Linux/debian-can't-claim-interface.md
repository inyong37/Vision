# Can't claim interface while connecting ACR122U

## Date

2023-02-22-Wednesday.

## Environment

Debian GNU/Linux 11 (Bullseye)

## Problem

I installed the ARC122U driver and checked the pcsc status, but it doesn't connect due to conflict.

```Bash
root@DESKTOP-8AI2B51:~/ACS-Unified-Driver-Lnx-Mac-118-P/acsccid-1.1.8# systemctl status pcscd
● pcscd.service - PC/SC Smart Card Daemon
     Loaded: loaded (/lib/systemd/system/pcscd.service; indirect; vendor preset: enabled)
     Active: active (running) since Wed 2023-02-22 11:16:57 KST; 1min 24s ago
TriggeredBy: ● pcscd.socket
       Docs: man:pcscd(8)
   Main PID: 17059 (pcscd)
      Tasks: 3 (limit: 4470)
     Memory: 608.0K
        CPU: 35ms
     CGroup: /system.slice/pcscd.service
             └─17059 /usr/sbin/pcscd --foreground --auto-exit

Feb 22 11:16:57 DESKTOP-8AI2B51 systemd[1]: Started PC/SC Smart Card Daemon.
Feb 22 11:16:57 DESKTOP-8AI2B51 pcscd[17059]: 00000000 ccid_usb.c:746:OpenUSBByName() Can't claim interface 1/5: LIBUSB_ERROR_BUSY
Feb 22 11:16:57 DESKTOP-8AI2B51 pcscd[17059]: 00000456 ifdhandler.c:204:CreateChannelByNameOrChannel() failed
Feb 22 11:16:57 DESKTOP-8AI2B51 pcscd[17059]: 00000018 readerfactory.c:1120:RFInitializeReader() Open Port 0x200000 Failed (usb:072f/2200:libudev:0:/dev/bus/usb/001/005)
Feb 22 11:16:57 DESKTOP-8AI2B51 pcscd[17059]: 00000010 readerfactory.c:380:RFAddReader() ACS ACR122U init failed.
Feb 22 11:16:57 DESKTOP-8AI2B51 pcscd[17059]: 00000164 hotplug_libudev.c:526:HPAddDevice() Failed adding USB device: ACS ACR122U
```

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
