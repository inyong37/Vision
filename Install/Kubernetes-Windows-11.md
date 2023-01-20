# [Deploy Windows 11 Virtual Machine on Kubernetes with KubeVirt](https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html)

## Requirements

- You’ll need a Kubernetes cluster with worker node(s) that have at least 6GB of available memory
- KubeVirt and CDI both deployed on the cluster
- A storage backend, such as Rook Ceph
- A Windows iso. One can be found at https://www.microsoft.com/software-download/windows11

```Bash
$ export KUBEVIRT_MEMORY_SIZE=8192M
$ export KUBEVIRT_STORAGE=rook-ceph-default
$ make cluster-up && make cluster-sync
```

---

### Reference
- KubeVirt: installing Microsoft Windows 11 from an ISO ,https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html, 2023-01-20-Fri.
