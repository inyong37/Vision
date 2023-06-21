# Pod Pending: 1 node(s) had untolerated taint

## Date

2023-06-21-Wednesday.

## Environment

* Ubuntu 22.04.2 LTS
  * Kubernetes 1.24.10
 
## Problem

`kubectl get pods -A -o wide`:

```Bash
STATUS
Pending
```

`kubectl describe pod {pod_name} -n {namespace}`:

```Bash
Events:
  Type     Reason            Age                   From               Message
  ----     ------            ----                  ----               -------
  Warning  FailedScheduling  33s (x39 over 3h10m)  default-scheduler  0/5 nodes are available: 1 node(s) had untolerated taint {node-role.kubernetes.io/control-plane: }, 4 node(s) didn't match Pod's node affinity/selector. preemption: 0/5 nodes are available: 5 Preemption is not helpful for scheduling.
```

## Solution

### Check Nodes

```Bash
kubectl describe node {node_name}
```

### Delete Node

```Bash
kubectl taint nodes --all node-role.kubernetes.io/master-
```

---

### Reference
- Taint Blog KR, https://velog.io/@baeyuna97/%ED%95%B4%EA%B2%B0-01-nodes-are-available-1-nodes-had-taints-that-the-pod-didnt-tolerate, 2023-06-21-Wed.
