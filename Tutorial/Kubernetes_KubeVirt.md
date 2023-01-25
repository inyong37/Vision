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
$ kubectl get vmis
```

## Accessing VMs (serial console)

```Bash
$ kubectl virt console testvm
$ virtctl console testvm
```

## Delete the virtual machine

```Bash
$ kubectl delete vm testvm
```

---

### Reference

- Use KubeVirt, https://kubevirt.io/labs/kubernetes/lab1.html, 2023-01-25-Wed.
