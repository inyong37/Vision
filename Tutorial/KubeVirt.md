# [Use KubeVirt](https://kubevirt.io/labs/kubernetes/lab1.html)

## Requirement

- Kubernetes
- KubeVirt

## Create a Virtual Machine

```Bash
$ kubectl apply -f https://kubevirt.io/labs/manifests/vm.yaml
```

## Start the Virtual Machine

A. Installed virtctl via krew:

```Bash
$ kubectl virt start testvm
```

B. Otherwise:

```Bash
$ virtctl start testvm
```

C. Using `kubectl patch`

```Bash
$ kubectl patch virtualmachine testvm --type merge -p \
    '{"spec":{"running":true}}'
```

## Stop/shutdown the virtual machine

A. Installed virtctl via krew:

```Bash
$ kubectl virt stop testvm
```

B. Otherwise:

```Bash
$ virtctl stop testvm
```

C. Using `kubectl patch`:

```Bash
$ kubectl patch virtualmachine testvm --type merge -p \
    '{"spec":{"running":false}}'
```

## Check virtual machines

```Bash
$ kubectl get vm
```

> <img width="240" alt="Screenshot 2023-01-25 at 3 29 06 PM" src="https://user-images.githubusercontent.com/20737479/214495683-25686f1f-1df9-4d2f-8ead-b145b82d0295.png">

```Bash
$ kubectl get vmis
```

> <img width="393" alt="Screenshot 2023-01-25 at 3 29 24 PM" src="https://user-images.githubusercontent.com/20737479/214495716-dc8cd50d-c189-4afd-8760-4ad053e1a07c.png">

## [Accessing Virtual Machines](https://kubevirt.io/user-guide/virtual_machines/accessing_virtual_machines/)

### A. CLI (console)

```Bash
$ kubectl virt console testvm
$ virtctl console testvm
```

> <img width="474" alt="Screenshot 2023-01-25 at 3 30 06 PM" src="https://user-images.githubusercontent.com/20737479/214495804-3a4e5fb2-b83b-4c2c-94f9-7a7b17cb3f25.png">

### B. GUI (VNC)

```Bash
$ kubectl virt vnc testvm
$ virtctl vnc testvm
```

## Delete the virtual machine

```Bash
$ kubectl delete vm testvm
```

---

### Reference

- Use KubeVirt, https://kubevirt.io/labs/kubernetes/lab1.html, 2023-01-25-Wed.
- Accessing Virtual Machines, https://kubevirt.io/user-guide/virtual_machines/accessing_virtual_machines/, 2023-01-25-Wed.
