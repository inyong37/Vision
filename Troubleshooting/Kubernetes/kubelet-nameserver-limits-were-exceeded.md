# kubelet Warning: Nameserver limits were exceeded.

## Date

2023-02-14-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Problem

```bash
Warning  DNSConfigForming        61s (x25 over 6m8s)    kubelet            Nameserver limits were exceeded, some nameservers have been omitted, the applied nameserver line is: 192.126.63.1 192.168.2.135 8.8.8.8
```

## [Solution](https://www.ibm.com/support/pages/how-fix-kube-event-nameserver-limits-were-exceeded-some-nameservers-have-been-omitted)

Reduce the number of nameservers (DNS) no more than three.

---

### Reference
- How to fix kube event "Nameserver limits were exceeded, some nameservers have been omitted."?, https://www.ibm.com/support/pages/how-fix-kube-event-nameserver-limits-were-exceeded-some-nameservers-have-been-omitted, 2023-02-14-Tue.
