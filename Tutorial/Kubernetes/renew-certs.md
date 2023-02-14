# Renew Certification

## Date

2023-02-14-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## [Renew](https://danawalab.github.io/kubernetes/2022/03/28/Renew-Kubernates.html)

Backup keys:

```Bash
cp -fR /etc/kubernetes/pki/ /etc/kubernetes/pki-backup/
```

Renew all:

```Bash
kubeadm certs renew all
```

Check keys renewed:

```Bash
kubeadm certs check-expiration
```

Backup configurations:

```Bash
cp -fR /etc/kubernetes/ /etc/kubernetes-backup/
```

Update configurations:

```Bash
kubeadm kubeconfig user --client-name=admin
kubeadm kubeconfig user --org system:masters --client-name kubernetes-admin > /etc/kubernetes/admin.conf
kubeadm kubeconfig user --client-name system:kube-controller-manager > /etc/kubernetes/controller-manager.conf
kubeadm kubeconfig user --org system:nodes --client-name system:node:$(hostname) > /etc/kubernetes/kubelet.conf
kubeadm kubeconfig user --client-name system:kube-scheduler > /etc/kubernetes/scheduler.conf
```

Restart services:

```Bash
systemctl daemon-reload && systemctl restart kubelet
```

---

:tada:

> <img width="817" alt="Screenshot 2023-02-14 at 4 22 15 PM" src="https://user-images.githubusercontent.com/20737479/218666904-2ec6b60a-ae2b-4959-99fa-6dfae2dd391e.png">

---

### Reference
- Kubernetes 인증서 만료시 갱신 방법, https://danawalab.github.io/kubernetes/2022/03/28/Renew-Kubernates.html, 2023-02-14-Tue.
- Organizing Cluster Access Using kubeconfig Files, https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/, 2023-02-14-Tue.
- Renewing Kubernetes 1.14.x cluster certificates, https://www.ibm.com/docs/en/fci/1.0.3?topic=kubernetes-renewing-114x-cluster-certificates, 2023-02-14-Tue.
- Certificate Management with kubeadm, https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/, 2023-02-14-Tue.
- Renewing Kubernetes cluster certificates, https://www.ibm.com/docs/en/fci/1.1.0?topic=kubernetes-renewing-cluster-certificates, 2023-02-14-Tue.
