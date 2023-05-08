# Get Ports

## Date

2023-05-08-Monday.

## Environemt

Ubuntu 20.04.1 LTS

Kubernetes 1.23.3

## Get Ports

### Install a Package

```Bash
apt-get install -y jq
```

### Get Ports

```Bash
kubectl get svc --all-namespaces -o json | jq '.items[] | {name:.metadata.name, ns:.metadata.namespace, p:.spec.ports[] } | select( .p.nodePort != null ) | "\(.ns)/\(.name): localhost:\(.p.nodePort) -> \(.p.port) -> target-port:\(.p.targetPort)"'
```

---

### Reference
- Get Ports Stackoverflow, https://stackoverflow.com/questions/58878764/kubectl-list-all-port-forwards-across-all-services, 2023-05-08-Mon.
