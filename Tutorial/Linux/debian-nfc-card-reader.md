# Install NFC Card Reader

## Date

2023-02-22-Wednesday

## Enviroment

Debian GNU/Linux 11 (bullseye)

NFC Card Reader ACR122U

## [Install](https://github.com/Rylern/ACR122U-tutorial)

:key: All commands are executed on root authority

```Bash
wget https://www.acs.com.hk/download-driver-unified/12030/ACS-Unified-Driver-Lnx-Mac-118-P.zip
unzip ACS-Unified-Driver-Lnx-Mac-118-P.zip
cd ACS-Unified-Driver-Lnx-Mac-118-P/
apt install -y pcscd libpcsclite1 libusb-1.0-0 flex perl pkg-config libpcsclite-dev libusb-1.0-0-dev
tar -xf acsccid-1.1.8.tar.bz2
cd acsccid-1.1.8/
./configure
make
make install
systemctl start pcscd
systemctl enable pcscd
echo "blacklist pn533_usb" | tee -a /etc/modprobe.d/blacklist-libnfc.conf
```

---

### Reference
- ACR122 Driver, https://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/, 2023-02-22-Wed.
- Install NFC Card Reader GitHub, https://github.com/Rylern/ACR122U-tutorial, 2023-02-22-Wed.
- LC_CTYPE Error Blog KR, https://timte.tistory.com/46, 2023-02-22-Wed.
- NFC Driver Conflict, https://ludovicrousseau.blogspot.com/2013/11/linux-nfc-driver-conflicts-with-ccid.html, 2023-02-22-Wed.
- rmmod Error Stackoverflow, https://stackoverflow.com/questions/42429871/device-driver-cannot-remove-rmmod-error-module-is-in-use, 2023-02-22-Wed.
