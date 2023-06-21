# Node Affinity

## Date

2023-06-21-Wednesday.

## Environment

* Ubuntu 22.04.2 LTS
  * Kubernetes 1.24.10

## Set a Label on a Node

```Bash
kubectl label node {node_name} {label}={name}
# kubectl label node node001 role=nginx
```

## Verify

```Bash
kubectl get node --show-labels
```

### Reference
- Node Affinity Blog KR, https://kimjingo.tistory.com/144, 2023-06-21-Wed.
