# Minikube

## Environment

Ubuntu 22.04.1 LTS Jammy

minikube 1.28.0

Kubernetes 1.24.0

## Content

### Start

```Bash
$ minikube start
```

> <img width="736" alt="Screenshot 2023-01-31 at 10 35 50 AM" src="https://user-images.githubusercontent.com/20737479/215636893-e42997d5-c5ec-4e2d-97c7-6ed7057c907f.png">

### Start with specified Kubernetes version

```Bash
$ $ minikube start --kubernetes-version v1.24.0
```

<img width="666" alt="Screenshot 2023-01-31 at 10 57 10 AM" src="https://user-images.githubusercontent.com/20737479/215640086-42e6f732-249b-4201-aa2a-dabdad3bbb6a.png">

### Downgrade

<img width="830" alt="Screenshot 2023-01-31 at 10 43 17 AM" src="https://user-images.githubusercontent.com/20737479/215638025-06b59d66-6a05-48db-8601-af1af6c9b6cd.png">

### Compatible

<img width="594" alt="Screenshot 2023-01-31 at 10 58 16 AM" src="https://user-images.githubusercontent.com/20737479/215640286-49517ef7-3de4-4461-bbf7-fc2b32f643f5.png">

---

### Reference
- Check Ubuntu, https://www.ionos.com/digitalguide/server/know-how/check-ubuntu-version/#:~:text=Open%20the%20terminal%20using%20%E2%80%9CShow,Description%E2%80%9D%20and%20%E2%80%9CRelease%E2%80%9D., 2023-01-31-Tue.
- Configuration, https://minikube.sigs.k8s.io/docs/handbook/config/, 2023-01-31-Tue.
- stop, https://minikube.sigs.k8s.io/docs/commands/stop/, 2023-01-31-Tue.
