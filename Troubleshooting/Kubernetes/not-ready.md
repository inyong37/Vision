# Kubernetes Nodes' status are NotReady

## Date

2023-02-02-Thursday.

## Environment

Ubuntu 20.04.5 LTS

## Problem

After organizing cluster, master and worker nodes are at NotReady state.

> <img width="1031" alt="Screenshot 2023-02-02 at 1 51 30 PM" src="https://user-images.githubusercontent.com/20737479/216234534-890ce0e2-5e6f-436b-a2b5-205914baf0d7.png">

This is because, I didn't deploy a pod network as the instruction:

> <img width="537" alt="Screenshot 2023-02-02 at 1 51 52 PM" src="https://user-images.githubusercontent.com/20737479/216234593-c0deaaef-15b8-4ce7-a98a-d45b527ffd98.png">

There are some coredns pods pending state:

> <img width="934" alt="Screenshot 2023-02-02 at 1 53 11 PM" src="https://user-images.githubusercontent.com/20737479/216234757-44490f8c-54bd-4e57-90ca-570f664af012.png">

## [Solution](https://nirsa.tistory.com/292)

Edit `kube-flannel.yml`

```Bash
kubectl edit cm coredns -n kube-system
```

Comment out `loop`:

```
...
# loop
...
```

Verify coredns is working and nodes are ready:

> <img width="1002" alt="Screenshot 2023-02-02 at 1 57 09 PM" src="https://user-images.githubusercontent.com/20737479/216235303-63e87a7d-fe8f-4a0d-875c-6f6e3176fb11.png">

> <img width="371" alt="Screenshot 2023-02-02 at 1 58 59 PM" src="https://user-images.githubusercontent.com/20737479/216235522-8020694b-d8e2-4e5e-b21d-641d70d03476.png">

---

### Reference
- [Kubernetes] 쿠버네티스 master node "NotReady" 해결 방법 (coredns pending), https://nirsa.tistory.com/292, 2023-02-02-Thu.
