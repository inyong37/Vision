# Renew the Certificates

## Date

2023-02-14-Tuesday.

## Environment

Ubuntu 22.04.1 LTS

Kubernetes 1.24.10

## [Renew](https://danawalab.github.io/kubernetes/2022/03/28/Renew-Kubernates.html)

### 1. Backup Configurations

```Bash
cp -fR /etc/kubernetes/ /etc/kubernetes-backup/ # pki at /etc/kubernetes/pki/
```

### 2. Renew the Certificates

```Bash
kubeadm certs renew all
```

### 3. Restart the Services

```Bash
systemctl daemon-reload
systemctl restart kubelet
```

### Finally, Check the Certificates

```Bash
kubeadm certs check-expiration
```

---

### Reference
- Kubernetes 인증서 만료시 갱신 방법, https://danawalab.github.io/kubernetes/2022/03/28/Renew-Kubernates.html, 2023-02-14-Tue.
- Renewing Kubernetes cluster certificates, https://www.ibm.com/docs/en/fci/1.1.0?topic=kubernetes-renewing-cluster-certificates, 2023-02-14-Tue.
- Certificate Management with kubeadm, https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/, 2023-02-14-Tue.
- Organizing Cluster Access Using kubeconfig Files, https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/, 2023-02-14-Tue.
