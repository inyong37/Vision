# Change Static IP Address

## Date

2023-04-14-Friday.

## Environment

Fedora 37

## Change Static IP Address

### 1. Check Current Devices

```Bash
nmcli dev status
```

Output:

```Bash
DEVICE  TYPE      STATE      CONNECTION
eno1    ethernet  connected  eno1
lo      loopback  unmanaged  --
```

### 2. Modify Static IP Address

```Bash
sudo nmcli connection modify {device_name=eno1} IPv4.address {new_ip_address}
```

### 3. Restart Connection

```Bash
sudo nmcli connection down {device_name=eno1}
sudo nmcli connection up {device_name=eno1}
```

---

### Reference
- Change Static IP Address, https://linuxhint.com/configure-static-ip-address-fedora/, 2023-04-14-Fri.
