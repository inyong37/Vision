# Kubernetes delet deployment

## Date

2023-02-09-Thursday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## Contents

### 1. get deployments

A. Using `deployments`

```Bash
root@master01:~# kubectl get deployments -A -o wide
NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS                IMAGES                                      SELECTOR
kube-system   calico-kube-controllers   0/1     1            0           2d    calico-kube-controllers   docker.io/calico/kube-controllers:v3.25.0   k8s-app=calico-kube-controllers
kube-system   coredns                   2/2     2            2           2d    coredns                   registry.k8s.io/coredns/coredns:v1.8.6      k8s-app=kube-dns
```

B. Using `deploy`:

```Bash
root@master01:~# kubectl get deploy -A -o wide
NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS                IMAGES                                      SELECTOR
kube-system   calico-kube-controllers   0/1     1            0           2d    calico-kube-controllers   docker.io/calico/kube-controllers:v3.25.0   k8s-app=calico-kube-controllers
kube-system   coredns                   2/2     2            2           2d    coredns                   registry.k8s.io/coredns/coredns:v1.8.6      k8s-app=kube-dns
```

### 2. delete a deployment

A. Using `deployments`:

```Bash
root@master01:~# kubectl delete deployments calico-kube-controllers -n kube-system
deployment.apps "calico-kube-controllers" deleted
```

B. Using `deploy`:

```Bash
root@master01:~# kubectl delete deploy calico-kube-controllers -n kube-system
deployment.apps "calico-kube-controllers" deleted
```

---
### Reference
- How to Delete a Kubernetes Deployment [Quick K8s Tips], https://linuxhandbook.com/kubectl-delete-deployment/, 2023-02-09-Thu.
- Stop the existing Deployments
, https://www.ibm.com/docs/en/control-desk/7.6.1.x?topic=containers-stop-existing-deployments, 2023-02-09-Thu.
