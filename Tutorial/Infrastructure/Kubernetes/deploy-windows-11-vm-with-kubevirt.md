# [Deploy Windows 11 VM with KubeVirt](https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html)

## Environment

Ubuntu 18.04.6 LTS -> Ubuntu 20.04.5 LTS

Kubernetes 1.26.0 -> Kubernetes 1.24.0

## Requirements

- You’ll need a Kubernetes cluster with worker node(s) that have at least 6GB of available memory
- KubeVirt and CDI both deployed on the cluster
- A storage backend, such as Rook Ceph
- A Windows iso. One can be found at https://www.microsoft.com/software-download/windows11

```Bash
export KUBEVIRT_MEMORY_SIZE=8192M
export KUBEVIRT_STORAGE=rook-ceph-default
# make cluster-up && make cluster-sync
```

## Preparation

```Bash
virtctl image-upload pvc win11cd-pvc --size 6Gi --image-path=/storage/win11.iso --insecure
```

> <img width="784" alt="Screenshot 2023-02-02 at 5 23 31 PM" src="https://user-images.githubusercontent.com/20737479/216270273-503e8c90-e3eb-4767-b71f-84733c1e6e32.png">

---

### Reference
- KubeVirt: installing Microsoft Windows 11 from an ISO, https://kubevirt.io/2022/KubeVirt-installing_Microsoft_Windows_11_from_an_iso.html, 2023-01-20-Fri.
- Installing a Windows VM from an ISO in Kubernetes with KubeVirt, https://youtu.be/MBvm48v43g0, 2023-01-25-Wed.
- [DIAMANTI] Use Case: How to run windows POD Using Kubevirt on Diamanti, https://knk1034.medium.com/diamanti-use-case-how-to-run-windows-pod-using-kubevirt-on-diamanti-f966f69c46bb, 2023-01-25-Wed.
- kubevirt-crc-windows-tutorial, https://redhat-developer-demos.github.io/kubevirt-crc-windows-tutorial/, 2023-02-02-Thu.
