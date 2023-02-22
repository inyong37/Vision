# Install NFC 

## Date

2023-02-22-Wednesday

## Enviroment

Debian GNU/Linux 11 (bullseye)

## [Content](https://github.com/Rylern/ACR122U-tutorial)

### Verify

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

```Bash
root@DESKTOP-8AI2B51:~/ACS-Unified-Driver-Lnx-Mac-118-P/acsccid-1.1.8# systemctl status pcscd
● pcscd.service - PC/SC Smart Card Daemon
     Loaded: loaded (/lib/systemd/system/pcscd.service; indirect; vendor preset: enabled)
     Active: inactive (dead) since Wed 2023-02-22 11:24:08 KST; 24s ago
TriggeredBy: ● pcscd.socket
       Docs: man:pcscd(8)
    Process: 17741 ExecStart=/usr/sbin/pcscd --foreground --auto-exit (code=exited, status=0/SUCCESS)
   Main PID: 17741 (code=exited, status=0/SUCCESS)
        CPU: 58ms

Feb 22 11:21:32 DESKTOP-8AI2B51 systemd[1]: Started PC/SC Smart Card Daemon.
Feb 22 11:21:32 DESKTOP-8AI2B51 pcscd[17741]: 00000000 ccid_usb.c:746:OpenUSBByName() Can't claim interface 1/5: LIBUSB_ERROR_BUSY
Feb 22 11:21:32 DESKTOP-8AI2B51 pcscd[17741]: 00000429 ifdhandler.c:204:CreateChannelByNameOrChannel() failed
Feb 22 11:21:32 DESKTOP-8AI2B51 pcscd[17741]: 00000017 readerfactory.c:1120:RFInitializeReader() Open Port 0x200000 Failed (usb:072f/2200:libudev:0:/dev/bus/usb/001/005)
Feb 22 11:21:32 DESKTOP-8AI2B51 pcscd[17741]: 00000023 readerfactory.c:380:RFAddReader() ACS ACR122U init failed.
Feb 22 11:21:32 DESKTOP-8AI2B51 pcscd[17741]: 00000142 hotplug_libudev.c:526:HPAddDevice() Failed adding USB device: ACS ACR122U
Feb 22 11:24:08 DESKTOP-8AI2B51 systemd[1]: pcscd.service: Succeeded.
```

---

### Reference
- ACR122 Driver, https://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/, 2023-02-22-Wed.
- Install NFC Card Reader GitHub, https://github.com/Rylern/ACR122U-tutorial, 2023-02-22-Wed.
- LC_CTYPE Error Blog KR, https://timte.tistory.com/46, 2023-02-22-Wed.
- NFC Driver Conflict, https://ludovicrousseau.blogspot.com/2013/11/linux-nfc-driver-conflicts-with-ccid.html, 2023-02-22-Wed.
- rmmod Error Stackoverflow, https://stackoverflow.com/questions/42429871/device-driver-cannot-remove-rmmod-error-module-is-in-use, 2023-02-22-Wed.
