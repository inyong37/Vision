# SSH Connection Refused During Installing Kubectl

## Environment

Ubuntu 18.04.6 LTS

Kubernetes 1.26.0

## Date

2023-01-12-Thursday

## Problem

After installing `kubectl` and restart it, ssh reconnect is refused.

## [Solution](https://blog.hkwon.me/ubuntu-18-04-netplan/)

When I checked the device's IPv4 setup, the dhcp4 has set 'true'. However, the server has to be set up static IP.

Therefore, I edited the netplan file as below.

### Setup static IP address with using `netplan`

Edit the static IP address:

```bash
$ vim /etc/netplan/*.yaml
```

Result:

```vim
root@node4:/etc/netplan# ip addr
1: 10: <LOOPBACK, UP ,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
	link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
	inet 127.0.0.1/8 scope hast 10
		valid_Ift forever preferred_Ift forever
	inet6 :: 1/128 scope host
		valid_Ift forever preferred_1ft forever
2: eno1: <BROADCAST, MULTICAST, UP, LOWER_UP> mtu 1500 adisc ma state UP group default qlen 1000
	link/ether 08:94 :ef:4e:ac:7e brd ff:ff:ff:ff:ff:ff altname enp17s0f0
	inet 192.168.1.237/24 brd 192.168.1.255 scope global eno1
		valid_Ift forever preferred_Ift forever
	inet6 fe80::a94:efff: fee: ac7e/64 scope link
		valid_Ift forever preferred_Ift forever
3: eno2: <NO-CARRIER, BROADCAST, MULTICAST, UP> mtu 1500 qdisc mq state DOWN group default qien 1000
	link/ether 08:94:ef:4e:ac:7f brd ff:ff:ff:ff:ff:ff
	altname enp17s0f1
4: eno3: <NO-CARRIER, BROADCAST, MULTICAST, UP> mtu 1500 qdisc mq state DONN group default qlen 1000
	1ink/ether 08:94:ef :4e:ac:80 brd ff:ff:ff:ff:ff:ff
	altname enp17s0f2
5: eno4: <NO-CARRIER, BROADCAST, MULTICAST, UP> mtu 1500 adisc mq state DONN group default qlen 1000
	link/ether 08:94:ef:4e:ac:81 brd ff:ff:ff:ff:ff:ff
	altname enp17s0f3
7: enxoa94ef4eac85: <BROADCAST, MULTICAST, UP, LOWER _UP> mtu 1500 qdisc fq codel state UNKNOWN group default qien 1000
	1ink/ether 0a:94:ef:4e:ac:85 brd ff:ffeff:ff:ff:ff
	inet 169.254.95.120/24 metric 100 brd 169.254.95.255 scope global dynamic enx0a94ef4eac85
		valid_ift 564sec preferred_1ft 564sec
	inet6 fe8o: :894:efff:fee:ac85/64 scope Link
		valid_Ift forever preferred_Ift forever
```

Apply the change:

```bash
$ netplan apply
```

Result:

```
# This is the network config written by 'subiquity"
network:
	ethernets:
		eno1:
			dhcp4: no
				addresses: (192.168.1.237/24)
				gateway4: 192.168.1.1
				nameservers:
					addresses:
					- 192.168.2.135
		eno2:
			nameservers:
				addresses:
				- 8.8.8.8
				- 8.8.8.8
				- 192.168.2.135
				- 168.126.63.1
				search: []
		eno3:
			dhcp4: true
		eno4:
			dhcp4: true
		enx0a94ef4eac85:
			dhcp4: true
version: 2
```

---

### Reference
- Ubuntu 18.04 Netplan을 사용한 Static IP 설정: [https://blog.hkwon.me/ubuntu-18-04-netplan/](https://blog.hkwon.me/ubuntu-18-04-netplan/)
