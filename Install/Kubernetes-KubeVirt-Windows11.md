# [Deploy Windows 11 on Kubernetes with KubeVirt](https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html)

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
- Installing a Windows VM from an ISO in Kubernetes with KubeVirt, https://youtu.be/MBvm48v43g0, 2023-01-25-Wed.
- [DIAMANTI] Use Case: How to run windows POD Using Kubevirt on Diamanti, https://knk1034.medium.com/diamanti-use-case-how-to-run-windows-pod-using-kubevirt-on-diamanti-f966f69c46bb, 2023-01-25-Wed.
